__author__ = 'artyom'
import wx
from simulation import GUI

if __name__ == '__main__':
    app = wx.App()
    GUI.SimulationGUI(None, title="Simulation")
    app.MainLoop()