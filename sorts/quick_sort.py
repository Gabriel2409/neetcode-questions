# pivot is last element
def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    n = len(arr)
    pvt_index = n - 1

    i = 0
    for j in range(n):
        if j == pvt_index:
            continue
        if arr[j] <= arr[pvt_index]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[pvt_index] = arr[pvt_index], arr[i]

    # not great, uses extra space
    arr[:i] = quick_sort(arr[:i])
    arr[i + 1 :] = quick_sort(arr[i + 1 :])
    return arr



def qsort(arr):
    l = 0
    r = len(arr) - 1
    return helper(arr, l, r)


def helper(arr, l, r):
    if l >= r:
        return
    pvt_index = r

    i = l
    for j in range(i, r + 1):
        if j == pvt_index:
            continue
        if arr[j] <= arr[pvt_index]:
            arr[j], arr[i] = arr[i], arr[j]
            i = i + 1
    arr[pvt_index], arr[i] = arr[i], arr[pvt_index]
    helper(arr, l, i - 1)
    helper(arr, r, i + 1)


arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
# print(quick_sort(arr))
qsort(arr)
print(arr)
