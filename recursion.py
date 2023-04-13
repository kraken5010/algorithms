# sum elements of list
def summ(lst: list):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]

    return lst[0] + summ(lst[1::])


# quick sort for number list
def quicksort(lst: list):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
