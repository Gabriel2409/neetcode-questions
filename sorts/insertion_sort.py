def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j = j - 1
    return arr


def insertion_sort2(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        cur = arr[i]
        j = i
        while j - 1 >= 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = cur
    return arr


arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
print(insertion_sort(arr))
print(insertion_sort2(arr))
