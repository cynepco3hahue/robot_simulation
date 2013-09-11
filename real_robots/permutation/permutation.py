__author__ = 'artyom'

from time import sleep
import robo3pi as robot


def main():
    robot.init('/dev/ttyUSB0')
    adjacent_permutation('1', '2')
    x_permutation('2', '3', '1')


def adjacent_permutation(robot_id_1, robot_id_2):
    #permutaion of 1 and 2(2 and 3)
     
    # make all robots move together 
    robot.addToGroup('2', '1')
    sleep(0.4)
    robot.addToGroup('3', '1')
    sleep(0.4)
    robot.move(robot_id_1, 40, 40)
    sleep(3)
    
    # separate robots no.2 and 3 from the group
    robot.removeFromGroup('3', '1')
    sleep(0.4)
    robot.move('3', 20, 20)
    sleep(0.4)
    robot.removeFromGroup('2', '1')
    sleep(0.4)
    
    # make each of the two turn left/right and move forward a little
    robot.move(robot_id_1, 38, -50)
    sleep(0.4)
    robot.stop(robot_id_1)
    sleep(0.4)
    robot.move(robot_id_2, -50, 38)
    sleep(0.4)
    robot.stop(robot_id_2)
    sleep(0.4)
    robot.move(robot_id_1, 40, 40)
    sleep(0.85)
    robot.stop(robot_id_1)
    sleep(0.4)
    robot.move(robot_id_2, 40, 40)
    sleep(1.3)
    robot.stop(robot_id_2)
    sleep(0.4)
    
    # turn the robots back to the original shape
    robot.move(robot_id_1, -50, 38)
    sleep(0.4)
    robot.stop(robot_id_1)
    sleep(0.5)
    robot.move(robot_id_2, 38, -50)
    sleep(0.5)
    robot.stop(robot_id_2)
    sleep(0.4)
    robot.stop('3')
    sleep(0.4)
    robot.move(robot_id_1, 50, 50)
    sleep(3)
    robot.stop(robot_id_1)
    sleep(0.4)
    robot.stop(robot_id_2)
    sleep(0.5)
    
    # join all three robots to one group and make them move together again
    robot.addToGroup('2', '1')
    sleep(0.4)
    robot.addToGroup('3', '1')
    sleep(0.4)
    robot.move('1', 30, 30)
    sleep(3)
    robot.stop('1')
   #########################################


def x_permutation(robot_id_1, robot_id_2, robot_id_3):
    # switching robot_id_1 and robot_id_2, robot_id_3 is the third robot
    robot.move(robot_id_3, 40, 40)
    sleep(0.4)
    robot.move(robot_id_1, 20, 20)
    sleep(0.4)
    robot.move(robot_id_2, 20, 20)
    sleep(0.4)
    robot.move(robot_id_1, 50, -38)
    sleep(0.4)
    robot.stop(robot_id_1)
    robot.move(robot_id_2, -38, 50)
    sleep(0.4)
    robot.stop(robot_id_2)
     

    ##########################3 and 5(1 and 3)######################
    #robot.addToGroup('1', '2')
    #sleep(0.4)
    #robot.addToGroup('3', '2')
    #sleep(0.4)
    #robot.addToGroup('4', '2')
    #sleep(0.4)
    #robot.move(robot_id_2, 40, 40)
    #sleep(3)
    #robot.removeFromGroup('1', '2')
    #sleep(0.4)
    #robot.removeFromGroup('4', '2')
    #sleep(0.5)
    #robot.stop('1')
    #sleep(0.5)
    #robot.stop('4')
    #sleep(1.6)
    #robot.move('2', 20, 20)
    #sleep(0.5)

    #robot.move('1', 50, -38)
    #sleep(0.4)
    #robot.stop('1')
    #sleep(0.5)
    #robot.move('4', -38, 50)
    #sleep(0.4)
    #robot.stop('4')
    #sleep(0.5)
    #robot.move('1', 80, 80)
    #sleep(1.5)
    #robot.stop('1')
    #sleep(0.5)
    #robot.move('4', 80, 80)
    #sleep(1.5)
    #robot.stop('4')
    #sleep(0.5)
    #robot.move('1', -38, 50)
    #sleep(0.4)
    #robot.stop('1')
    #sleep(0.5)
    #robot.move('4', 50, -38)
    #sleep(0.4)
    #robot.stop('4')
    #sleep(0.5)
    #robot.move('4', 80, 80)
    #sleep(3)
    #robot.addToGroup('4', '2')
    #sleep(0.5)
    #robot.addToGroup('1', '2')
    #sleep(0.5)
    #robot.move('2', 40, 40)
    #sleep(2)
    #robot.stop('2')
##########################################################################


if __name__ == '__main__':
    main()
