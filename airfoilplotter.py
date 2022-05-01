from math import *
import numpy as np
import matplotlib.pyplot as plt

file = "NACA2723.txt"
f = open(file, 'r')

# get x and y coordinates
coordinatedata = [] 
coordinatedata = np.array([ line.split() for line in f])

x_coordinates = []
y_coordinates = []

for i in range(len(coordinatedata)):
    x_coordinates.append(float(coordinatedata[i][0])/100)
    y_coordinates.append(float(coordinatedata[i][1])/100)

# close airfoil data file
f.close()

plt.plot(x_coordinates,y_coordinates)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.show()