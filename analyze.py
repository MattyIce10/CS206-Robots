import numpy as n
import matplotlib.pyplot
backLegSensorValues = n.load('data/values.npy')
frontLegSensorValues = n.load('data/frontLegSensorValues.npy')
print(backLegSensorValues)
print(frontLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label = "backLegSensorValues", linewidth = 3)
matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLegSensorValues")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

