from random import randint, shuffle


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = round((high + low) / 2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = list(range(100))
shuffle(my_list)  # random list
value = randint(0, 100)  # random value

print(binary_search(my_list, value))