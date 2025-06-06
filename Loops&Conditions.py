
# This code checks if numbers in a list are even or odd and prints the result.
l = [2,4,5,6,78,9]
for i in l:
    if i%2 == 0:
        print("even")
    else:
        print("odd")


# This code checks if idex is prime and prints the result.

l = [2,4,5,6,78,9]
for i in range(len(l)):
    if i%2 == 0:
        print("even")
    else:
        print("odd")


# range function
for i in range(-5, 5):
    if i%2 == 0:
        print("even")
    else:
        print("odd")


# while loop example: index looping over the list
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while ( i < len(squares)) :
    if squares[i] == 'orange':
        new_squares.append(squares[i])
    i+=1;

print(new_squares)