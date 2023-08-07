import math

def find(list, n, target):
    i = 0
    j = n - 1
    while i <= j:
        mid = math.floor((i + j) / 2)
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            j = mid - 1
        elif list[mid] < target:
            i = mid + 1
    return -1

list = [1, 2, 3, 4, 5, 6]
target = 4
n = len(list)
result = find(list, n, target)
print(result)
