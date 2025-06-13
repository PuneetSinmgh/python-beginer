#lambda functionsd are anonymous functions defined with the lambda keyword.
# They can take any number of arguments but only have one expression.
def add(x, y):
    return x + y
# Using a lambda function to achieve the same result
add_lambda = lambda x, y: x + y
# Example usage
print(add(5, 3))          # Output: 8
print(add_lambda(5, 3))   # Output: 8
# Lambda functions can be used in higher-order functions like map, filter, and reduce

list1 = list(range(0,25))
print(list1)

def is_multiple(x):
    return x%3 == 0

list(filter( lambda x: x%3==0, list1))

# Using lambda with map to square each element in the list
squared_list = list(map(lambda x: x**2, list1))
print(squared_list)

# Using lambda with filter to get elements that are multiples of 3
filtered_list = list(filter(lambda x: x % 3 == 0, list1))
print(filtered_list)

# Using lambda with reduce to sum all elements in the list
from functools import reduce
sum_of_list = reduce(lambda x, y: x + y, list1)
print(sum_of_list)  # Output: 300

bfunc = lambda x,y : ( x+y+1, y)
bfunc(3,4)