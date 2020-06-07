# Megan Chu
# PID: A12814536
# Assignment 3
# 5/14/18

from statistics import mean
import sys
from random import *
import math
from typing import Tuple

print("Running Q5...")

db_file = sys.argv[1]
query_file = sys.argv[2]
db_start = int(sys.argv[3])
nodes = list()
class TrieNode(object):
    def __init__(self, char: str, label: int, ind: int):
        self.char = char
        self.children = []
        self.finished = False
        self.counter = 1
        self.label = label
        self.index = ind
def add(root, word: str, label: int):
    node = root
    for char in word:
        isChild = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                isChild = True
                break
        if not isChild:
            newNode = TrieNode(char,0,len(nodes))
            nodes.append(newNode)
            node.children.append(newNode)
            node = newNode
    node.finished = True
    node.label = label
def findPrefix(root, prefix: str) -> int:
    node = root
    if not root.children:
        return 0
    notFound = True
    for child in node.children:
        if child.char == prefix:
            notFound = False
            node = child
            break
    if notFound:
        return 0
    return node.index


root = TrieNode(" ",0,0)
nodes.append(root)
queries = list()
with open(query_file, "r", encoding='utf-8-sig') as q:
    qLine = q.readline()
    y = 1
    while(len(qLine) > 0):
        if qLine[len(qLine) - 1] == "\n":
            qLine = qLine[0:len(qLine) - 1]
        add(root, qLine, y)
        queries.append(qLine)
        qLine = q.readline()
        y += 1

hits = [0]*len(queries)
total = 0
with open(db_file, "r") as db:
    db.readline()
    start = db.tell()
    itr = db.tell()
    while (itr - start + 1) < db_start:
        let = db.read(1)
        if let != "\n" and let != " " and len(let) > 0:
            itr += 1
    L = db_start
    c = L
    v = root
    db_start = db.tell()
    dbs = 0
    next = db.read(1)
    while len(next) > 0:
        if next == "\n" or next == " ":
            dbs = db.tell()
            next = db.read(1)
        x = findPrefix(v, next)
        if x != 0:
            v = nodes[x]
            c += 1
            if v.finished:
                print("Pattern " + str(v.label) + " matches starting at position " + str(L))
                hits[v.label - 1] += 1
                total += 1
        else:
            db_start += 1
            if db_start == dbs - 1:
                db_start += 1
                c = L
                L = c
            else:
                c = L + 1
                L = c
            db.seek(db_start)
            v = root
        next = db.read(1)

with open("Q5matches2.txt", "w") as w:
    w.write("Total # Matches: " + str(total) + "\n")
    w.write("Keyword\t# Matches\n")
    for i in range(0,len(queries)-1):
        w.write(queries[i] + "\t" + str(hits[i]) + "\n")
    w.write(queries[len(queries)-1] + "\t" + str(hits[len(queries)-1]))
    

            













     
       
       
