__author__ = 'artyom'

import wx
from simulation import robot
import math
import help_functions


class SimulationGUI(wx.Frame):

    def __init__(self, parent, title):
        super(SimulationGUI, self).__init__(parent, title=title,
                                            size=(800, 600))
        self.newWindow = None
        self.InitUI()
        self.Centre()
        self.Bind(wx.EVT_CLOSE, self.onExit)
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Robots Simulation")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM,
                  border=15)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 6),
                  flag=wx.EXPAND | wx.BOTTOM, border=10)

        diameter = wx.StaticText(panel, label="Radius")
        sizer.Add(diameter, pos=(2, 0), flag=wx.LEFT, border=10)
        self.tc1 = wx.TextCtrl(panel)
        sizer.Add(self.tc1, pos=(2, 1), span=(1, 4), flag=wx.TOP | wx.EXPAND)

        speed = wx.StaticText(panel, label="Speed")
        sizer.Add(speed, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=10)
        self.tc2 = wx.TextCtrl(panel)
        sizer.Add(self.tc2, pos=(3, 1), span=(1, 4), flag=wx.TOP | wx.EXPAND,
                  border=5)

        numberOfRobots = wx.StaticText(panel, label="Number of Robots")
        sizer.Add(numberOfRobots, pos=(4, 0), flag=wx.TOP | wx.LEFT, border=10)
        self.tc3 = wx.TextCtrl(panel)
        sizer.Add(self.tc3, pos=(4, 1), span=(1, 4), flag=wx.TOP | wx.EXPAND,
                  border=5)

        heigth = wx.StaticText(panel, label="Height of Rectangle")
        sizer.Add(heigth, pos=(5, 0), flag=wx.TOP | wx.LEFT, border=10)
        self.tc4 = wx.TextCtrl(panel)
        sizer.Add(self.tc4, pos=(5, 1), span=(1, 4), flag=wx.TOP | wx.EXPAND,
                  border=5)

        width = wx.StaticText(panel, label="Width of Rectangle")
        sizer.Add(width, pos=(6, 0), flag=wx.TOP | wx.LEFT, border=10)
        self.tc5 = wx.TextCtrl(panel)
        sizer.Add(self.tc5, pos=(6, 1), span=(1, 4), flag=wx.TOP | wx.EXPAND,
                  border=5)

        newOrder = wx.StaticText(panel, label="New Order")
        sizer.Add(newOrder, pos=(7, 0), flag=wx.TOP | wx.LEFT, border=10)
        self.tc6 = wx.TextCtrl(panel)
        sizer.Add(self.tc6, pos=(7, 1), span=(1, 4), flag=wx.TOP | wx.EXPAND,
                  border=5)

        dstRob = wx.StaticText(panel, label="Distance between robots")
        sizer.Add(dstRob, pos=(8, 0), flag=wx.TOP | wx.LEFT, border=10)
        self.tc7 = wx.TextCtrl(panel)
        sizer.Add(self.tc7, pos=(8, 1), span=(1, 4), flag=wx.TOP | wx.EXPAND,
                  border=5)

        self.tc1.WriteText('15')
        self.tc2.WriteText('10')
        self.tc3.WriteText('3')
        self.tc4.WriteText('400')
        self.tc5.WriteText('300')

        sb = wx.StaticBox(panel, label="Optional Attributes")

        box_sizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        box_sizer.Add(wx.CheckBox(panel, label="Folks Form"),
                      flag=wx.LEFT, border=5)
        box_sizer.Add(wx.CheckBox(panel, label="Other"),
                      flag=wx.LEFT | wx.BOTTOM, border=5)
        sizer.Add(box_sizer, pos=(9, 0), span=(1, 6),
                  flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)

        button1 = wx.Button(panel, label='Help')
        button1.Bind(wx.EVT_BUTTON, self.helpMessage)
        sizer.Add(button1, flag=wx.RIGHT | wx.TOP, pos=(0, 5), border=10)

        button2 = wx.Button(panel, label='Exit')
        button2.Bind(wx.EVT_BUTTON, self.onExit)
        sizer.Add(button2, flag=wx.LEFT, pos=(11, 0), border=10)

        button3 = wx.Button(panel, label='Start')
        button3.Bind(wx.EVT_BUTTON, self.onStart)
        sizer.Add(button3, flag=wx.LEFT, pos=(11, 3), border=10)

        button4 = wx.Button(panel, label="Change")
        button4.Bind(wx.EVT_BUTTON, self.onChange)
        sizer.Add(button4, pos=(11, 4))

        button5 = wx.Button(panel, label="Stop")
        button5.Bind(wx.EVT_BUTTON, self.onStop)
        sizer.Add(button5, pos=(11, 5))

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)

    def onChange(self, event):
        if self.newWindow.change:
            self.errorMessage("Previous Change still in progress")
            return
        list_of_ids = self.checkChangeInput()
        if list_of_ids and list_of_ids != self.newWindow.old_order:
            self.permutation = help_functions.getPermutation(self.newWindow.old_order, list_of_ids)
            for i in range(len(self.permutation)):
                self.newWindow.one_permutation = self.permutation[i]
                print self.newWindow.one_permutation
                if self.permutation[i] == (0, 1):
                    self.newWindow.robots[0].setChangeSpeed(2 * self.newWindow.robots[0].speed)
                    self.newWindow.robots[1].setChangeSpeed(self.newWindow.robots[1].speed / 2)
                    self.newWindow.robots[2].setChangeSpeed(self.newWindow.robots[2].speed / 2)
                    self.newWindow.Bind(wx.EVT_PAINT, self.newWindow.onChange1)
                    self.newWindow.timer.Stop()
                    self.newWindow.change_timer_1.Start(50)
                elif self.permutation[i] == (0, 2):
                    self.newWindow.robots[0].setChangeSpeed(self.newWindow.robots[0].speed * 2)
                    self.newWindow.robots[1].setChangeSpeed(self.newWindow.robots[1].speed * 2)
                    self.newWindow.robots[2].setChangeSpeed(self.newWindow.robots[2].speed / 2)
                    self.newWindow.Bind(wx.EVT_PAINT, self.newWindow.onChange2)
                    self.newWindow.timer.Stop()
                    self.newWindow.change_timer_2.Start(50)
                else:
                    self.newWindow.robots[2].setChangeSpeed(2 * self.newWindow.robots[2].speed)
                    self.newWindow.robots[1].setChangeSpeed(self.newWindow.robots[1].speed / 2)
                    self.newWindow.robots[0].setChangeSpeed(self.newWindow.robots[0].speed / 2)
                    self.newWindow.Bind(wx.EVT_PAINT, self.newWindow.onChange2)
                    self.newWindow.timer.Stop()
                    self.newWindow.change_timer_3.Start(50)
                self.newWindow.old_order = list_of_ids
        else:
            return

    def checkChangeInput(self):
        if self.newWindow:
            strOfIds = self.tc6.GetValue().split(',')
            if len(strOfIds) != int(self.tc3.GetValue()):
                self.errorMessage("Not valid number of ids")
                return
            listOfIds = list()
            for i in range(len(strOfIds)):
                try:
                    robotId = int(strOfIds[i])
                    if help_functions.idIsValid(robotId, self.newWindow.robots):
                        if help_functions.idOnce(strOfIds, strOfIds[i]):
                            listOfIds.append(robotId)
                        else:
                            self.errorMessage("Id %s exist more that once" % robotId)
                            return
                    else:
                        self.errorMessage("Id %s is not valid" % robotId)
                        return
                except ValueError:
                    self.errorMessage("Not valid value of id")
                    return
            return listOfIds
        else:
            return

    def onExit(self, e):
        if self.newWindow:
            self.newWindow.Destroy()
        self.Destroy()

    def helpMessage(self, e):
        text = '''Radius - radius of robot(0 < radius <= 30 cm)\nSpeed - speed for robot on outer orbit(grad/s)\nNumber of Robots - number of robots(min: 1, max: 5)\nHeight of Rectangle - Height of board(cm)\nWeight of Rectangle - Weight of board(cm)\nNew order - new permutation of robots(enter ids of robots\nseparated by comas, for example 0,1,2,3,4)\nDistance between robots - distance between robots(cm)'''
        wx.MessageBox(text, 'Help', wx.OK | wx.ICON_INFORMATION)

    def onStart(self, e):
        if not self.checkInput():
            return
        self.newWindow = NewWindow(self, parent=None, given_id=-1)
        self.newWindow.Bind(wx.EVT_PAINT, self.newWindow.onPaint)
        self.newWindow.Show()

    def onStop(self, event):
        if self.newWindow:
            if NewWindow.change:
                NewWindow.change = False
            self.newWindow.Destroy()

    def checkInput(self):
        try:
            number = self.tc1.GetValue()
            if float(number) <= 0 or float(number) > 30:
                self.errorMessage("Wrong radius value")
                return False
            number = self.tc2.GetValue()
            if float(number) <= 0 or float(number) > 30:
                self.errorMessage("Wrong speed value")
                return False
            number = self.tc3.GetValue()
            if int(number) <= 0 or int(number) > 30:
                self.errorMessage("Wrong number of robots value")
                return False
            number = self.tc4.GetValue()
            if float(number) < 100 or float(number) > 1000:
                self.errorMessage("Wrong height of rectangle")
                return
            number = self.tc5.GetValue()
            if float(number) < 100 or float(number) > 1000:
                self.errorMessage("Wrong width of rectangle")
                return False
        except ValueError:
            self.errorMessage("Wrong input, please see help for more information")
            return False
        return True

    def errorMessage(self, message):
        wx.MessageBox(message, 'ERROR', wx.OK | wx.ICON_ERROR)


class NewWindow(wx.Frame):
    LEFT_NEIGHBOR = 1
    RIGHT_NEIGHBOR = 2
    NOT_NEIGHBOR = 3
    ID_TIMER_PAINT = 11
    ID_TIMER_CHANGE_1 = 1
    ID_TIMER_CHANGE_2 = 2
    ID_TIMER_CHANGE_3 = 3
    change = False
    assigned = False

    def __init__(self, mainWindow, parent, given_id):
        self.one_permutation = None
        self.counter = 0
        self.mainWindow = mainWindow
        self.old_order = list()
        self.robotRadius = float(mainWindow.tc1.GetValue())
        self.speed = float(mainWindow.tc2.GetValue())
        self.numRobots = int(mainWindow.tc3.GetValue())
        self.height = float(mainWindow.tc4.GetValue())
        self.width = float(mainWindow.tc5.GetValue())
        self.robots = [None] * self.numRobots
        self.ellipses_size = [None] * self.numRobots
        self.angle = 0
        self.colorList = [wx.RED_BRUSH, wx.BLUE_BRUSH, wx.GREEN_BRUSH, wx.BLACK_BRUSH, wx.CYAN_BRUSH]
        for i in range(self.numRobots):
            self.old_order.append(i)
            ellipse_size_width = self.width - i * (self.robotRadius + 1) * 4
            ellipse_size_height = self.height - i * (self.robotRadius + 1) * 4
            self.ellipses_size[i] = (ellipse_size_width, ellipse_size_height)
            if self.numRobots == 5:
                if i == 1 or i == 3:
                    self.robots[i] = robot.Robot(i, self.speed, 0, 0, 12)
                elif i == 2:
                    self.robots[i] = robot.Robot(i, self.speed, 0, 0, 24)
                else:
                    self.robots[i] = robot.Robot(i, self.speed, 0, 0, 0)
            elif self.numRobots == 3 and i == 1:
                self.robots[i] = robot.Robot(i, self.speed, 0, 0, 12)
            else:
                self.robots[i] = robot.Robot(i, self.speed, 0, 0, 0)
        wx.Frame.__init__(self, parent, given_id, 'Moving', pos=(0, 0), size=(800, 640))
        self.timer = wx.Timer(self, NewWindow.ID_TIMER_PAINT)
        self.Bind(wx.EVT_TIMER, self.onTimer, id=NewWindow.ID_TIMER_PAINT)
        self.timer.Start(50)
        self.change_timer_1 = wx.Timer(self, NewWindow.ID_TIMER_CHANGE_1)
        self.Bind(wx.EVT_TIMER, self.onTimer, id=NewWindow.ID_TIMER_CHANGE_1)
        self.change_timer_2 = wx.Timer(self, NewWindow.ID_TIMER_CHANGE_2)
        self.Bind(wx.EVT_TIMER, self.onTimer, id=NewWindow.ID_TIMER_CHANGE_2)
        self.change_timer_3 = wx.Timer(self, NewWindow.ID_TIMER_CHANGE_3)
        self.Bind(wx.EVT_TIMER, self.onTimer, id=NewWindow.ID_TIMER_CHANGE_3)

    def onPaint(self, event):
        self.scenePaint(-1, -1)

    def scenePaint(self, robot_index_1, robot_index_2):
        self.realRobotData()
        dc = wx.PaintDC(self)
        size_x, size_y = self.GetSizeTuple()
        dc.DrawRectangle(0, 0, size_x, size_y)
        for i in range(self.numRobots):
            eclipse_position_x = size_x / 2 - self.ellipses_size[i][0] / 2
            eclipse_position_y = size_y / 2 - self.ellipses_size[i][1] / 2
            dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
            dc.SetBrush(wx.WHITE_BRUSH)
            dc.DrawEllipse(eclipse_position_x, eclipse_position_y, self.ellipses_size[i][0], self.ellipses_size[i][1])
        for i in range(self.numRobots):
            eclipse_position_x = size_x / 2 - self.ellipses_size[i][0] / 2
            eclipse_position_y = size_y / 2 - self.ellipses_size[i][1] / 2
            robot_position_x = eclipse_position_x + self.ellipses_size[i][0] / 2 + self.robots[i].change_pos_x
            robot_position_y = eclipse_position_y + self.ellipses_size[i][1] / 2 + self.robots[i].change_pos_y
            self.robots[i].setChangeAngle(float(self.robots[i].change_speed) / float(20) + self.robots[i].change_angle)
            if self.robots[i].change_angle >= 360:
                self.robots[i].setChangeAngle(0.0)
            if NewWindow.change and (i == robot_index_1 or i == robot_index_2):
                next_pos_x = self.robots[i].change_pos_x + self.robots[i].linear_speed_x
                next_pos_y = self.robots[i].change_pos_y + self.robots[i].linear_speed_y
            else:
                next_pos_x = (self.ellipses_size[i][0] / 2) * math.cos(
                    math.radians(self.robots[i].change_angle))
                next_pos_y = (self.ellipses_size[i][1] / 2) * math.sin(
                    math.radians(self.robots[i].change_angle))
            self.robots[i].setChangePosition(next_pos_x, next_pos_y)
            dc.SetBrush(self.colorList[self.robots[i].id])
            dc.DrawCircle(robot_position_x, robot_position_y, self.robotRadius)

    def onChange1(self, event):
        if not NewWindow.change:
            self.positionForChanging(0, 1, 2)
        self.positionAssigned(0, 1, 2, self.change_timer_1)
        self.scenePaint(0, 1)

    def onChange2(self, event):
        if not NewWindow.change:
            self.positionForChanging(0, 2, 1)
        self.positionAssigned(0, 2, 1, self.change_timer_2)
        self.scenePaint(0, 2)

    def onChange3(self, event):
        if not NewWindow.change:
            self.positionForChanging(1, 2, 0)
        self.positionAssigned(1, 2, 0, self.change_timer_3)
        self.scenePaint(1, 2)

    def onTimer(self, event):
        if event.GetId() == NewWindow.ID_TIMER_PAINT:
            self.onPaint(event)
        elif event.GetId() == NewWindow.ID_TIMER_CHANGE_1:
            self.onChange1(event)
        elif event.GetId() == NewWindow.ID_TIMER_CHANGE_2:
            self.onChange2(event)
        elif event.GetId() == NewWindow.ID_TIMER_CHANGE_3:
            self.onChange3(event)
        else:
            event.Skip()

    def realRobotData(self):
        for i in range(self.numRobots):
            self.robots[i].setAngle(float(self.robots[i].speed) / float(20) + self.robots[i].angle)
            if self.robots[i].angle >= 360:
                self.robots[i].setAngle(0.0)
            next_pos_x = (self.ellipses_size[i][0] / 2) * math.cos(
                math.radians(self.robots[i].angle))
            next_pos_y = (self.ellipses_size[i][1] / 2) * math.sin(
                math.radians(self.robots[i].angle))
            self.robots[i].setPosition(next_pos_x, next_pos_y)

    def getTime(self, robot):
        counter = 0
        change_angle = robot.change_angle
        real_angle = robot.angle
        speed = float(robot.change_speed) / float(20)
        while math.fabs(change_angle - real_angle) > 0.5:
            change_angle += speed
            if change_angle >= 360:
                change_angle = 0.0
            counter += 1
        return counter

    def getLinearSpeed(self, start_pos_x, start_pos_y, end_pos_x, end_pos_y, robot_not_change):
        diff_x = end_pos_x - start_pos_x
        diff_y = end_pos_y - start_pos_y
        time = 90
        if self.one_permutation != (0, 2):
            time = self.getTime(robot_not_change)
        return diff_x / time, diff_y / time

    def backAfterChange(self, robot_1, robot_2):
        robot_1.setChangeAngle(robot_2.start_angle)
        robot_1.setAngle(robot_2.start_angle)
        robot_2.setChangeAngle(robot_1.start_angle)
        robot_2.setAngle(robot_1.start_angle)
        for i in range(self.numRobots):
            self.robots[i].setChangeSpeed(self.speed)
            self.robots[i].setPosition(self.robots[i].change_pos_x,
                                       self.robots[i].change_pos_y)
            self.robots[i].setAngle(self.robots[i].change_angle)

    def positionAssigned(self, robot_index_1, robot_index_2, robot_index_3, change_timer):
        if math.fabs(self.robots[robot_index_1].change_pos_x - self.robots[robot_index_2].start_pos_x) < 1:
            if math.fabs(self.robots[robot_index_1].change_pos_y - self.robots[robot_index_2].start_pos_y) < 1:
                print "Position assigned"
                if self.one_permutation == (0, 2) and not NewWindow.assigned:
                    self.calculateLinearSpeed(robot_index_1, robot_index_2, robot_index_3)
                    NewWindow.assigned = True
                    return
                self.backAfterChange(self.robots[robot_index_1], self.robots[robot_index_2])
                temp_robot = self.robots[robot_index_1]
                self.robots[robot_index_1] = self.robots[robot_index_2]
                self.robots[robot_index_2] = temp_robot
                NewWindow.change = False
                NewWindow.assigned = False
                change_timer.Stop()
                self.timer.Start(50)
                return

    def positionForChanging(self, robot_index_1, robot_index_2, robot_index_3):
        diff_angle = math.fabs(self.robots[robot_index_1].change_angle - self.robots[robot_index_2].change_angle)
        if diff_angle > 300:
            diff_angle = 360 - diff_angle
        if diff_angle > 40:
            NewWindow.change = True
            print "Position for changing"
            self.calculateLinearSpeed(robot_index_1, robot_index_2, robot_index_3)
            if self.one_permutation == (0, 2):
                self.robots[1].setChangeSpeed(self.robots[1].speed / 4)

    def calculateLinearSpeed(self, robot_index_1, robot_index_2, robot_index_3):
        speed_x, speed_y = self.getLinearSpeed(self.robots[robot_index_1].change_pos_x,
                                               self.robots[robot_index_1].change_pos_y,
                                               self.robots[robot_index_2].pos_x,
                                               self.robots[robot_index_2].pos_y,
                                               self.robots[robot_index_3])
        self.robots[robot_index_1].setLinearSpeed(speed_x, speed_y)
        self.robots[robot_index_1].setStartPos(self.robots[robot_index_1].pos_x,
                                               self.robots[robot_index_1].pos_y)
        self.robots[robot_index_1].setStartAngle(self.robots[robot_index_1].angle)
        speed_x, speed_y = self.getLinearSpeed(self.robots[robot_index_2].change_pos_x,
                                               self.robots[robot_index_2].change_pos_y,
                                               self.robots[robot_index_1].pos_x,
                                               self.robots[robot_index_1].pos_y,
                                               self.robots[robot_index_3])
        self.robots[robot_index_2].setLinearSpeed(speed_x, speed_y)
        self.robots[robot_index_2].setStartPos(self.robots[robot_index_2].pos_x,
                                               self.robots[robot_index_2].pos_y)
        self.robots[robot_index_2].setStartAngle(self.robots[robot_index_2].angle)