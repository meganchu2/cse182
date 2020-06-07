# Megan Chu
# PID: A12814546
# Assignment 4
# 5/27/18

import sys
from random import *

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
if count < 1:
    print("Error in arguments, please follow the following format:")
    print("python Q1.py <fasta_file>")
    exit()

print("Running Q1(dinucelotide frequency)...")

fasta_file = sys.argv[1]

AA = 0
AC = 0
AG = 0
AT = 0
CA = 0
CC = 0
CG = 0
CT = 0
GA = 0
GC = 0
GG = 0
GT = 0
TA = 0
TC = 0
TG = 0
TT = 0
tD = 0
A = 0
C = 0
G = 0
T = 0
with open(fasta_file, "r") as f:
    f.readline()
    nuc = f.read(1)
    dN = ""
    if nuc == " " or nuc == "\n":
        nuc = f.read(1)
    dN += nuc
    nuc = f.read(1)
    if nuc == " " or nuc == "\n":
        nuc = f.read(1)
    dN += nuc
    while len(dN) == 2:
        if dN[0] == "A":
            A += 1
            if dN[1] == "A":
                AA += 1
            elif dN[1] == "C":
                AC += 1
            elif dN[1] == "G":
                AG += 1
            elif dN[1] == "T":
                AT += 1
        elif dN[0] == "C":
            C += 1
            if dN[1] == "A":
                CA += 1
            elif dN[1] == "C":
                CC += 1
            elif dN[1] == "G":
                CG += 1
            elif dN[1] == "T":
                CT += 1
        elif dN[0] == "G":
            G += 1
            if dN[1] == "A":
                GA += 1
            elif dN[1] == "C":
                GC += 1
            elif dN[1] == "G":
                GG += 1
            elif dN[1] == "T":
                GT += 1
        elif dN[0] == "T":
            T += 1
            if dN[1] == "A":
                TA += 1
            elif dN[1] == "C":
                TC += 1
            elif dN[1] == "G":
                TG += 1
            elif dN[1] == "T":
                TT += 1
        tD += 1
        dN = ""
        f.seek(f.tell() - 1)
        nuc = f.read(1)
        if nuc == " " or nuc == "\n":
            nuc = f.read(1)
        dN += nuc
        nuc = f.read(1)
        if nuc == " " or nuc == "\n":
            nuc = f.read(1)
        dN += nuc
        if len(dN) == 1:
            if dN == "A":
                A += 1
            elif dN == "C":
                C += 1
            elif dN == "G":
                G += 1
            elif dN == "T":
                T += 1

tB = A+C+G+T
oA = A/tB
oC = C/tB
oG = G/tB
oT = T/tB
eAA = A/tB*(A-1)/tB
eAC = A/tB*C/tB
eAG = A/tB*G/tB
eAT = A/tB*T/tB
eCA = C/tB*A/tB
eCC = C/tB*(C-1)/tB
eCG = C/tB*G/tB
eCT = C/tB*T/tB
eGA = G/tB*A/tB
eGC = G/tB*C/tB
eGG = G/tB*(G-1)/tB
eGT = G/tB*T/tB
eTA = T/tB*A/tB
eTC = T/tB*C/tB
eTG = T/tB*G/tB
eTT = G/tB*T/tB
print("Total length of sequence: ")
print("\t" + str(tB))
print("Observed frequency of each base: ")
print("\tA\tC\tG\tT")
print("\t" + str(round(oA,4)) + "\t" + str(round(oC,4)) + "\t" + str(round(oG,4)) + "\t" + str(round(oT,4)))
print("Calculated Expected Frequency of each dinucleotide: ")
print("\tNote that rows represent 1st base and columns represent 2nd base")
print("\t\tA\tC\tG\tT")
print("\tA\t" + str(round(eAA,4)) + "\t" + str(round(eAC,4)) + "\t" + str(round(eAG,4)) + "\t" + str(round(eAT,4)))
print("\tC\t" + str(round(eCA,4)) + "\t" + str(round(eCC,4)) + "\t" + str(round(eCG,4)) + "\t" + str(round(eCT,4)))
print("\tG\t" + str(round(eGA,4)) + "\t" + str(round(eGC,4)) + "\t" + str(round(eGG,4)) + "\t" + str(round(eGT,4)))
print("\tT\t" + str(round(eTA,4)) + "\t" + str(round(eTC,4)) + "\t" + str(round(eTG,4)) + "\t" + str(round(eTT,4)))

print("Observed Frequency of each dinucleotide: ")
print("\tNote that rows represent 1st base and columns represent 2nd base")
print("\t\tA\tC\tG\tT")
print("\tA\t" + str(round(AA/tD,4)) + "\t" + str(round(AC/tD,4)) + "\t" + str(round(AG/tD,4)) + "\t" + str(round(AT/tD,4)))
print("\tC\t" + str(round(CA/tD,4)) + "\t" + str(round(CC/tD,4)) + "\t" + str(round(CG/tD,4)) + "\t" + str(round(CT/tD,4)))
print("\tG\t" + str(round(GA/tD,4)) + "\t" + str(round(GC/tD,4)) + "\t" + str(round(GG/tD,4)) + "\t" + str(round(GT/tD,4)))
print("\tT\t" + str(round(TA/tD,4)) + "\t" + str(round(TC/tD,4)) + "\t" + str(round(TG/tD,4)) + "\t" + str(round(TT/tD,4)))

print("Observed/Expected frequencies for dinucleotides: ")
print("\tNote that rows represent 1st base and columns represent 2nd base")
print("\t\tA\tC\tG\tT")
print("\tA\t" + str(round(AA/tD/eAA,4)) + "\t" + str(round(AC/tD/eAC,4)) + "\t" + str(round(AG/tD/eAG,4)) + "\t" + str(round(AT/tD/eAT,4)))
print("\tC\t" + str(round(CA/tD/eCA,4)) + "\t" + str(round(CC/tD/eCC,4)) + "\t" + str(round(CG/tD/eCG,4)) + "\t" + str(round(CT/tD/eCT,4)))
print("\tG\t" + str(round(GA/tD/eGA,4)) + "\t" + str(round(GC/tD/eGC,4)) + "\t" + str(round(GG/tD/eGG,4)) + "\t" + str(round(GT/tD/eGT,4)))
print("\tT\t" + str(round(TA/tD/eTA,4)) + "\t" + str(round(TC/tD/eTC,4)) + "\t" + str(round(TG/tD/eTG,4)) + "\t" + str(round(TT/tD/eTT,4)))

    
