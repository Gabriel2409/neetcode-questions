def bubble_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        for j in range(len(arr)-i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr



arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
print(bubble_sort(arr))
