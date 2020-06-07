# Megan Chu
# PID: A12814536
# Assignment 3
# 5/14/18

from statistics import mean
import sys
from random import *
import math

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
if count < 2:
    print("Error in arguments, please follow the following format:")
    print("python Q2.py <database file> <query file>")
    exit()

print("Running Q2...")

db_file = sys.argv[1]
query_file = sys.argv[2]
w = 3
allHomologs = list(list())

with open(db_file, "r") as db:
    db.readline()
    db.readline()
    start = db.tell()
    with open(query_file, "r") as q:
        qLine = q.readline()
        while(!qLine.isEmpty() and qLine != "\n" and qLine != " "):
            homologs = list()
            qLine = qLine[0:len(qLine) - 1]
            L = len(qLine)
            w = 5
            if w > L:
                break
            key = qLine[0:w]
            k = "k"
            dbIter = db.tell()
            while(!k.isEmpty()):
            dbW = ""
                while len(dbW) < len(key):
                    k = db.read(1)
                    while k == " " or k == "\n":
                        k = db.read(1)
                    dbW = dbW + k
                if dbW == key:
                    while len(dbW) < len(qLine) and !k.isEmpty():
                        k = db.read(1)
                        while k == " " or k == "\n":
                            k = db.read(1)
                        dbW = dbW + k
                    if len(dbw) < len(qLine):
                        break
                    seq1 = dbW
                    seq2 = qLine
                    m = 1
                    s = 0
                    d = 0

                    #set up matrix with seq1 as rows and seq2 as columns
                    a = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

                    # 0 for start, 1 for diagonal, 2 for left, 3 for up
                    bt = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

                    for i in range(1, len(seq1) + 1):
                        for j in range(1, len(seq2) + 1):
                            if seq1[i - 1] == seq2[j - 1]:
                                a[i][j] = max(0, int(a[i-1][j-1]) + m, int(a[i][j-1]) + d, int(a[i-1][j]) + d)
                            else:
                                a[i][j] = max(0, a[i-1][j-1] + s, a[i][j-1] + d, a[i-1][j] + d)
                            # using elif statements lets us get shorter alignment with same score
                            if a[i][j] == 0:
                                bt[i][j] = 0
                            elif a[i][j] == a[i-1][j-1] + m or a[i][j] == a[i-1][j-1] + s:
                                bt[i][j] = 1
                            elif a[i][j] == a[i][j-1] + d:
                                bt[i][j] = 2
                            elif a[i][j] == a[i-1][j] + d:
                                bt[i][j] = 3

                    maxVal = 0
                    x = 0
                    y = 0
                    for i in range(len(seq1) + 1):
                        for j in range(len(seq2) + 1):
                            if a[i][j] > maxVal:
                                maxVal = a[i][j]
                                x = i
                                y = j
                    if maxVal/len(qLine) >= .85:
                        homologs.append(dbW)
                else:
                    dbIter += 1
            qLine = q.readline()
            allHomologs.append(homologs)
                                
                          
                           
       
       
