# Megan Chu
# PID: A12814536
# Assignment 2
# 4/25/18

import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
if count < 7:
    print("Error in arguments, please follow the following format:")
    print("python locAL.py <seq_file> -m <match> -s <mismatch> -d <indel> -a")
    exit()

print("Running Q1(locAL)...")

seq_file = sys.argv[1]
x = 2
alignment = 0
while x <= count:
    if sys.argv[x] == "-m":
        m = int(sys.argv[x+1])
        x += 2
    elif sys.argv[x] == "-s":
        s = int(sys.argv[x+1])
        x += 2
    elif sys.argv[x] == "-d":
        d = int(sys.argv[x+1])
        x += 2
    elif sys.argv[x] == "-a":
        alignment = 1
        x += 1

seq1 = ""
seq2 = ""
with open(seq_file, "r") as sf:
    sf.seek(0)
    ln = sf.read(1)
    if ln != ">":
        while ln != ">":
            ln = sf.read(1)
    ln = sf.readline()
    ln = sf.read(1)
    while ln != ">":
        if ln != "\n" and ln != " " and len(ln) > 0:
            seq1 += ln
        ln = sf.read(1)
    ln = sf.readline()
    ln = sf.read(1)
    while len(ln) > 0:
        if ln != "\n" and ln != " " and len(ln) > 0:
            seq2 += ln
        ln = sf.read(1)

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
print("Score of the best local-alignment: " + str(maxVal))

end1 = x
end2 = y
start1 = 0
start2 = 0

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
    start1 = x
    start2 = y
print("*Note there may be many local-alignments with the best score, this code only outputs one of the local-alignments with the best score.*")
print("Length of one best local-alignment: " + str(len(align1)))

if alignment == 1:
    print("Actual local-alignment: ")
    # number of bases clipped from beginning and end, respectively, of sequence 1
    print(str(start1) + " " + str(len(seq1) - end1))
    print(align1)
    print(align2)
    # number of bases clipped from beginning and end, respectively, of sequence 2
    print(str(start2)+ " " + str(len(seq2) - end2))
