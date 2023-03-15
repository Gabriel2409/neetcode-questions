import math


def min_eating_speed(piles: list[int], h: int) -> int:
    l = math.ceil(sum(piles) / h)
    # l = 1
    r = max(piles)
    res = r

    while l <= r:
      
        mid = (l + r)// 2
        time = 0
        for el in piles:
            time = time + math.ceil(el / mid)
        if time > h:
            l = mid + 1
        else:
            r = mid - 1
        res = min(res, mid)
    return res

piles = [3,6,7,11]
h = 70
print(min_eating_speed(piles, h))