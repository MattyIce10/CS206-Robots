from math import pi
import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import random
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

backLeg_amplitude = 2*numpy.pi
backLeg_frequency = 20
backLeg_phaseOffset = numpy.pi/8

frontLeg_amplitude = numpy.pi/10
frontLeg_frequency = 5
frontLeg_phaseOffset = numpy.pi/2

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
line = numpy.linspace(0, 2*numpy.pi, 1000)

frontLeg_targetAngles = (numpy.pi/4)*numpy.sin(frontLeg_frequency * line + frontLeg_phaseOffset)
backLeg_targetAngles = (numpy.pi/4)*numpy.sin(backLeg_frequency * line + backLeg_phaseOffset)


for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


	pyrosim.Set_Motor_For_Joint(

		bodyIndex= robotId,

		jointName=b'Torso_BackLeg',

		controlMode=p.POSITION_CONTROL,

		targetPosition=backLeg_targetAngles[i],

		maxForce=15)
	pyrosim.Set_Motor_For_Joint(

		bodyIndex=robotId,

		jointName=b'Torso_FrontLeg',

		controlMode=p.POSITION_CONTROL,

		targetPosition=frontLeg_targetAngles[i],

		maxForce=15)
	time.sleep(1/240)

numpy.save('data/values.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
numpy.save('data/frontLeg_targetAngles.npy', frontLeg_targetAngles)
numpy.save('data/backLeg_targetAngles.npy', backLeg_targetAngles)


p.disconnect()