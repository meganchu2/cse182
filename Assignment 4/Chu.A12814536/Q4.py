# Megan Chu
# PID: A12814546
# Assignment 4
# 5/27/18

import sys
from random import *
import math

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
if count < 1:
    print("Error in arguments, please follow the following format:")
    print("python Q4.py <fasta_file> <cpgLocation_file>")
    exit()

print("Running Q4(Calculate Transformation and Emission Probabilities)...")

fasta_file = sys.argv[1]
cpG_loc = sys.argv[2]
numIslands = 0
nII = 0
nOO = 0
nIO = 0
nOI = 0
lastEnd = 0
diP = [0,0,0,0]
diM = [0,0,0,0]
plus = list()
minus = list()
for i in range(4):
    plus.append(list())
    minus.append(list())
    for j in range(4):
        plus[i].append(0)
        minus[i].append(0)

with open(cpG_loc, "r") as c:
    with open(fasta_file, "r") as f:
        n = f.readline()
        count = 0
        n = f.read(1)
        if n == " " or n == "\n":
            n = f.read(1)
        pos = 0
        prev = ""
        cx = c.readline()
        while len(cx) > 0 and cx != " "  and cx !="\n":
            numIslands += 1
            cx = cx[0:len(cx) - 1]
            cx = cx.split(" ")
            start = int(cx[0])
            end = int(cx[1])
            if start != lastEnd + 1:
                nOI += 1
            if end != 1999999: #end of chrA.fasta
                nIO += 1
            nII += (end - start)
            if end - start < 0:
                print(start)
                print(end)
            nOO += (start - 1) - (lastEnd + 1)

            while pos <= end:
                if pos >= start:
                    if n == "A":
                        diP[0] += 1
                        if prev == "A":
                            plus[0][0] += 1
                        elif prev == "C":
                            plus[1][0] += 1
                        elif prev == "G":
                            plus[2][0] += 1
                        elif prev == "T":
                            plus[3][0] += 1
                    elif n == "C":
                        diP[1] += 1
                        if prev == "A":
                            plus[0][1] += 1
                        elif prev == "C":
                            plus[1][1] += 1
                        elif prev == "G":
                            plus[2][1] += 1
                        elif prev == "T":
                            plus[3][1] += 1
                    elif n == "G":
                        diP[2] += 1
                        if prev == "A":
                            plus[0][2] += 1
                        elif prev == "C":
                            plus[1][2] += 1
                        elif prev == "G":
                            plus[2][2] += 1
                        elif prev == "T":
                            plus[3][2] += 1
                    elif n == "T":
                        diP[3] += 1
                        if prev == "A":
                            plus[0][3] += 1
                        elif prev == "C":
                            plus[1][3] += 1
                        elif prev == "G":
                            plus[2][3] += 1
                        elif prev == "T":
                            plus[3][3] += 1
                else:
                    if n == "A":
                        diM[0] += 1
                        if prev == "A":
                            minus[0][0] += 1
                        elif prev == "C":
                            minus[1][0] += 1
                        elif prev == "G":
                            minus[2][0] += 1
                        elif prev == "T":
                            minus[3][0] += 1
                    elif n == "C":
                        diM[1] += 1
                        if prev == "A":
                            minus[0][1] += 1
                        elif prev == "C":
                            minus[1][1] += 1
                        elif prev == "G":
                            minus[2][1] += 1
                        elif prev == "T":
                            minus[3][1] += 1
                    elif n == "G":
                        diM[2] += 1
                        if prev == "A":
                            minus[0][2] += 1
                        elif prev == "C":
                            minus[1][2] += 1
                        elif prev == "G":
                            minus[2][2] += 1
                        elif prev == "T":
                            minus[3][2] += 1
                    elif n == "T":
                        diM[3] += 1
                        if prev == "A":
                            minus[0][3] += 1
                        elif prev == "C":
                            minus[1][3] += 1
                        elif prev == "G":
                            minus[2][3] += 1
                        elif prev == "T":
                            minus[3][3] += 1
                pos += 1
                prev = n
                n = f.read(1)
                if n == " " or n == "\n":
                    n = f.read(1)
            
            lastEnd = end
            cx = c.readline()
        if lastEnd != 1999999:
            nOO += 1999999 - (lastEnd + 1)
            while len(n) > 0 and n != " " and n != "\n":
                if n == "A":
                    diM[0] += 1
                    if prev == "A":
                        minus[0][0] += 1
                    elif prev == "C":
                        minus[1][0] += 1
                    elif prev == "G":
                        minus[2][0] += 1
                    elif prev == "T":
                        minus[3][0] += 1
                elif n == "C":
                    diM[1] += 1
                    if prev == "A":
                        minus[0][1] += 1
                    elif prev == "C":
                        minus[1][1] += 1
                    elif prev == "G":
                        minus[2][1] += 1
                    elif prev == "T":
                        minus[3][1] += 1
                elif n == "G":
                    diM[2] += 1
                    if prev == "A":
                        minus[0][2] += 1
                    elif prev == "C":
                        minus[1][2] += 1
                    elif prev == "G":
                        minus[2][2] += 1
                    elif prev == "T":
                        minus[3][2] += 1
                elif n == "T":
                    diM[3] += 1
                    if prev == "A":
                        minus[0][3] += 1
                    elif prev == "C":
                        minus[1][3] += 1
                    elif prev == "G":
                        minus[2][3] += 1
                    elif prev == "T":
                        minus[3][3] += 1
                prev = n
                n = f.read(1)
                if n == " " or n == "\n":
                    n = f.read(1)

print("Number of CpG Islands: " + str(numIslands))                
print("nII: " + str(nII))
print("nOO: " + str(nOO))
print("nIO: " + str(nIO))
print("nOI: " + str(nOI))
print("T[I,I]: " + str(nII/(nII+nIO)))
print("T[O,O]: " + str(nOO/(nOO+nOI)))
print("T[I,O]: " + str(nIO/(nIO+nII)))
print("T[O,I]: " + str(nOI/(nOI+nOO)))
print("T[I,O]/16: " + str(nIO/(nIO+nII)/16))
print("T[O,I]/16: " + str(nOI/(nOI+nOO)/16))
print("T matrix, Note that rows are first state, columns are second state")
print("\tA+\t\t\tC+\t\t\tG+\t\t\tT+")
print("A+\t" + str(plus[0][0]/diP[0]) + "\t" + str(plus[0][1]/diP[0]) + "\t" + str(plus[0][2]/diP[0]) + "\t" + str(plus[0][3]/diP[0]))
print("C+\t" + str(plus[1][0]/diP[1]) + "\t" + str(plus[1][1]/diP[1]) + "\t" + str(plus[1][2]/diP[1]) + "\t" + str(plus[1][3]/diP[1]))
print("G+\t" + str(plus[2][0]/diP[2]) + "\t" + str(plus[2][1]/diP[2]) + "\t" + str(plus[2][2]/diP[2]) + "\t" + str(plus[2][3]/diP[2]))
print("T+\t" + str(plus[3][0]/diP[3]) + "\t" + str(plus[3][1]/diP[3]) + "\t" + str(plus[3][2]/diP[3]) + "\t" + str(plus[3][3]/diP[3]))

print("\tA-\t\t\tC-\t\t\tG-\t\t\tT-")
print("A-\t" + str(minus[0][0]/diM[0]) + "\t" + str(minus[0][1]/diM[0]) + "\t" + str(minus[0][2]/diM[0]) + "\t" + str(minus[0][3]/diM[0]))
print("C-\t" + str(minus[1][0]/diM[1]) + "\t" + str(minus[1][1]/diM[1]) + "\t" + str(minus[1][2]/diM[1]) + "\t" + str(minus[1][3]/diM[1]))
print("G-\t" + str(minus[2][0]/diM[2]) + "\t" + str(minus[2][1]/diM[2]) + "\t" + str(minus[2][2]/diM[2]) + "\t" + str(minus[2][3]/diM[2]))
print("T-\t" + str(minus[3][0]/diM[3]) + "\t" + str(minus[3][1]/diM[3]) + "\t" + str(minus[3][2]/diM[3]) + "\t" + str(minus[3][3]/diM[3]))

with open("Q5_T.txt", "w") as t:
    for i in range(4):
        for j in range(4):
            t.write(str(plus[i][j]/diP[i]) + "\t")
        for j in range(4):
            t.write(str(nIO/(nIO+nII)/16) + "\t")
        t.write("\n")
    for i in range(4):
        for j in range(4):
            t.write(str(nOI/(nOI+nOO)/16) + "\t")
        for j in range(4):
            t.write(str(minus[i][j]/diM[i]) + "\t")
        t.write("\n")
        
