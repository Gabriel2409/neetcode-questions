def count_sort(arr):
    min_val = min(arr)
    max_val = max(arr)

    freqs = [0 for _ in range(max_val - min_val + 1)]
    for el in arr:
        freqs[el - min_val] += 1

    new_arr = []
    for i, freq in enumerate(freqs):
        new_arr.extend([i + min_val] * freq)
    return new_arr


print(count_sort([1, 12, 4, 4, 38, 7, 65, 98, 54, 22, 56, 58, 31, 47]))
