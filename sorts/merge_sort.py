def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    l = merge_sort(arr[0:mid])
    r = merge_sort(arr[mid:])

    i = 0
    j = 0
    final = []
    while i < len(l) or j < len(r):
        if j == len(r):
            final.append(l[i])
            i = i + 1
        elif i == len(l):
            final.append(r[j])
            j = j + 1
        else:
            if l[i] <= r[j]:
                final.append(l[i])
                i = i + 1
            else:
                final.append(r[j])
                j = j + 1
    return final


def merge_sort_2(arr: list[int], l, r) -> list[int]:
    if l >= r:
        return arr

    mid = (l + r) // 2

    merge_sort_2(arr, l, mid)
    merge_sort_2(arr, mid + 1, r)

    left = arr[l:mid+1]
    right = arr[mid+1: r+1]


    i = 0
    j = 0
    k = l
    while i < len(left) or j < len(right):
        if j == len(right):
            arr[k] = left[i]
            i = i + 1
            k = k +1
        elif i == len(left):
            arr[k] = right[j] 
            j = j + 1
            k = k +1
        else:
            if left[i] <= right[j]:
                arr[k] = left[i] 
                i = i + 1
                k = k +1
            else:
                arr[k] = right[j] 
                k = k +1
                j = j + 1
    return arr


arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
print(merge_sort(arr))
print(merge_sort_2(arr, 0, len(arr)-1))
