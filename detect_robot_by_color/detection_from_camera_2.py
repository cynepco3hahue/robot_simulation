__author__ = 'artyom'

import cv


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


class Target:
    def __init__(self):
        self.capture = cv.CaptureFromCAM(0)
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
            cv.InRangeS(hsv_img, cv.Scalar(20, 100, 100),
                        cv.Scalar(30, 255, 255), orange_threshold)
            # Select a range of blue color
            cv.InRangeS(hsv_img, cv.Scalar(100, 100, 100),
                        cv.Scalar(130, 255, 255), blue_threshold)
            # Select a range of yellow color
            cv.InRangeS(hsv_img, cv.Scalar(35, 100, 100),
                        cv.Scalar(40, 255, 255), yellow_threshold)
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

            color_points = list()

            for i in range(5):
                color_points.append(Point(0, 0))

            #there can be noise in the video so ignore objects with small
            if yellow_area > 300000:
                color_points[0].set_x(
                    int(cv.GetSpatialMoment(yellow_moment, 1, 0)/yellow_area))
                color_points[0].set_y(
                    int(cv.GetSpatialMoment(yellow_moment, 0, 1)/yellow_area))
                #draw circle
                cv.Circle(img, (color_points[0].get_x(),
                                color_points[0].get_y()), 2, (0, 255, 0), 10)

            if blue_area > 300000:
                color_points[1].set_x(
                    int(cv.GetSpatialMoment(blue_moment, 1, 0)/blue_area))
                color_points[1].set_y(
                    int(cv.GetSpatialMoment(blue_moment, 0, 1)/blue_area))
                cv.Circle(img, (color_points[1].get_x(),
                                color_points[1].get_y()), 2, (0, 255, 0), 10)

            if orange_area > 300000:
                color_points[2].set_x(
                    int(cv.GetSpatialMoment(orange_moment, 1, 0)/orange_area))
                color_points[2].set_y(
                    int(cv.GetSpatialMoment(orange_moment, 0, 1)/orange_area))
                cv.Circle(img, (color_points[2].get_x(),
                                color_points[2].get_y()), 2, (0, 255, 0), 10)

            if green_area > 300000:
                color_points[3].set_x(
                    int(cv.GetSpatialMoment(green_moment, 1, 0)/green_area))
                color_points[3].set_y(
                    int(cv.GetSpatialMoment(green_moment, 0, 1)/green_area))
                cv.Circle(img, (color_points[3].get_x(),
                                color_points[3].get_y()), 2, (0, 255, 0), 10)

            if magneta_area > 300000:
                color_points[4].set_x(
                    int(cv.GetSpatialMoment(
                        magneta_moment, 1, 0)/magneta_area))
                color_points[4].set_y(
                    int(cv.GetSpatialMoment(
                        magneta_moment, 1, 0)/magneta_area))
                print color_points[4].get_point()
                cv.Circle(img, (color_points[4].get_x(),
                                color_points[4].get_y()), 2, (0, 255, 0), 10)

            #angle = int(math.atan((y1-y2)/(x2-x1))*180/math.pi)

            #display frames to users
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
                break
        cv.DestroyAllWindows()

if __name__ == "__main__":
    t = Target()
    t.run()
