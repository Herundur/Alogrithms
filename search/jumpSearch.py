import math

def jumpSearch(arr, target):

    n = len(arr)
    i = 0
    m = math.sqrt(n)

    if(arr[n - 1] < target or arr[0] > target):
        return -1

    while i < n:
        if arr[i] < target:
            i = min(int(i + m), n - 1)
        elif arr[i] > target and not arr[i-1] < target:
            i -= 1
        elif arr[i] == target:
            return i
        else:
            return -1