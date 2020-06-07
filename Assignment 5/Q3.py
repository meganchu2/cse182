# Megan Chu
# PID: A12814546
# Assignment 5
# 6/11/18

import sys
from random import *
import math

print("Running Q3(grid search)...")

input_file = sys.argv[1]
B = [-2,-2,-2,-2]
B0 = -1
minE = math.inf
minB = [-2,-2,-2,-2]
minBNorm = [-2,-2,-2,-2]
minB0 = 2
norm = [-1,-.9,-.8,-.7,-.6,-.5,-.4,-.3,-.2,-.1,0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
norm0 = [0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]

for i1 in norm:
    for i2 in norm:
        for i3 in norm:
            for i4 in norm:
                for B0 in norm0:
                    B2 = math.sqrt(math.pow(i1,2)+math.pow(i2,2)+math.pow(i3,2)+math.pow(i4,2))
                    if B2 == 0:
                        break
                    B = [i1/B2,i2/B2,i3/B2,i4/B2]
                    error = 0
                    with open(input_file, "r") as x:
                        x.readline()
                        curr = x.readline()                        
                        while len(curr) > 0:
                            if curr[len(curr) - 1: len(curr)] == "\n":
                                curr = curr[0:len(curr) - 1]
                            curr = curr.split("\t")
                            dist = -1*B0
                            for i in range(0, len(B)):
                                dist += float(curr[i])*B[i]
                            if (dist < 0 and curr[4] == "+") or (dist > 0 and curr[4] == "-"):
                                error += math.fabs(dist)
                            curr = x.readline()
                        if error < minE:
                            minE = error
                            minB = [i1,i2,i3,i4]
                            minBNorm = B
                            minB0 = B0
print("Beta = ["+str(minB[0])+","+str(minB[1])+","+str(minB[2])+","+str(minB[3])+"]^T" )
print("BetaNorm = ["+str(minBNorm[0])+","+str(minBNorm[1])+","+str(minBNorm[2])+","+str(minBNorm[3])+"]^T" )
print("Beta0 = " + str(minB0))
print("Minimum Classification Error = " + str(minE))
    
