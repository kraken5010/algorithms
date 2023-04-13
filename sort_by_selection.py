# Find index smallest element in list
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(find_smallest([5, 2, 3, 10, 0, 1]))


# Sort ascending in list
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = min(arr)
        new_arr.append(smallest)
        arr.remove(smallest)
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))