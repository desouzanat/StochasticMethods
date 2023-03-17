# Nathalia De Souza -- Stochastic Methods 2 -- 2/6/2023

import numpy as np
from random import uniform ; from math import sin; from math import pi
from scipy.integrate import quad
import matplotlib.pyplot as plt
import random


nTrials = 1000
fxCount = 0 # number of points that fall under the curve
sqCount = 0 # number of total points calculated

yLim = []
xLim = np.linspace(-2,3, num=1000)
for x in xLim:
    yLim.append(x**3 * sin(x))

yMax = max(yLim)

for i in range(nTrials):
    iter = i
    xPt = random.uniform(-2, 3)
    yPt = random.uniform(0, yMax)

    point = (xPt, yPt)  # finds random, uniformly distributed x and y values in a square of length 5 and height 10
    
    # if the point is within the area of interest is is counted
    if yPt < (xPt**3 * sin(xPt)): 
        fxCount+=1
    sqCount += 1

    # color points blue if they are underneath the curve and red if above
    if yPt <= (xPt**3 * sin(xPt)):
        col = 'blue'
    else:
        col = 'red'

    sqArea = yMax * 5
    estimate = (float(fxCount)/float(sqCount)) * sqArea # this is my estimated solution to the function

    actual = quad(lambda x: x**3 * sin(x), -2, 3) # this is the true solution to the function
    
    # exit the for loop when the estimated solution is within 0.1% of the true solution
    tol = 0.01
    if estimate <= actual[0]:
       error = actual[0] - estimate
       if error < tol:
        break
       
    allPts =  plt.scatter(xPt, yPt, c=str(col), s=10)

print("\n\n**************")
print("The true solution to the function is {0:.6f}.".format(actual[0]))
print("The estimated solution to the function after {0:.0f}".format(iter), "iterations", "is {0:.6f}.".format(estimate))
print("The difference between the true and estimated values of the solution is {0:.6f}.".format(error))
print("**************\n\n")

fxnPlot = plt.plot(xLim, yLim, 'k', linewidth =2)
fig = plt.gcf()
ax = fig.gca()
plt.title("n = {0:.0f}, Estimate = {1:.6f}".format(iter, estimate), fontsize = 10)
plt.suptitle("Monte Carlo Integration of $f(x) = x^3sin(x)$", fontsize = 15)
plt.xlabel('x')
plt.ylabel('y')
plt.show()









