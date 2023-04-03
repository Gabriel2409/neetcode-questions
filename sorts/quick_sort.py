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


def quick_sort_in_place(arr: list[int], l, r):
    if l >= r:
        return 

    pvt_index = r

    i = l
    for j in range(l, r + 1):
        if j == pvt_index:
            continue
        if arr[j] <= arr[pvt_index]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[pvt_index] = arr[pvt_index], arr[i]

    quick_sort_in_place(arr, l, i - 1)
    quick_sort_in_place(arr, i + 1, r)


arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
# print(quick_sort(arr))
quick_sort_in_place(arr, 0, len(arr) - 1)
print(arr)
