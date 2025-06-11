from collections import *
 

# File : Hello.py

print("Hello World!")

print(7 <= 3)

print(7.5 > 3)

List = [1,2,3,"car"]

a = [List]*3
print(a)

for item in List:
    print(item)

f =1.01
print(int(f))
print(float(3))
print(str(3.5))

print(bool(0))
print(bool(1))
print(int(True))
print(int(False))

print(float(True))
print(float(False))

#int 64bit

#Data Structures

#List : ordered sequence , they are mutable, can be nested and can be accessed by index like array, supports negative indexes. Slicing is supported on index.
# can be deleted by del(), split(), append(), insert(), remove(), index(), reverse(),  etc.
# List.repl
# help(A) 




counter=0
while counter<4:
    print (List.__getitem__(counter))
    counter = counter+1


List.append(45)
List.insert(2,10)
#List.reverse()
c=List.remove(3)
print (c)
print (List.index(1).__add__(10))
del List[1]

print (List)
print((55).__add__(10))
print(list(range(1,10,3)))


#tuples  : ordered  sequence of immutable objects , can be accessed by index liek array , tuple[], it s imutable this can't be changed 
# can be nested, supports slicing, can be deleted by del(), index(), count(), etc.
mylist = [1,2,3,4,5]
mytuple = tuple(mylist) 
print(mytuple)
print(type(mytuple))
print(mytuple[1])
print(mytuple[1:3])
print(mytuple[1:])  # Slicing from index 1 to end
print(mytuple[:3])  # Slicing from start to index 3
print(mytuple[-1])  # Accessing last element
print(mytuple[-2:])  # Slicing from second last element to end
print(mytuple.count(2))  # Count occurrences of 2
print(mytuple.index(3))  # Find index of first occurrence of 3

# Strings : ordered sequence of characters, immutable, can be accessed by index like array, supports slicing, can be nested, can be deleted by del(), split(), join(), replace(), etc.


str="david"
#str[2]= "f"
print(str)
mytuple=(2,"fan",True,0.5,8)
print(mytuple[1])
myset = {3,2,5.4,8,10}
yset = {"true",2,6,7,3,8}
print(myset.difference(yset))


#Dictionaries : are like map , keys are unique and immutable, values can be mutable or immutable, they are unordered,
#  can be accessed by key, 
# supports slicing, 
# can be nested, 
# can be deleted by del(), pop(), clear(), etc.

firstdictionary = {"a":12321,"b":234535,"c":4379}

print (firstdictionary.get("c"))
print(list(firstdictionary.values()))
str = ["i", "love","india"]
counter = 0 ;
firstdictionary["d"] = 1234
print(firstdictionary)
print(firstdictionary.keys())
print(firstdictionary.items())
print(firstdictionary.pop("b"))

firstdictionary.update({"e": 9999, "f": 8888})
firstdictionary.get
mylist = [x*x for x in range(1,10)]
print (mylist)

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

diction = {}
diction["a"] = 1
diction["b"] = 2
diction["c"] = 3
print (diction)

print (diction["a"])
#print (diction["d"])
print (diction.get("e") is not None) # python has None object and compares it with NoneType
print (diction.get("e", "Not Found")) # returns default value if key not found
print (diction.get("e", [1,2])) # returns value if key found
print (diction)



#Sets : isert different value, unordered , mutable
# can be accessed by index, supports slicing, can be nested, can be deleted by del(), pop(), clear(), etc.
# no duplicate elements

l1 = [1,9,3,4,6,6,7,4,9];
myset = set(l1)

print(myset) 
print(type(myset))
print(len(myset))
print(myset.pop())
print(myset)
myset.add(10)
print(myset.__contains__(10))
myset.remove(10)
print(myset)

set2 = {3,6,1,8,}
set3 = myset & set2
print(set3)  # Intersection
set4 = myset | set2
print(set4)  # Union
set5 = myset - set2
print(set5)  # Difference
set6 = myset ^ set2
print(set6)  # Symmetric Difference (set union - the intersection)
set7 = myset.copy()
print(set7)  # Copy of the set
set8 = frozenset(myset)  # Immutable set
print(set8)  # Frozen set (immutable)