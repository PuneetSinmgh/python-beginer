# File : Hello.py

print "Hello World!"
print(7 <= 3)
print(7.5 > 3)

List = [1,2,3,"car"]
a = [List]*3
print a
for item in List:
    print item

counter=0
while counter<4:
    print List.__getitem__(counter)
    counter = counter+1


List.append(45)
List.insert(2,10)
#List.reverse()
c=List.remove(3)
print c
print List.index(1).__add__(10)
print List
print((55).__add__(10))
print(list(range(1,10,3)))
str="david"
#str[2]= "f"
print(str)
mytuple=(2,"fan",True,0.5,8)
print(mytuple[1])
myset = {3,2,5.4,8,10}
yset = {"true",2,6,7,3,8}
print(myset.difference(yset))
firstdictionary = {"a":12321,"b":234535,"c":4379}
print (firstdictionary.get("c"))
print(list(firstdictionary.values()))
str = ["i", "love","india"]
counter = 0 ;
mylist = [x*x for x in range(1,10)]
print mylist


def letterappend():
    wordlist = ['cat', 'dog', 'rabbit']
    letterlist = []
    for aword in wordlist:
        for aletter in aword:
            if letterlist.__contains__(aletter):
                continue
            else:
                letterlist.append(aletter)
    print(letterlist)
    return


