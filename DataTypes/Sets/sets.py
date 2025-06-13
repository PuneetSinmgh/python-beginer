# Add elements in a set
def add_elements_to_set(elements):
    """
    Adds elements to a set and returns the updated set.
    
    :param elements: An iterable of elements to be added to the set.
    :return: A set containing the added elements.
    """
    my_set = set()
    for element in elements:
        my_set.add(element)
    return my_set
# Example usage
if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5]
    updated_set = add_elements_to_set(elements)
    print("Updated Set:", updated_set)
    # Output: Updated Set: {1, 2, 3, 4, 5}
# This code defines a function to add elements to a set and demonstrates its usage.
# Sets are unordered collections of unique elements in Python.
# They are useful for storing distinct items and performing set operations like union, intersection, and difference.

#set operations : 
#union, intersection, difference, symmetric difference, copy, frozenset
# Example of set operations
def set_operations(set1, set2):
    """
    Performs various set operations on two sets and returns the results.
    
    :param set1: First set.
    :param set2: Second set.
    :return: A dictionary containing results of union, intersection, difference, and symmetric difference.
    """
    results = {
        'intersection': set1 & set2,
        'union': set1 | set2,
        'difference': set1 - set2,
        'symmetric_difference': set1 ^ set2
    }
    return results
# Example usage
if __name__ == "__main__":
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    results = set_operations(set1, set2)
    print("Set Operations Results:")
    print("Intersection:", results['intersection'])  # Output: {3, 4}
    print("Union:", results['union'])                # Output: {1, 2, 3, 4, 5, 6}
    print("Difference:", results['difference'])      # Output: {1, 2}
    print("Symmetric Difference:", results['symmetric_difference'])  # Output: {1, 2, 5, 6}

#comprehension in a set
def set_comprehension_example():
    """
    Demonstrates set comprehension to create a set of squares of even numbers from 0 to 9.
    
    :return: A set containing squares of even numbers.
    """
    return {x**2 for x in range(10) if x % 2 == 0}
# enumerate in a set
for i, val in enumerate(set_comprehension_example()):
    print(f"Index: {i}, Value: {val}")

# Example  of subset and superset
def subset_and_superset_example():
    """
    Demonstrates subset and superset operations on sets.
    
    :return: A tuple containing a subset and a superset.
    """
    set_a = {1, 2, 3}
    set_b = {1, 2, 3, 4, 5}
    return set_a.issubset(set_b), set_b.issuperset(set_a)
# Example usage
if __name__ == "__main__":
    is_subset, is_superset = subset_and_superset_example()
    print("Is set A a subset of set B?", is_subset)  # Output: True
    print("Is set B a superset of set A?", is_superset)  # Output: True
# Example of frozen set
def frozen_set_example():
    """
    Demonstrates the use of frozenset, which is an immutable version of a set.
    
    :return: A frozenset containing unique elements.
    """
    my_set = {1, 2, 3, 4}
    frozen = frozenset(my_set)
    return frozen
