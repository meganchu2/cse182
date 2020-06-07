# Megan Chu
# PID: A12814546
# Assignment 5
# 6/11/18

import sys
from random import *
import math

print("Running Q1(calculate distance from hyperplane)...")

input_file = sys.argv[1]
B = [-.15,.9,.05,-.02]
B0 = .88
minV = math.inf
minP = 0

print("Beta = ["+str(B[0])+","+str(B[1])+","+str(B[2])+","+str(B[3])+"]^T" )
print("Beta0 = "+str(B0))
print("gene1\tgene2\tgene3\tgene4\tlabel\tdist")

with open(input_file, "r") as x:
    x.readline()
    curr = x.readline()
    
    while len(curr) > 0:
        if curr[len(curr) - 1: len(curr)] == "\n":
            curr = curr[0:len(curr) - 1]
        print(curr, end = "\t")
        curr = curr.split("\t")
        dist = -1*B0
        for i in range(0, len(B)):
            dist += float(curr[i])*B[i]
        if math.fabs(dist) < minV:
            minV = math.fabs(dist)
            minP = curr
        print(round(dist,10))
        curr = x.readline()
print("\nPoint closest to hyperplane: ")
print(str(minP[0])+"\t"+str(minP[1])+"\t"+str(minP[2])+"\t"+str(minP[3])+"\t"+str(minP[4])+"\t"+str(round(minV,10)))
    
