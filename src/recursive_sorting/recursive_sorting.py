# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr


def quicksort(arr, low, high):
    if low >= high:
        return arr
    else:
        pivot_index = low
        for i in range(low, high):
            if arr[i]< arr[pivot_index]:
                temp = arr[pivot_index + 1]
                arr[pivot_index + 1] = arr[i]
                arr[i] = temp

                temp = arr[pivot_index]
                arr[pivot_index] = arr[pivot_index + 1]
                arr[pivot_index + 1] = temp
                pivot_index += 1

    arr = quicksort(arr, pivot_index, low)
    arr = quicksort(arr, pivot_index+1, high)
