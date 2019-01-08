# Alex Wilkinson
# awilki13
# CS 370
# Homework 5

#!/usr/bin/env python3
#
# Description. Evaluates problem set 3.2 # 10 on page 143 of the textbook using least squares curve fitting
#			   to predict the thermal efficiency of a year 2000 steam engine.
from numpy import array,zeros
from polyFit import *
import pylab

def evalPoly(c,x): # c stores coefficients for polynomial
    m = len(c) - 1 # (copied from polyFit module)
    p = c[m]
    for j in range(m):
        p = p*x + c[m-j-1]
    return p

xData = array([1718,1767,1774,1775,1792,1816,1828,1834,1878,1906])
yData = array([0.5,0.8,1.4,2.7,4.5,7.5,12.0,17.0,17.2,23.0])

minsdev=float("inf")
minpoly=0
n=len(xData)
print('Degree  Stdev   2000P')
for m in range(1,6):   # Try m=1,2,3,4,5 (degree of polynomial)
    ys=zeros((n),dtype='float') # initialize y-coordinates for polynomial curve

    # calculate the polynomial coefficients and standard deviation using polyFit and stdDev from polyFit.py
    coeff = polyFit(xData,yData,m) # get coefficients for n-th degree polynomial
    stdev = stdDev(coeff,xData,yData) # get stdev of the error in the fit

    #evaluate the polynomial using the function inside the stdDev function in polyFit.py
    proj  = evalPoly(coeff,2000) # evaluate the polynomial at year 2000
#
#   Year 2000 projections >= 100 or < 0 are meaniningless        
#
    if (stdev < minsdev) and proj < 100 and proj > 0 :

        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'viable'))
        # get y-coordinates of polynomial using x-coordinates in xData array
        #use the loop and evalPoly function from polyFit.py to calculate the y value for each x value in xData
        for y in range(n):
        	ys[y] = evalPoly(coeff,xData[y])


#       Use Matplotlib to plot original data points with validated curve fitting
#
        pylab.xlabel("x")
        pylab.ylabel("Thermal Efficiency")
        my_title= 'Fit with poly degree = ' + str(m) + '; green dot is 2000 projection'
        pylab.title(my_title)
        pylab.xlim(1710,2015)            # x-axis values should range from 1710 to 2015
        pylab.plot(2000,proj,'go')            # plot Year 2000 projection as a green dot
        pylab.plot(xData,yData,'ro')            # plot the original data given in the xData and yData
                                   # arrays as red dots
        pylab.plot(xData, ys, 'b-')            # plot polynomial curve using xData and ys arrays
                                   # and make it blue.
        pylab.grid()
        pylab.show()
    else :
        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'not viable'))
#--------------------------------------------------------------------------------------
# Table to stdout should look similar to this...
#
# Degree Stdev   2000P
#   1 	 2.855	 34.986	    viable
#   2	 2.768	 45.419	    viable
#   3	 2.266	 -6.602	    not viable
#   4	 2.234	 112.391	not viable
#   5	 2.496	 113.726	not viable
#--------------------------------------------------------------------------------------
