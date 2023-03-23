arr = [2, 5, 6, 7, 13, 17, 20, 21, 25]

targ = 17


def BinarySearch(arr, targ):
    l, r = 0, len(arr)

    while l < r:
        mid = (l + r) // 2
        if arr[mid] == targ:
            return mid
        elif arr[mid] < targ:
            l = mid + 1
        else:
            r = mid -1
    return -1


print(BinarySearch(arr, targ))
