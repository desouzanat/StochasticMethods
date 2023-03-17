# Nathalia De Souza -- Stochastic Methods 1 -- 2/6/2023

import matplotlib.pyplot as plt
import numpy as np
import random as ran


times = 1000
circ_pts = 0
sq_pts = 0

center = [0, 0]
circ = 0
sq = 0
x = np.array(None)
y = np.array(None)

for i in range(times):

    # creates a random and uniformly distributed number between (-1,1)
    x = ran.uniform(-1,1)
    y = ran.uniform(-1,1)
    iter = i

    # calculating distance from the point (x,y) to the center of the circle at (0,0)
    distToOG = np.sqrt(x**2 + y**2)

    # adding one to the arrays for circ and sq whenever the distance from the origin is less than or equal to 1
    if distToOG <= 1:
        circ += 1
    sq +=1

    # coloring (x,y) blue if inside the circle and red if outside
    if distToOG <= 1:
        col = 'b'
    else: 
        col = 'r'

    # using monte carlo to estimate the value of pi
    piEst = 4 * (circ/sq)
 
    # stopping the algorithm when the estimated value of pi is within 1% of the true value of pi
    tol = 0.01
    if abs(piEst - np.math.pi) <= tol:
        break

    # plots all the points we've created and color codes them accordingly
    allPts =  plt.scatter(x, y, c=str(col), s=10)

    
print ("\n\n**************")
print ("Estimated value of pi after {0:.0f}".format(iter), "iterations", "is {0:.6f}".format(piEst))
print ("Difference from numpy pi: {0:.6f}".format(piEst - np.math.pi))
print ("**************\n\n")

circle_plot = plt.Circle((0, 0), 1, linewidth=2, fill=False)
fig = plt.gcf()
ax = fig.gca()
ax.add_patch(circle_plot)
plt.title("n = {0:.0f}, $\pi_{{est}}$ = {1:.6f}".format(iter, piEst), fontsize = 10)
plt.suptitle("Monte Carlo Approximation of $\pi$", fontsize = 15)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

