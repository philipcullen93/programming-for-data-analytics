# Author: Philip Cullen

import csv

FILENAME = "data.csv"
DATADIR = "/workspaces/programming-for-data-analytics/my-work/"

'''
# part 2
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line)
'''

'''
# part 3
# Modification for separate header line
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount:
            print(f"{line}\n-------------")
        else:
            print(line)
        linecount += 1
'''

'''
# part 4a
# Convert the string that is read into an integer
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if linecount:
            total += int(line[1])

        linecount += 1
    print(f"average is {total/(linecount-1)}")
'''


# part 4b
# 
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: 
            pass
        else: 
            total += line[1] # why 1

        linecount += 1
    print (f"average is {total/(linecount-1)}")
