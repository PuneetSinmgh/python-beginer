from collections import Counter
import sys

def moeyEarned():
    # read number of shoes
    numOfShoes = int(input())
    # read shoe sizes
    shoeSizes = Counter([int(s) for s in input().split(" ")])
    
    # read number of customers
    numofCustomers = int(input())
    
    res = 0 
    for _ in range(numofCustomers):
        tup = tuple([int(s) for s in input().split(" ")])
        if tup[0] in shoeSizes:
            if shoeSizes[tup[0]] > 0:
                res += tup[1]
                shoeSizes[tup[0]] -= 1
    
    print(res)


def money():

    listinput = []
    for line in sys.stdin:
        # read line and remove spaces
        line = line.rstrip()
        listinput.append(line)

    numOfShoes = int(listinput[0])
    shoeSizes = Counter([int(s) for s in listinput[1].split(" ")])

    numofCustomers = int(listinput[2])

    res =0 
    for t in listinput[3 : len(listinput)]:
        tup = tuple([int(s) for s in t.split(" ")])
        if tup[0] in shoeSizes:
            if shoeSizes[tup[0]]>0:
                res += tup[1]
                shoeSizes[tup[0]] -= 1

    return res