#!/usr/bin/python
# -*- coding: utf-8 -*-

# UTF8 encoding: https://stackoverflow.com/a/35923227
# ---------------------------------------------------
#
#   Author: Viktor Jon Helgason vjh2@hi.is
#
#   Parses BIN KristinSnid.CSV
#   Creates TXT file for each category of words
#   
#   https://bin.arnastofnun.is/gogn/mimisbrunnur/
#   
#   Written using Python 2.7.16 @ macOS 10.15.6
#   Parsing took about 35 seconds
#   Could be improved by paralell proccessing
# ---------------------------------------------------
import time

t0 = time.time()

qbfile = open("KRISTINsnid.csv", "r")

lastWord = ""

for aline in qbfile:
    values = aline.split(";")
    currentWord = values[0]

    if(currentWord != lastWord):
        with open(values[2]+".txt","a+") as f: 
            # https://stackoverflow.com/a/15359499
            print(currentWord)
            f.write(values[0])
            f.write("\n")
    lastWord = currentWord

qbfile.close()

# Timer: https://stackoverflow.com/a/27594952
t1 = time.time()
total = t1-t0
print("Time elapsed: ")
print(total)