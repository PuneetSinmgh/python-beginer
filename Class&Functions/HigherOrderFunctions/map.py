# map functions are used to apply a function to all items in an iterable (like a list) and return a new iterable with the results.
# This is useful for transforming data without using explicit loops.
# Example of using map to square each element in a list
# Map returns an iterable without chnaginf the number length of the list.
# It applies the function to each element in the iterable.

car = ['san', 'fan','Pan','tan']
print(sorted( car))
print (list( map( lambda s: s.upper(), car) )) 

#list comprehension is a concise way to create lists in Python.
# It can be used to apply a function to each element in an iterable, similar to map.
print( [ s.upper() for s in car])

# Example of using map to convert list into a dictionary key mapped to their frequency
from collections import defaultdict
from collections import Counter
list1 = ['san', 'fan', 'Pan', 'tan', 'san', 'fan']
frequency_dict = dict(Counter(list1))
print(frequency_dict)

# Using map to create a dictionary with frequency counts
frequency_map = dict(map(lambda x: (x, frequency_dict[x]), frequency_dict))
print(frequency_map)

# Using defaultdict to create a frequency dictionary
frequency_defaultdict = defaultdict(int)
for item in list1:
    frequency_defaultdict[item] += 1
print(frequency_defaultdict)

# Using map to apply a function to each element in a list
squared_list = list(map(lambda x: x**2, range(10)))
print(squared_list)