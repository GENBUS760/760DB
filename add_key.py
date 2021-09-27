#!/usr/bin/env python

import sys

key = sys.argv[1]
val = sys.argv[2]

f = open("db.txt", "a+")
f.write(key + "," + val + "\n")
f.close()
