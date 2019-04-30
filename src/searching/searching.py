# STRETCH: implement Linear Search				
def linear_search(arr, target):
    for a in arr:
        if a == target:
            return a

    return -1  # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    # TO-DO: add missing code
    while len(arr) > 0:
        mid = int(len(arr) / 2)
        mid_test = arr[mid]
        if mid_test == target:
            return target
        elif mid_test > target:
            arr = arr[:mid]
        else:
            arr = arr[mid + 1:]

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target):
    # middle = (low + high) // 2
    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    while len(arr) > 1:
        middle = int(len(arr) / 2)
        if arr[middle] == target:
            arr = arr[middle:middle + 1]
        elif arr[middle] > target:
            arr = binary_search_recursive(arr[:middle], target)
        else:
            arr = binary_search_recursive(arr[middle + 1:], target)
    return arr


ar = [1, 2, 3, 4, 5, 65, 7, 8, 9, 10, 11, 12, 13]
# print(binary_search(ar, 6))
print(binary_search_recursive(ar, 6))
