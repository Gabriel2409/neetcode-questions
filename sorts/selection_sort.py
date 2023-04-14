def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        minimum = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
print(selection_sort(arr))
