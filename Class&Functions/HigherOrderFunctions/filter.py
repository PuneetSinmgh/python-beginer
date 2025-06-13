list1 = list(range(0,25))
print(list1)

def is_multiple(x):
    return x%3 == 0

list(filter(is_multiple, list1))