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
            i+=1
    
    arr[i], arr[pvt_index] = arr[pvt_index], arr[i]

    # not great, uses extra space
    arr[:i] = quick_sort(arr[:i])
    arr[i+1:] = quick_sort(arr[i+1:])
    return arr

def quick_sort_with_extra_param(arr: list[int], low, high) -> list[int]:


    def partition(arr, low, high):
        pvt_index = high

        i = low
        for j in range(low,high + 1):
            if j == pvt_index:
                continue
            if arr[j] <= arr[pvt_index]:
                arr[j], arr[i] = arr[i], arr[j]
                i+=1
        
        arr[i], arr[pvt_index] = arr[pvt_index], arr[i]


        return i

    if low < high:
        i = partition(arr, low, high)
        quick_sort_with_extra_param(arr, low, i-1)
        quick_sort_with_extra_param(arr, i+1, high)




    # not great, uses extra space
    return arr


arr = [1, 5, 9, 8, 7, 6, 4, 2, 2, 5, 3]
print(quick_sort(arr))
print(quick_sort_with_extra_param(arr, 0, len(arr) - 1))
