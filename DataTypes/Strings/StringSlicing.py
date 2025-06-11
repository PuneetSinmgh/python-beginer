from collections import *

s = "Michelangelo Buonarroti"

print(s[0:5])  # Slicing from index 0 to 4
print(s[8:])   # Slicing from index 8 to the end
print(s[:5])   # Slicing from the start to index 4
print(s[-5:])  # Slicing from the last 5 characters
print(s[::2])  # Slicing with a step of 2

# len of string
print(len(s))  # Length of the string  

# reverse the string
print(s.replace)  # Using __reversed__ method

print(s[::])  # Slicing to reverse the string

#split the string with delimiter
print(s.split(" "))  # Splitting by space
print(s.split(","))  # Splitting by 'o' 


#Strinf methods
print(s.lower())  # Convert to lowercase
print(s.upper())  # Convert to uppercase
print(s.title())  # Convert to title case
print(s.capitalize())  # Capitalize the first letter
print(s.count("o"))  # Count occurrences of 'o' 

print(s.find("o"))  # Find the first occurrence of 'o' it finds substring and returns its index
print(s.find("gelo"))
print(s.replace("o" , "Changed"))  # Find the first occurrence of 'o' (raises error if not found)

print(s.index("ch"))