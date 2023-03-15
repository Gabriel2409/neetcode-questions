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


arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
print(merge_sort(arr))
