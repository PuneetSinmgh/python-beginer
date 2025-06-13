#zip function combines two or more iterables (like lists or tuples) into a single iterable of tuples.
# It pairs elements from each iterable based on their positions.
# If the iterables are of different lengths, it stops at the shortest one.
# Example of using zip to combine two lists into a list of tuples

players= [ 'Tom', 'Don','Son','Park']
goals =  [ 7, 20, 40]
print([ (name,score) for name,score in zip(players, goals) ])

