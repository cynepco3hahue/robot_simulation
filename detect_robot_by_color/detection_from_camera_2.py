__author__ = 'artyom'

import cv
import math
from time import sleep
import robo3pi as robot_api
import simulation.robot as robotClass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_point(self):
        return self.x, self.y

    def set_pos(self, x, y):
        self.x = x
        self.y = y


class Target:
    def __init__(self):
        self.capture = cv.CaptureFromCAM(1)
        self.robot = robotClass.Robot('3', 40, 0, 0, 0)
        self.start_position = Point(0, 0)
        self.start = True
        cv.NamedWindow("Target", 1)
        cv.NamedWindow("Yellow Threshold", 1)
        cv.NamedWindow("Blue Threshold", 1)
        cv.NamedWindow("Orange Threshold", 1)
        cv.NamedWindow("Green Threshold", 1)
        cv.NamedWindow("Magneta Threshold", 1)
        cv.NamedWindow("hsv", 1)

    def run(self):
        #instantiate images
        hsv_img = cv.CreateImage(cv.GetSize(cv.QueryFrame(self.capture)),
                                 8, 3)
        yellow_threshold = cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
        blue_threshold = cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
        orange_threshold = cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
        green_threshold = cv.CreateImage(cv.GetSize(hsv_img), 8, 1)
        magneta_threshold = cv.CreateImage(cv.GetSize(hsv_img), 8, 1)

        while True:
            #capture the image from the cam
            img = cv.QueryFrame(self.capture)

            #convert the image to HSV
            cv.CvtColor(img, hsv_img, cv.CV_BGR2HSV)

            # Select a range of orange color
            cv.InRangeS(hsv_img, cv.Scalar(10, 100, 100),
                        cv.Scalar(25, 255, 255), orange_threshold)
            # Select a range of blue color
            cv.InRangeS(hsv_img, cv.Scalar(100, 100, 100),
                        cv.Scalar(130, 255, 255), blue_threshold)
            # Select a range of yellow color
            cv.InRangeS(hsv_img, cv.Scalar(35, 100, 100),
                        cv.Scalar(45, 255, 255), yellow_threshold)
            # Select a range of green color
            cv.InRangeS(hsv_img, cv.Scalar(50, 100, 100),
                        cv.Scalar(70, 255, 255), green_threshold)
            # Select a range of magneta color
            cv.InRangeS(hsv_img, cv.Scalar(155, 100, 100),
                        cv.Scalar(170, 255, 255), magneta_threshold)

            #determine the moments of the five objects
            yellow_threshold = cv.GetMat(yellow_threshold)
            blue_threshold = cv.GetMat(blue_threshold)
            orange_threshold = cv.GetMat(orange_threshold)
            green_threshold = cv.GetMat(green_threshold)
            magneta_threshold = cv.GetMat(magneta_threshold)
            yellow_moment = cv.Moments(yellow_threshold, 0)
            blue_moment = cv.Moments(blue_threshold, 0)
            orange_moment = cv.Moments(orange_threshold, 0)
            green_moment = cv.Moments(green_threshold, 0)
            magneta_moment = cv.Moments(magneta_threshold, 0)
            yellow_area = cv.GetCentralMoment(yellow_moment, 0, 0)
            blue_area = cv.GetCentralMoment(blue_moment, 0, 0)
            orange_area = cv.GetCentralMoment(orange_moment, 0, 0)
            green_area = cv.GetCentralMoment(green_moment, 0, 0)
            magneta_area = cv.GetCentralMoment(magneta_moment, 0, 0)

            #initialize x and y

            color_points = {'yellow': Point(0, 0), 'blue': Point(0, 0),
                            'orange': Point(0, 0), 'green': Point(0, 0),
                            'magneta': Point(0, 0)}

            #there can be noise in the video so ignore objects with small
            if yellow_area > 300000:
                color_points['yellow'].set_x(
                    int(cv.GetSpatialMoment(yellow_moment, 1, 0)/yellow_area))
                color_points['yellow'].set_y(
                    int(cv.GetSpatialMoment(yellow_moment, 0, 1)/yellow_area))
                #draw circle
                cv.Circle(img, (color_points['yellow'].get_x(),
                                color_points['yellow'].get_y()),
                          2, (0, 255, 0), 10)
                cv.Line(img, (320, 240),
                        (color_points['yellow'].get_x(),
                         color_points['yellow'].get_y()),
                        (255, 255, 0), 2)

            if blue_area > 200000:
                sleep(0.4)
                color_points['blue'].set_x(
                    int(cv.GetSpatialMoment(blue_moment, 1, 0)/blue_area))
                color_points['blue'].set_y(
                    int(cv.GetSpatialMoment(blue_moment, 0, 1)/blue_area))
                cv.Circle(img, (color_points['blue'].get_x(),
                                color_points['blue'].get_y()),
                          2, (0, 255, 0), 10)
                cv.Line(img, (320, 240),
                        (color_points['blue'].get_x(),
                         color_points['blue'].get_y()),
                        (255, 0, 0), 2)
                print color_points['blue'].get_x(), \
                    color_points['blue'].get_y()
                if self.start:
                    self.start_position.set_pos(color_points['blue'].get_x(),
                                                color_points['blue'].get_y())
                    robot_api.move(self.robot.getId(), 25, 25)
                    self.robot.setSpeedOnWheels(25, 25)
                    self.start = False
                else:
                    self.start_position.set_pos(self.start_position.get_x(),
                                                color_points['blue'].get_y())
                self.robot.setPosition(color_points['blue'].get_x(),
                                       color_points['blue'].get_y())
                print "Real:", self.start_position.get_point()
                print "Robot:", self.robot.getRobotPos()
                if math.fabs(self.robot.getPosX() -
                             self.start_position.get_x()) > 80:
                    if self.robot.getPosX() > self.start_position.get_x():
                        robot_api.move(self.robot.getId(), 30, 25)
                        print "Move Left"
                    else:
                        robot_api.move(self.robot.getId(), 25, 30)
                        print "Move Right"
                else:
                    robot_api.move(self.robot.getId(), 25, 25)

            if orange_area > 300000:
                color_points['orange'].set_x(
                    int(cv.GetSpatialMoment(orange_moment, 1, 0)/orange_area))
                color_points['orange'].set_y(
                    int(cv.GetSpatialMoment(orange_moment, 0, 1)/orange_area))
                cv.Circle(img, (color_points['orange'].get_x(),
                                color_points['orange'].get_y()),
                          2, (0, 255, 0), 10)
                cv.Line(img, (320, 240),
                        (color_points['orange'].get_x(),
                         color_points['orange'].get_y()),
                        (0, 148, 255), 2)

            if green_area > 300000:
                color_points['green'].set_x(
                    int(cv.GetSpatialMoment(green_moment, 1, 0)/green_area))
                color_points['green'].set_y(
                    int(cv.GetSpatialMoment(green_moment, 0, 1)/green_area))
                cv.Circle(img, (color_points['green'].get_x(),
                                color_points['green'].get_y()),
                          2, (0, 255, 0), 10)
                cv.Line(img, (320, 240),
                        (color_points['green'].get_x(),
                         color_points['green'].get_y()),
                        (0, 255, 0), 2)
                # self.robot.setPosition(color_points['green'].get_x(),
                #                        color_points['green'].get_y())

            if magneta_area > 300000:
                color_points['magneta'].set_x(
                    int(cv.GetSpatialMoment(
                        magneta_moment, 1, 0)/magneta_area))
                color_points['magneta'].set_y(
                    int(cv.GetSpatialMoment(
                        magneta_moment, 0, 1)/magneta_area))
                cv.Circle(img, (color_points['magneta'].get_x(),
                                color_points['magneta'].get_y()),
                          2, (0, 255, 0), 10)
                cv.Line(img, (320, 240),
                        (color_points['magneta'].get_x(),
                         color_points['magneta'].get_y()),
                        (199, 0, 255), 2)

            #angle = int(math.atan((y1-y2)/(x2-x1))*180/math.pi)

            #display frames to users
            center = (cv.GetSize(img)[0] / 2, cv.GetSize(img)[1] / 2)
            ellipse_color = (255, 255, 255)
            for i in range(5):
                ellipse_size = (320 - i * 40, 240 - i * 40)
                cv.Ellipse(img, center, ellipse_size, 0,
                           0, 360, ellipse_color, 2)
            cv.Line(img, (320, 240), (640, 240), (0, 0, 0), 2)
            cv.ShowImage("Target", img)
            cv.ShowImage("Yellow Threshold", yellow_threshold)
            cv.ShowImage("Blue Threshold", blue_threshold)
            cv.ShowImage("Orange Threshold", orange_threshold)
            cv.ShowImage("Green Threshold", green_threshold)
            cv.ShowImage("Magneta Threshold", magneta_threshold)
            cv.ShowImage("hsv", hsv_img)
            #Listen for ESC or ENTER key
            c = cv.WaitKey(2) % 0x100
            if c == 27 or c == 10:
                robot_api.stop(self.robot.getId())
                break
        cv.DestroyAllWindows()

if __name__ == "__main__":
    robot_api.init("/dev/ttyUSB0")
    t = Target()
    t.run()
