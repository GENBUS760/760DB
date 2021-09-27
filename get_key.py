#!/usr/bin/env python

import sys

key = sys.argv[1]

f = open("db.txt", "r")

# search for key in db.txt, print val if found
for line in f:
    line_key, line_val = line.split(",")
    
    if line_key == key:
        print(line_val)
        break

f.close()
