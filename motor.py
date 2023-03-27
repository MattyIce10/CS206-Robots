import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        print(jointName)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):

            self.amplitude = c.amplitude
            self.frequency = c.frequency
            self.offset = c.offset
            self.motorValues = self.amplitude * numpy.sin(self.frequency * c.line + self.offset)

            if self.jointName == b'Torso_BackLeg':
                print("Worked")
                self.motorValues = self.amplitude * numpy.sin(.5 * self.frequency * c.line + self.offset)

    def Set_Value(self, robot, i):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot.robotId,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=self.motorValues[i],

            maxForce=c.force)

    def Save_Values(self):
        numpy.save('data/motorValues.npy', self.motorValues)

