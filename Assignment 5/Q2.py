# Megan Chu
# PID: A12814546
# Assignment 5
# 6/11/18

import sys
from random import *
import math

print("Running Q2(misclassified points and classification error)...")

input_file = sys.argv[1]
B = [-.15,.9,.05,-.02]
B0 = .88
numMC = 0
error = 0

print("Beta = ["+str(B[0])+","+str(B[1])+","+str(B[2])+","+str(B[3])+"]^T" )
print("Beta0 = "+str(B0))
print("gene1\tgene2\tgene3\tgene4\tlabel\tdist")

with open(input_file, "r") as x:
    x.readline()
    curr = x.readline()
    
    while len(curr) > 0:
        if curr[len(curr) - 1: len(curr)] == "\n":
            curr = curr[0:len(curr) - 1]
        curr0 = curr
        curr = curr.split("\t")
        dist = -1*B0
        for i in range(0, len(B)):
            dist += float(curr[i])*B[i]
        if (dist < 0 and curr[4] == "+") or (dist > 0 and curr[4] == "-"):
            numMC += 1
            print(curr0 + "\t" + str(round(dist,10)) + "\tMisclassified")
            error += math.fabs(round(dist,10))
        curr = x.readline()
print("Number of misclassified points: " + str(numMC))
print("Classification error: " + str(round(error,10)))
    
