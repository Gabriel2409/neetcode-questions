
from collections import Counter
def bucket_sort(arr):
    counter  = Counter(arr)

    store = [[] for _ in range(100)]
    for key,val in counter.items():
        for _ in range(val):
            store[key].append(key)
    
    final = []
    for bucket in store:
        for el in bucket:
            final.append(el)
    return final

print(bucket_sort([1,2,4,2,8,7,5,98,54,2,56,8,1,0]))


    




