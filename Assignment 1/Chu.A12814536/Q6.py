# Megan Chu
# PID: A12814536
# Assignment 1
# 4/10/18

print("Running Q6(getSeq) with data.seq and data.in...")
with open("data.seq", "r") as ds:
    with open("data.in", "r") as di:
        print("Getting contents of Q6query.txt...")
        with open("Q6query.txt", "r") as q:
            query = q.readline()
            if query[len(query) - 1:len(query)] == "\n":
                query = query[0:len(query) - 1]
            print("Query is: " + query)
            seq = di.readline()
            while len(seq) > 0:
                seq = seq[0:len(seq) - 1] # remove new line character
                pair = seq.split(" ")
                count = int(pair[1])
                ds.seek(count)
                ln = ds.read(len(query))
                while ln.lower() != query.lower() and ln[len(query) - 1:len(query)] != "@":
                    count += 1
                    ds.seek(count)
                    ln = ds.read(len(query))
                if ln.lower() == query.lower():
                    print("gi # of database sequence containing query is: " + pair[0])
                    break
                seq = di.readline()
            
