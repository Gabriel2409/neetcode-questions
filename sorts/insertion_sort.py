def insertions_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        j = i -1
        while j >= 0  and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j+1], arr[j]
            j = j -1
    return arr



arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
print(insertions_sort(arr))
