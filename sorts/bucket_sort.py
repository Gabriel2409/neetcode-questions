from collections import Counter


def bucket_sort(arr):
    counter = Counter(arr)

    store = [[] for _ in range(100)]
    for key, val in counter.items():
        for _ in range(val):
            store[key].append(key)

    final = []
    for bucket in store:
        for el in bucket:
            final.append(el)
    return final


def bucket_sort2(arr):
    min_val = min(arr)
    max_val = max(arr)

    nb_buckets = 8
    buckets = [[] for _ in range(nb_buckets)]

    for el in arr:
        ind = int((el - min_val) / (max_val - min_val) * (nb_buckets - 1))
        print(ind)
        buckets[ind].append(el)
    for buck in buckets:
        buck.sort()

    final_arr = []
    for buck in buckets:
        for el in buck:
            final_arr.append(el)
    return final_arr


print(bucket_sort([1, 2, 4, 2, 8, 7, 5, 98, 54, 2, 56, 8, 1, 0]))
print(bucket_sort2([1, 2, 4, 2, 8, 7, 5, 98, 54, 2, 56, 8, 1, 0]))
