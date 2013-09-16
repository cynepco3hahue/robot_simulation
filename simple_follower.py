import robo3pi as s
import time

################################################################
# main program - unless the robots are told differently, they should follow elliptic tracks of a size known in advance.
###############################################################

# This function makes the robot with the given id move along a track with a
#  ~25cm part of a straight line, and a circular part with radius ~10cm.
#  All time and speed calculations are done empirically.

global is_on_the_curve


def follow_the_line(id):
    id_str = str(id)

    def make_n_turns(n):
        for i in range(n):
            if i == 0:
                is_on_the_curve[id] = 1
            s.move(id_str, -20, 20)
            time.sleep(0.2)
            s.move(id_str, 20, 20)
            time.sleep(1.5)
            if i == n - 1:
                is_on_the_curve[id] = 0
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

    # at first, all robots are on the straight line
    is_on_the_curve = [0*i for i in range(5)]
    #s.readCalibratedSensors(id, 1)
    #time.sleep(0.35)
    start = time.time()
    # for one minute
    while time.time() - start < 60:
        s.move(id_str, 20, 20)
        if id == 1:
            time.sleep(9.5)
        elif id == 4 or id == 2:
            time.sleep(8)
        if id == 1:
            make_n_turns(7)
        if id == 4:
            make_n_turns(8)
        s.move(id_str, -20, 20)
        time.sleep(0.7)
    s.stop(id_str)


def main():
# The first robot to start moving is the leader of the flock
# (assuming the identity permutation),
# then the ones which are behind him, and finally those behind them.
# After one second all robots will be moving.
# Each of the robots is given different timings and set of orders according
#  to its position with respect of the rest of the flock.
    s.init('/dev/ttyUSB0')
    # follow_the_line(3)
    # time.sleep(0.4)
    # follow_the_line(2)
    # time.sleep(0.4)
    follow_the_line(4)
    time.sleep(0.4)
    #follow_the_line(1)
    #time.sleep(0.4)
    # follow_the_line(5)
    # time.sleep(0.4)

main()
