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
    print("python Q3.py <fasta_file>")
    exit()

print("Running Q5(identify CpG Islands with estimated parameters)...")

fasta_file = sys.argv[1]
P = list()
bT = list()
for i in range(8):
    P.append(list())
    bT.append(list())
    P[i].append(-math.inf)
    bT[i].append(-1)
# 0 A+, 1 C+, 2 G+, 3 T+, 4 A-, 5 C-, 6 G-, 7 T-


T = list()
with open("Q5_T.txt", "r") as t:
    tr = t.readline().split("\t")
    for i in range(8):
        T.append(list())
        for j in range(8):
            T[i].append(math.log(float(tr[j])))
        tr = t.readline()
        tr = tr.split("\t")

c = 1
prevNuc = -1
with open(fasta_file, "r") as f:
    f.readline() 
    n = f.read(1)
    if n == " " or n == "\n":
        n = f.read(1)
    if n == "A":
        P[4][0] = 0
        prevNuc = 0
    elif n == "C":
        P[5][0] = 0
        prevNuc = 1
    elif n == "G":
        P[6][0]= 0
        prevNuc = 2
    elif n == "T":
        P[7][0]= 0
        prevNuc = 3
    c = 1
    n = f.read(1)
    if n == " " or n == "\n":
        n = f.read(1)

    while len(n) > 0:
        for i in range(8):
            P[i].append(-math.inf)
            bT[i].append(-1)
        if n == "A":
            if P[prevNuc][c-1]+T[prevNuc][0] > P[0][c]: # ++
                P[0][c] = P[prevNuc][c-1]+T[prevNuc][0]
                bT[0][c] = prevNuc                
            if P[prevNuc + 4][c-1]+T[prevNuc+4][4] > P[4][c]: # --
                P[4][c] = P[prevNuc + 4][c-1]+T[prevNuc+4][4]
                bT[4][c] = prevNuc + 4
            if P[prevNuc][c-1]+T[prevNuc][4] > P[4][c]: # +-
                P[4][c] = P[prevNuc][c-1]+T[prevNuc][4]
                bT[4][c] = prevNuc
            if P[prevNuc + 4][c-1]+T[prevNuc+4][0] > P[0][c]: # -+
                P[0][c] = P[prevNuc + 4][c-1]+T[prevNuc+4][0]
                bT[0][c] = prevNuc + 4
            prevNuc = 0
        elif n == "C":
            if P[prevNuc][c-1]+T[prevNuc][1] > P[1][c]: # ++
                P[1][c] = P[prevNuc][c-1]+T[prevNuc][1]
                bT[1][c] = prevNuc
            if P[prevNuc + 4][c-1]+T[prevNuc+4][5] > P[5][c]: # --
                P[5][c] = P[prevNuc + 4][c-1]+T[prevNuc+4][5]
                bT[5][c] = prevNuc + 4
            if P[prevNuc][c-1]+T[prevNuc][5] > P[5][c]: # +-
                P[5][c] = P[prevNuc][c-1]+T[prevNuc][5]
                bT[5][c] = prevNuc
            if P[prevNuc + 4][c-1]+T[prevNuc+4][1] > P[1][c]: # -+
                P[1][c] = P[prevNuc + 4][c-1]+T[prevNuc+4][1]
                bT[1][c] = prevNuc + 4
            prevNuc = 1
        elif n == "G":
            if P[prevNuc][c-1]+T[prevNuc][2] > P[2][c]: # ++
                P[2][c] = P[prevNuc][c-1]+T[prevNuc][2]
                bT[2][c] = prevNuc
            if P[prevNuc + 4][c-1]+T[prevNuc+4][6] > P[6][c]: # --
                P[6][c] = P[prevNuc + 4][c-1]+T[prevNuc+4][6]
                bT[6][c] = prevNuc + 4
            if P[prevNuc][c-1]+T[prevNuc][6] > P[6][c]: # +-
                P[6][c] = P[prevNuc][c-1]+T[prevNuc][6]
                bT[6][c] = prevNuc
            if P[prevNuc + 4][c-1]+T[prevNuc+4][2] > P[2][c]: # -+
                P[2][c] = P[prevNuc + 4][c-1]+T[prevNuc+4][2]
                bT[2][c] = prevNuc + 4
            prevNuc = 2
        elif n == "T":
            if P[prevNuc][c-1]+T[prevNuc][3] > P[3][c]: # ++
                P[3][c] = P[prevNuc][c-1]+T[prevNuc][3]
                bT[3][c] = prevNuc
            if P[prevNuc + 4][c-1]+T[prevNuc+4][7] > P[7][c]: # --
                P[7][c] = P[prevNuc + 4][c-1]+T[prevNuc+4][7]
                bT[7][c] = prevNuc + 4
            if P[prevNuc][c-1]+T[prevNuc][7] > P[7][c]: # +-
                P[7][c] = P[prevNuc][c-1]+T[prevNuc][7]
                bT[7][c] = prevNuc
            if P[prevNuc + 4][c-1]+T[prevNuc+4][3] > P[3][c]: # -+
                P[3][c] = P[prevNuc + 4][c-1]+T[prevNuc+4][3]
                bT[3][c] = prevNuc + 4
            prevNuc = 3
        n = f.read(1)
        if n == " " or n == "\n":
            n = f.read(1)
        c += 1

c -= 1
start = list()
end = list()
max = -1
prev = -1
curr = -1
for i in range(8):
    if P[i][c] > max:
        P[i][c] = max
        prev = bT[i][c]
        curr = i
if curr in [0,1,2,3]:
    end.insert(0, c+1)
    print(c+1, end = " ")
while c >= 0:
    if curr in [0,1,2,3] and prev in [4,5,6,7]: # -+
        start.insert(0, c+1)
    if curr in [4,5,6,7] and prev in [0,1,2,3]: # +-
        end.insert(0, c)
    curr = prev
    prev = bT[curr][c]
    c -= 1

with open("Q5_CpG.txt", "w") as out:
    if len(start) != len(end):
        print("Error: Size Mismatch")
    for i in range(len(start)):
        out.write(str(start[i]) + " " + str(end[i]) + "\n")
        print(str(start[i]) + " " + str(end[i]))
    print("Number of CpG Islands Identified: " + str(len(start)))

numS = 0
numD3 = 0
numD5 = 0
with open("Q3_CpG.txt", "r") as one:
    with open("Q5_CpG.txt", "r") as two:
        bPrev = one.tell()
        aPrev = two.tell()
        b = one.readline()
        a = two.readline()
        while len(b) > 0 and len(a) > 0:
            b = b[0:len(b) - 1]
            a = a[0:len(a) - 1]
            b = b.split(" ")
            a = a.split(" ")
            if int(b[0]) >= int(a[0]) and int(b[0]) <= int(a[1]):
                numS += 1
            elif int(a[0]) >= int(b[0]) and int(a[0]) <= int(b[1]):
                numS += 1
            elif int(b[1]) >= int(a[0]) and int(b[1]) <= int(a[1]):
                numS += 1
            elif int(a[1]) >= int(b[0]) and int(a[1]) <= int(b[1]):
                numS += 1
            elif int(b[1]) < int(a[0]):
                numD3 += 1
                two.seek(aPrev)
            elif int(a[1]) < int(b[0]):
                numD5 += 1
                one.seek(bPrev)
            bPrev = one.tell()
            aPrev = two.tell()
            b = one.readline()
            a = two.readline()
        while len(b) > 0:
            numD3 += 1
            b = one.readline()
        while len(a) > 0:
            numD5 += 1
            a = two.readline()

print("Number Shared CpG Islands: " + str(numS))
print("Number in Q3 but not Q5: " + str(numD3))
print("Number in Q5 but not Q3: " + str(numD5))
                            
