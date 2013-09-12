__author__ = 'artyom'

from time import sleep
import robo3pi as robot


def main():
    robot.init('com4')
    adjacent_permutation('1', '2', '4')
    sleep(0.2)
    x_permutation('2', '4', '1')

def turn_robot(id, left_speed, right_speed):
    robot.move(id, left_speed, right_speed)
    sleep(0.4)
    robot.stop(id)
    sleep(0.2)
	
def adjacent_permutation(robot_id_1, robot_id_2, robot_id_3):
    #permutaion of robot_id_1 and robot_id_2
    robot.move(robot_id_3, 20, 20)
    sleep(0.2)
    # make each of the two turn left/right and move forward a little
    turn_robot(robot_id_1, 38, -50)
    turn_robot(robot_id_2, -50, 38)
    robot.move(robot_id_1, 40, 40)
    sleep(1.3)
    robot.stop(robot_id_1)
    sleep(0.2)
    robot.move(robot_id_2, 40, 40)
    sleep(1.3)
    robot.stop(robot_id_2)
    sleep(0.2)

    
    # turn the robots back to the original shape
    turn_robot(robot_id_1, -50, 38)
    turn_robot(robot_id_2, 38, -50)
    robot.move(robot_id_1, 50, 50)
    sleep(2)
    robot.stop(robot_id_1)
    sleep(0.2)
    robot.addToGroup(robot_id_1, '6')
    sleep(0.2)
    robot.addToGroup(robot_id_2, '6')
    sleep(0.2)
    robot.move('6',40,40)
    sleep(2.5)
    robot.stop('6')
    sleep(0.2)
    robot.stop(robot_id_3)
   #########################################


def x_permutation(robot_id_1, robot_id_2, robot_id_3):
    # used for switching two robots on the same horizontal line
    # switching robot_id_1 and robot_id_2, robot_id_3 is the third robot
    robot.addToGroup(robot_id_1, '7')
    sleep(0.4)
    robot.addToGroup(robot_id_2, '7')
    sleep(0.4)
	
    robot.move(robot_id_3, 20, 20)
    sleep(0.2)
    robot.stop('7')
    sleep(0.2)
    robot.move(robot_id_1, 50, -38)
    sleep(0.2)
    robot.stop(robot_id_1)
    sleep(0.2)
    robot.move(robot_id_2, -38, 50)
    sleep(0.15)
    robot.stop(robot_id_2)
    sleep(0.2)
    robot.move(robot_id_1, 40, 40)
    sleep(4.1)
    robot.move(robot_id_1, -38, 50)
    sleep(0.2)
    robot.stop(robot_id_1)
    sleep(0.2)
    robot.move(robot_id_2, 40, 40)
    sleep(3.8)
    robot.move(robot_id_2, 50, -38)
    sleep(0.2)
    robot.stop(robot_id_2)
    sleep(0.2)
    robot.move(robot_id_3, 20, 20)
    sleep(0.3)
	
    robot.move('7', 40, 40)
    sleep(2)
    robot.stop('7')
    sleep(0.5)
    robot.stop(robot_id_3)
	
    sleep(0.4)
    robot.addToGroup(robot_id_3, '7')
    sleep(0.4)
    robot.move('7', 40, 40)
    sleep(1.5)
    robot.stop('7')
     

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
