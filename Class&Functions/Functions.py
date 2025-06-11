
import random
from random import Random
import random

def stringfunction (strlen):
    alphabetstring = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabetstring[random.randrange(27)]

    return res



def comparefunction (goal, teststring):
    numsame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numsame = numsame + 1

    return numsame/len(goal)

print(comparefunction("methinks it is like a weasel",stringfunction(28)))

def main():
    goalstring = "methinks it is like a weasel"
    newstring = stringfunction(28)
    newscore = comparefunction(goalstring,stringfunction(28))
    best=0
    while newscore < 1:
        if newscore>best:
            print(newscore , newstring)
            best=newscore

        newstring=stringfunction(28)
        newscore = comparefunction(goalstring,newstring)

main()


# sorting a list b 
unSorted = [1,5,3,6,7,3,5,2,8,95,7,7,98]
print( sorted (unSorted))

unSorted = [1,5,3,6,7,3,5,2,8,95,7,7,98]
unSorted.sort()
print( unSorted)

# run a function to count the number of words in a string
string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
def numOfWords( string ):
    count=0
    for s in string.split():
        count+=1
    return count
print(numOfWords(string))

# count the number of words in a string and return a dictionary with the word as key and its count as value
def countOfEachWords( string ):
    dictionary = {}
    words = string.split()
    print(words)
    for s in words:
        dictionary[s] = dictionary.get(s,0)+1 
    return dictionary
print(countOfEachWords(string))

