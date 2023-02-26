import numpy as n
import matplotlib.pyplot
backLegSensorValues = n.load('data/values.npy')
frontLegSensorValues = n.load('data/frontLegSensorValues.npy')
frontLeg_targetAngles = n.load('data/frontLeg_targetAngles.npy')
backLeg_targetAngles = n.load('data/backLeg_targetAngles.npy')

#matplotlib.pyplot.plot(backLegSensorValues, label = "backLegSensorValues", linewidth = 3)
#matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLegSensorValues")

matplotlib.pyplot.plot(frontLeg_targetAngles, label = "frontLeg_targetAngles", linewidth = 3)
matplotlib.pyplot.plot(backLeg_targetAngles, label = "backLeg_targetAngles")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

