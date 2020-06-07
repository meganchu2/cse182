# Megan Chu
# PID: A12814546
# Assignment 5
# 6/11/18

import sys
from random import *
import math

print("Running Q4(calculate F function)...")

input_file = sys.argv[1]
B1 = [-.4,.45,.01,0]
B2 = [-.15,1,.1,.2]
p = 0
m = 0
p1Sum = 0
p2Sum = 0
m1Sum = 0
m2Sum = 0

with open(input_file, "r") as x:
    x.readline()
    curr = x.readline()                        
    while len(curr) > 0:
        if curr[len(curr) - 1: len(curr)] == "\n":
            curr = curr[0:len(curr) - 1]
        curr = curr.split("\t")
        val1 = 0
        val2 = 0
        for i in range(0, len(B1)):
            val1 += float(curr[i])*B1[i]
            val2 += float(curr[i])*B2[i]
        if curr[4] == "+":
            p += 1
            p1Sum += val1
            p2Sum += val2
        elif curr[4] == "-":
            m += 1
            m1Sum += val1
            m2Sum += val2
        curr = x.readline()
p1Mean = p1Sum/p
p2Mean = p2Sum/p
m1Mean = m1Sum/m
m2Mean = m2Sum/m
p1Var = 0
p2Var = 0
m1Var = 0
m2Var = 0
with open(input_file, "r") as x:
    x.readline()
    curr = x.readline()                        
    while len(curr) > 0:
        if curr[len(curr) - 1: len(curr)] == "\n":
            curr = curr[0:len(curr) - 1]
        curr = curr.split("\t")
        val1 = 0
        val2 = 0
        for i in range(0, len(B1)):
            val1 += float(curr[i])*B1[i]
            val2 += float(curr[i])*B2[i]
        if curr[4] == "+":
            p1Var += math.pow(val1-p1Mean,2)
            p2Var += math.pow(val2-p2Mean,2)
        elif curr[4] == "-":
            m1Var += math.pow(val1-m1Mean,2)
            m2Var += math.pow(val2-m2Mean,2)
        curr = x.readline()
print("Beta = ["+str(B1[0])+","+str(B1[1])+","+str(B1[2])+","+str(B1[3])+"]^T" )
print("\tF = " + str(math.pow(p1Mean-m1Mean,2)/(p1Var+m1Var)))
print("Beta = ["+str(B2[0])+","+str(B2[1])+","+str(B2[2])+","+str(B2[3])+"]^T" )
print("\tF = " + str(math.pow(p2Mean-m2Mean,2)/(p2Var+m2Var)))    
