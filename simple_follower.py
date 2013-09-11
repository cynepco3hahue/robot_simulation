import robo3pi as s
import time


# This function makes the robot with the given id move along a track with a
#  ~25cm part of a straight line, and a circular part with radius ~10cm.
#  All time and speed calculations are done empirically.

def follow_the_line(id):
    def make_n_turns(n):
        for i in range(n):
            s.move(id, -20, 20)
            time.sleep(0.35)
            s.move(id, 20, 20)
            time.sleep(0.5)
    # to be used later on

    def fix_location(id):
        pos = s.readLinePosition(id)
        time.sleep(0.2)
        if pos != "":
            # get real value of each character
            val = ord(pos[0]) + (ord(pos[1]) << 8)
            if val > 2200: # the robot is too left to the line
                print 'value is {0}, moving right'.format(val)
                s.move(id, 20, -20)
                time.sleep(0.35)
                s.move(id, 20, 20)
                time.sleep(0.35)
            elif val < 1800: # the robot is far to the right of the line
                print 'value is {0}, moving left'.format(val)
                s.move(id, -20, 20)
                time.sleep(0.35)
                s.move(id, 20, 20)
                time.sleep(0.35)
            else: # the robot is centered on the line
                print 'value is {0}, moving forward'.format(val)
                s.move(id, 40, 40)
                time.sleep(1)
                s.move(id, 20, 20)
                time.sleep(0.3)

    s.init("/dev/ttyUSB0")
    #s.readCalibratedSensors(id, 1)
    #time.sleep(0.35)
    start = time.time()
    while time.time() - start < 60: # for one minute
        s.move(id, 20, 20)
        time.sleep(3.2)
        make_n_turns(3)
        s.move(id, -20, 20)
        time.sleep(0.7)
        s.move(id, 20, 20)
        #fix_location(id)
        time.sleep(1.7)
        s.move(id, -20, 20)
        time.sleep(0.5)
    s.stop(id)


follow_the_line('5')
