# Megan Chu
# PID: A12814536
# Assignment 2
# 4/25/18

import sys
from random import *
import matplotlib.pyplot as plt
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
if count < 2:
    print("Error in arguments, please follow the following format:")
    print("python randomDNA.py <number of seq> <size of seq>")
    exit()

print("Running Q2(randomDNA)...")

num_seq = int(sys.argv[1])
size_seq = int(sys.argv[2])

a = 0
c = 0
g = 0
t = 0
total = 0
with open("Q2randomSeq.txt", "w") as rs:
    for x in range(num_seq):
        seq = ""
        for y in range(size_seq):
            p = randint(1,100) # includes 1 and 100
            if p >= 1 and p <= 25:
                seq += "A"
                a += 1
            elif p > 25 and p <= 50:
                seq += "C"
                c += 1
            elif p > 50 and p <= 75:
                seq += "G"
                g += 1
            elif p > 75 and p <= 100:
                seq += "T"
                t += 1
            total += 1
        print(seq)
        rs.write(seq + "\n")
    print("Frequency A: " + str(round(a/total, 3)))
    print("Frequency C: " + str(round(c/total, 3)))
    print("Frequency G: " + str(round(g/total, 3)))
    print("Frequency T: " + str(round(t/total, 3)))
    rs.write("Frequency A: " + str(round(a/total, 3)) + "\n")
    rs.write("Frequency C: " + str(round(c/total, 3)) + "\n")
    rs.write("Frequency G: " + str(round(g/total, 3)) + "\n")
    rs.write("Frequency T: " + str(round(t/total, 3)) + "\n")


with open("lengthsP1.txt", "w") as lp1:
    lp1.write("lengths\n")
    with open("Q2randomSeq.txt", "r") as rs:
       rand = rs.readline()
       while len(rand) > 0 and rand[0] != "F" and rand != "\n" and rand != " ":
            # change depending on P1 or P2
            m = 1
            s = -30
            d = 0
            
            seq1 = rand[0:len(rand) - 1]
            rand = rs.readline()
            seq2 = rand[0:len(rand) - 1]
            rand = rs.readline()
            
            #set up matrix with seq1 as rows and seq2 as columns
            l = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

            # 0 for start, 1 for diagonal, 2 for left, 3 for up
            bt = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

            for i in range(1, len(seq1) + 1):
                for j in range(1, len(seq2) + 1):
                    if seq1[i - 1] == seq2[j - 1]:
                        l[i][j] = max(0, int(l[i-1][j-1]) + m, int(l[i][j-1]) + d, int(l[i-1][j]) + d)
                    else:
                        l[i][j] = max(0, l[i-1][j-1] + s, l[i][j-1] + d, l[i-1][j] + d)
                    # using elif statements lets us get shorter alignment with same score
                    if l[i][j] == 0:
                        bt[i][j] = 0
                    elif l[i][j] == l[i-1][j-1] + m or l[i][j] == l[i-1][j-1] + s:
                        bt[i][j] = 1
                    elif l[i][j] == l[i][j-1] + d:
                        bt[i][j] = 2
                    elif l[i][j] == l[i-1][j] + d:
                        bt[i][j] = 3

            maxVal = 0
            x = 0
            y = 0
            for i in range(len(seq1) + 1):
                for j in range(len(seq2) + 1):
                    if l[i][j] > maxVal:
                        maxVal = l[i][j]
                        x = i
                        y = j
            btPointer = bt[x][y]
            align1 = ""
            align2 = ""
            while btPointer != 0:
                if btPointer == 1:
                    x = x-1
                    y = y-1
                    align1 = seq1[x] + align1
                    align2 = seq2[y] + align2
                elif btPointer == 2:
                    y = y-1
                    align1 = "-" + align1
                    align2 = seq2[y] + align2
                elif btPointer == 3:
                    x = x-1
                    align1 = seq1[x] + align1
                    align2 = "-" + align2
                btPointer = bt[x][y]
            lp1.write(str(len(align1)) + "\n")


with open("lengthsP2.txt", "w") as lp2:
    lp2.write("lengths\n")
    with open("Q2randomSeq.txt", "r") as rs:
       rand = rs.readline()
       while len(rand) > 0 and rand != "\n" and rand != " ":
            # change depending on P1 or P2
            m = 1
            s = -30
            d = -20
            
            seq1 = rand[0:len(rand) - 1]
            rand = rs.readline()
            seq2 = rand[0:len(rand) - 1]
            rand = rs.readline()
            
            #set up matrix with seq1 as rows and seq2 as columns
            l = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

            # 0 for start, 1 for diagonal, 2 for left, 3 for up
            bt = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

            for i in range(1, len(seq1) + 1):
                for j in range(1, len(seq2) + 1):
                    if seq1[i - 1] == seq2[j - 1]:
                        l[i][j] = max(0, int(l[i-1][j-1]) + m, int(l[i][j-1]) + d, int(l[i-1][j]) + d)
                    else:
                        l[i][j] = max(0, l[i-1][j-1] + s, l[i][j-1] + d, l[i-1][j] + d)
                    # using elif statements lets us get shorter alignment with same score
                    if l[i][j] == 0:
                        bt[i][j] = 0
                    elif l[i][j] == l[i-1][j-1] + m or l[i][j] == l[i-1][j-1] + s:
                        bt[i][j] = 1
                    elif l[i][j] == l[i][j-1] + d:
                        bt[i][j] = 2
                    elif l[i][j] == l[i-1][j] + d:
                        bt[i][j] = 3

            maxVal = 0
            x = 0
            y = 0
            for i in range(len(seq1) + 1):
                for j in range(len(seq2) + 1):
                    if l[i][j] > maxVal:
                        maxVal = l[i][j]
                        x = i
                        y = j
            btPointer = bt[x][y]
            align1 = ""
            align2 = ""
            while btPointer != 0:
                if btPointer == 1:
                    x = x-1
                    y = y-1
                    align1 = seq1[x] + align1
                    align2 = seq2[y] + align2
                elif btPointer == 2:
                    y = y-1
                    align1 = "-" + align1
                    align2 = seq2[y] + align2
                elif btPointer == 3:
                    x = x-1
                    align1 = seq1[x] + align1
                    align2 = "-" + align2
                btPointer = bt[x][y]
            lp2.write(str(len(align1)) + "\n")


