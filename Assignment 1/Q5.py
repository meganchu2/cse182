# Megan Chu
# PID: A12814536
# Assignment 1
# 4/10/18

print("Running Q5...", end = "\n\n")
print("Creating data.seq...")
with open("database.txt", "r") as db:
    with open("data.seq", "w") as ds:
        ln = db.readline();
        while len(ln) > 0:
            if ln[0:1] == ">":
                ln = db.readline()
                ds.write(ln[0:len(ln) - 1])
            while ln[0:1] != ">" and len(ln) > 0:
                ln = db.readline()
                if ln[0:1] == ">":
                    ds.write("@")
                elif len(ln) > 0:                        
                    ds.write(ln[0:len(ln) - 1])

with open("data.seq", "r") as ds:
      print("Contents of data.seq: ")
      print(ds.read(), end = "\n\n")

print("Creating data.in...")
with open("database.txt", "r") as db:
    with open("data.in", "w") as di:
        ln = db.read(1)
        count = 0
        while len(ln) > 0:
            if ln == ">":
                ln = db.read(3) # read to end of gi|
                ln = db.read(1)
                while ln != "|":
                    di.write(ln)
                    ln = db.read(1)
                di.write(" " + str(count) + "\n")
                ln = db.readline() # read to end of header line
                ln = db.read(1)
            while ln != ">" and len(ln) > 0:
                if ln != "\n" and ln != " ":
                    count += 1
                ln = db.read(1)
            count += 1 # account for @ between strings

with open("data.in", "r") as di:
      print("Contents of data.in: ")
      print(di.read())
