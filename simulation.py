import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import time

import robot
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.gravX, c.gravY, c.gravZ)

        self.world = WORLD()
        self.robot = ROBOT()


    def run(self):
        for i in range(c.loopLength):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(1 / 1000)

    def __del__(self):
        p.disconnect()
