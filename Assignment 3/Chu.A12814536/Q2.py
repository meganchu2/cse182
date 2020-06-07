# Megan Chu
# PID: A12814536
# Assignment 3
# 5/14/18

from statistics import mean
import sys
from random import *
import math

print("Running Q2...")

n = math.pow(10,7)
m = math.pow(10,7)
L = 100
w0 = [5,11,15,20,25,30,35,40]

for w in w0:
    w = int(w)
    print(str(w), end = "\t")
    print("1:" + str(math.pow(.25, w)*L*L) + " ~ " + str(1/(math.pow(.25, w)*L*L)), end = "\t")
    print(str(1-math.pow(1-math.pow(.85,w),L-w)))
