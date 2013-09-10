import robo3pi as s
import time
import math


def line_follower(id):
    #place on line
    s.readCalibratedSensors(id, 1)
    time.sleep(0.35)
    s.readCalibratedSensors(id, 0)
    time.sleep(0.35)
    start = time.time()
    while time.time() - start < 60:
        # s.readCalibratedSensors(id, 0)
        # time.sleep(0.35)
        pos = s.readLinePosition(id)
        print pos
        if pos != "":
            # get real value of each character
            val = ord(pos[0]) + (ord(pos[1]) << 8)
            print val
            if val > 2100: # the robot is too right to the line
                s.move(id, 20, -20)
                time.sleep(0.35)
                s.move(id, 30, 30)
                time.sleep(0.2)
                s.stop(id)
            elif val < 1900:
                s.move(id, -20, 20)
                time.sleep(0.35)
                s.move(id, 30, 30)
                time.sleep(0.2)
                s.stop(id)
            else:      # the robot is centered on the line
                s.move(id, 40, 40)
                time.sleep(0.2)
                s.stop(id)


def main():
    s.init('/dev/ttyUSB0')
    line_follower('2')
    time.sleep(0.2)
    s.stop('2')
    s.close()

main()