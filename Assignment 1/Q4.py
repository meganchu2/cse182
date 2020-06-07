# Megan Chu
# PID: A12814536
# Assignment 1
# 4/10/18

print("Running Q4(filter)...")
print("Creating filteredDatabase.txt with mouse and rat sequences...")
with open("database.txt", "r") as db:
    with open("filteredDatabase.txt", "w") as f:
        ln = db.readline();
        while len(ln) > 0:
            count = 0
            if ln[0:1] == ">":
                tog = 1
                i = 0
                while i <= (len(ln) - 3):
                    if ln[i:i+3].lower() == "rat" or ln[i:i+3].lower() == "mus":
                        tog = 0
                    i += 1
                if(tog == 0): # this is mouse or rat sequence
                    f.write(ln) # contains new line                
                    ln = db.read(1)
                    count = 0 # start ofsequence
                    while ln != ">" and len(ln) > 0:
                        if ln != "\n" and ln != " ":
                            f.write(ln)
                            count+= 1
                            if count == 60:
                                count=0
                                f.write("\n")
                        ln = db.read(1)
                    if count != 0 and len(ln) > 0:
                        f.write("\n")
                    db.seek(db.tell() - 1)
                    ln = db.readline()
                else:
                    ln = db.readline()
                    while ln[0:1] != ">" and len(ln) > 0:
                        ln = db.readline()

with open("filteredDatabase.txt", "r") as f:
    print("Contents of filteredDatabase: ")
    print(f.read())
