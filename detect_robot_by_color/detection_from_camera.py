__author__ = 'artyom'

''' multi_color_two_object.py

Go through multi_color_multiple_points_track.py well before reading this script.

This program tracks only two objects of two different colors
(yellow and blue here) to draw to different lines independent of each other.
In multi_color_multiple_points_track.py, we get a line connecting those blobs.
Here each blob draws its own independent lines.
I have uploaded an image "multi_track.png" to show you what i got.

Disadvantage:- It applies only for different colors, not for same color.
This seems not to be a good method when there is large number of objects.


Brought to you by Abid.K 			mail me at abidrahmank@gmail.com
'''
#############################################################################

import cv
global imghsv


def get_thresholded_img(im):
    '''
    this function take RGB image.Then convert it into HSV for easy colour
    detection and threshold it with yellow and blue part as white and all
    other regions as black.Then return that image
    '''

    global imghsv

    cv.CvtColor(im, imghsv, cv.CV_BGR2HSV)				# Convert image from RGB to HSV

    # A little change here. Creates images for all colors
    img_yellow = cv.CreateImage(cv.GetSize(im), 8, 1)
    img_blue = cv.CreateImage(cv.GetSize(im), 8, 1)
    img_red = cv.CreateImage(cv.GetSize(im), 8, 1)
    img_green = cv.CreateImage(cv.GetSize(im), 8, 1)
    img_magneta = cv.CreateImage(cv.GetSize(im), 8, 1)

    # Select a range of yellow color
    cv.InRangeS(imghsv, cv.Scalar(20, 100, 100),
                cv.Scalar(30, 255, 255), img_yellow)
    # Select a range of blue color
    cv.InRangeS(imghsv, cv.Scalar(100, 100, 100),
                cv.Scalar(130, 255, 255), img_blue)
    # Select a range of red color
    cv.InRangeS(imghsv, cv.Scalar(0, 100, 100),
                cv.Scalar(10, 255, 255), img_red)
    # Select a range of green color
    cv.InRangeS(imghsv, cv.Scalar(50, 100, 100),
                cv.Scalar(70, 255, 255), img_green)
    # Select a range of magneta color
    cv.InRangeS(imghsv, cv.Scalar(140, 100, 100),
                cv.Scalar(160, 255, 255), img_magneta)

capture = cv.CaptureFromCAM(0)
frame = cv.QueryFrame(capture)
frame_size = cv.GetSize(frame)
test = cv.CreateImage(cv.GetSize(frame), 8, 3)
img2 = cv.CreateImage(cv.GetSize(frame), 8, 3)
cv.NamedWindow("Real", 0)
cv.NamedWindow("Threshold", 0)
cv.NamedWindow("final", 0)

#	Create two lists to store co-ordinates of blobs
blue = []
yellow = []
red = []
green = []
magneta = []

while 1:
    color_image = cv.QueryFrame(capture)
    img_draw = cv.CreateImage(cv.GetSize(frame), 8, 3)
    cv.SetZero(img_draw)
    cv.Flip(color_image, color_image, 1)
    cv.Smooth(color_image, color_image, cv.CV_GAUSSIAN, 3, 0)
    img_yellow_thresh = get_thresholded_img(color_image)
    cv.Erode(img_yellow_thresh, img_yellow_thresh, None, 3)
    cv.Dilate(img_yellow_thresh, img_yellow_thresh, None, 10)
    img2 = cv.CloneImage(img_yellow_thresh)
    storage = cv.CreateMemStorage(0)
    contour = cv.FindContours(img_yellow_thresh, storage,
                              cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
    points = []

#	This is the new part here. ie Use of cv.BoundingRect()
    while contour:
        # Draw bounding rectangles
        bound_rect = cv.BoundingRect(list(contour))
        contour = contour.h_next()
        print contour
        # for more details about cv.BoundingRect,see documentation
        pt1 = (bound_rect[0], bound_rect[1])
        pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
        points.append(pt1)
        points.append(pt2)
        cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255, 0, 0), 1)

        #	Calculating centroids

        centroid_x = cv.Round((pt1[0]+pt2[0])/2)
        centroid_y = cv.Round((pt1[1]+pt2[1])/2)

    #	Identifying if blue or yellow blobs and adding centroids
    #  to corresponding lists
        print cv.Get2D(imghsv, centroid_y, centroid_x)[0]
        if 140 < cv.Get2D(imghsv, centroid_y, centroid_x)[0] < 160:
            magneta.append((centroid_x, centroid_y))
        elif 100 < cv.Get2D(imghsv, centroid_y, centroid_x)[0] < 130:
            blue.append((centroid_x, centroid_y))
        elif 0 < cv.Get2D(imghsv, centroid_y, centroid_x)[0] < 10:
            red.append((centroid_x, centroid_y))
        elif 50 < cv.Get2D(imghsv, centroid_y, centroid_x)[0] < 70:
            green.append((centroid_x, centroid_y))
        elif 20 < cv.Get2D(imghsv, centroid_y, centroid_x)[0] < 30:
            yellow.append((centroid_x, centroid_y))

    #Now drawing part. Exceptional handling is used to avoid IndexError.
    #After drawing is over, centroid from previous part is
    #removed from list by pop. So in next frame,centroids in this frame
    # become initial points of line to draw.
    try:
        cv.Circle(img_draw, yellow[1], 5, (0, 255, 255))
        cv.Line(img_draw, yellow[0], yellow[1], (0, 255, 255), 3, 8, 0)
        yellow.pop(0)
    except IndexError:
        print "Just wait for yellow"
    try:
        cv.Circle(img_draw, blue[1], 5, (255, 0, 0))
        cv.Line(img_draw, blue[0], blue[1], (255, 0, 0), 3, 8, 0)
        blue.pop(0)
    except IndexError:
        print "just wait for blue"
    try:
        cv.Circle(img_draw, red[1], 5, (0, 0, 255))
        cv.Line(img_draw, red[0], red[1], (0, 0, 255), 3, 8, 0)
        red.pop(0)
    except IndexError:
        print "Just wait for red"
    try:
        cv.Circle(img_draw, green[1], 5, (0, 255, 0))
        cv.Line(img_draw, green[0], green[1], (0, 255, 0), 3, 8, 0)
        green.pop(0)
    except IndexError:
        print "Just wait for green"
    try:
        cv.Circle(img_draw, magneta[1], 5, (255, 0, 255))
        cv.Line(img_draw, magneta[0], magneta[1], (255, 0, 255), 3, 8, 0)
        magneta.pop(0)
    except IndexError:
        print "Just wait for magneta"
    cv.Add(test, img_draw, test)

    cv.ShowImage("Real", color_image)
    cv.ShowImage("Threshold", img2)
    cv.ShowImage("final", test)
    if cv.WaitKey(33) == 1048603:
        cv.DestroyWindow("Real")
        cv.DestroyWindow("Threshold")
        cv.DestroyWindow("final")
        break
#############################################################################