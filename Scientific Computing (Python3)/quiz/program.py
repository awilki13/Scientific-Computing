import numpy as np
from euler import *
from print import *

def F(x,y):
	F = np.zeros(2)
	F[0] = y[1]
	F[1] = -0.1*y[1] - x
	return F
x = 0.0 # Start of integration
xStop = 2.0 # End of integration
y = np.array([0.0, 1.0]) # Initial values of {y}
h = 0.05 # Step size
X,Y = integrate(F,x,y,xStop,h)
printSoln(X,Y,1)
