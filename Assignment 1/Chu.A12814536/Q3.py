# Megan Chu
# PID: A12814536
# Assignment 1
# 4/10/18

print("Running Q3(cat)...")
with open("database.txt", 'r') as db:
    ln = db.readline();
    while len(ln) > 0:
        count = 0
        if ln[0:1] == ">":
            print(ln, end= "") #ln already has a newline at the end
            ln = db.readline()
            count += len(ln) - 1 # minus 1 for new line character
        else:
            count += len(ln) - 1 # minus 1 for new line character
        while ln[0:1] != ">" and len(ln) > 0:
            ln = db.readline()
            if ln[0:1] != ">" and len(ln) > 0:
                count += len(ln) - 1
        print(count)
