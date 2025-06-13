nums = [2,5,3,8,34,7,9,3,5,6,7,88,77,34,3,4,4,65,65,67,7,8798,4]
nums.sort(reverse=True)
print(nums)

#searching for a number in the list
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Example usage of binary search
target = 34
index = binary_search(nums, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")


# Example of sorting a list of tuples based on the second element
def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])
# Example usage
tuples_list = [(1, 3), (2, 1), (3, 2)]
sorted_tuples = sort_tuples_by_second_element(tuples_list)
print("Sorted tuples by second element:", sorted_tuples)

# Example of sorting a list of dictionaries by a specific key
def sort_dicts_by_key(dicts_list, key):
    return sorted(dicts_list, key=lambda x: x[key]) 

# Example of sorting a dictionary by its keys
def sort_dict_by_keys(input_dict):
    return dict(sorted(input_dict.items()))
# Example usage
input_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = sort_dict_by_keys(input_dict)
print("Sorted dictionary by keys:", sorted_dict)

# Example usage of sorting dictionaries by first element in tuple values
def sort_dicts_by_first_tuple_element(dicts_list):
    return sorted(dicts_list, key=lambda x: x[0][0])
# Example usage
dicts_list = [((1, 2), 'a'), ((3, 4), 'b'), ((0, 5), 'c')] 
sorted_dicts = sort_dicts_by_first_tuple_element(dicts_list)
print("Sorted dictionaries by first tuple element:", sorted_dicts)


# Example of sorting a list of strings by length
def sort_strings_by_length(strings_list):
    return sorted(strings_list, key=len)