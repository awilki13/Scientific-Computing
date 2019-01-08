# Alex Wilkinson
# awilki13
# August 2013 High Temps for Knoxville,TN
# Homework 1 for COSC 370

from numpy import arange
import matplotlib.pyplot as plt
xData = arange(1,32)    # Ranges for x and y axes must match
tData = [86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81, \
         75,80,81,85,81,88,89,87,84,85,86,88,88,90,90]
avg = [86.]  # First value for montly avg high temp is just Day 1 temp

## 1) CALCULATE A RUNNING MONTHLY AVERAGE AND PRINT IT OUT IN A TABLE
##    IT DOES NOT MATTER HOW THE TABLE IS FORMATTED
sum = 0
count = 0
# Create a running list of averages
for temp in tData :
	count = count + 1
	sum = temp + sum
	if count > 1 :
		avg.append(sum/count)
day = 1
# Iterate through avg list and print them out. Round to 2 decimal places
for average in avg :
	print('August', day, '2013 Average:', "%.2f" % average)
	day = day + 1

## 2) CREATE A GRAPH FOR THE DATA USING MATPLOTLIB
##	- PLOT RED POINTS WITH BLUE LINE FOR ORIGINAL DATA
##	- SHOW CHANGE IN AVERAGE HIGH WITH GREEN DASHED LINE
##	- SET DISPLAY RANGES FOR X AND Y AXES
##		- X SHOULD RANGE FROM 0 TO 32
##		- Y SHOULD RANGE FROM 70 TO 95
##	- ENABLE GRID DISPLAY
##	- LABEL AXES AND SET TITLE
##	- USE MATPLOTLIB.PYPLOT.TEXT() TO LABEL THE MONTHLY AVERAGE LINE

# Plot red circles
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],[86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81,75,80,81,85,81,88,89,87,84,85,86,88,88,90,90], 'ro')
# Plot blue lines
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],[86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81,75,80,81,85,81,88,89,87,84,85,86,88,88,90,90], 'b-')
# Plot green dashes monthly average
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], avg, 'g--')
plt.axis([0, 32, 70, 95])
# Plot the grid
plt.grid()
# Label the title and x and y axis
plt.ylabel('High Temp')
plt.xlabel('Day')
plt.title('High Temperatures for Knoxville, TN - August 2013')

## label for the monthly average line
plt.text(15, 86, 'Monthly Avg', color='green', fontsize=13.5)
plt.show()

