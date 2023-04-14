from typing import List, Optional


class Hashmap:
    def __init__(self):
        self.capacity = 4
        self.nb_inserted = 0
        self.arr = [None for _ in range(self.capacity)]

    def hash(self, key: str) -> int:
        """sums ascii chars"""
        total = 0
        for char in key:
            total += ord(char)
        return total

    def put(self, key: str, val):
        ind = self.hash(key) % self.capacity
        while self.arr[ind] is not None:
            if self.arr[ind] == -1:
                ind += 1
            elif self.arr[ind][0] == key:
                self.arr[ind] = (key, val)
                return
            else:
                ind += 1
            if ind == len(self.arr):
                ind = 0

        self.arr[ind] = (key, val)
        self.nb_inserted += 1

        if self.nb_inserted >= self.capacity // 2:
            self.resize()

    def resize(self):
        self.capacity = self.capacity * 2
        self.nb_inserted = 0
        oldarr = self.arr.copy()
        self.arr = [None for _ in range(self.capacity)]
        for el in oldarr:
            if el is not None and el != -1:
                self.put(el[0], el[1])

    def get(self, key):
        ind = self.hash(key) % self.capacity
        while self.arr[ind] is not None:
            if self.arr[ind] == -1:
                ind += 1
            elif self.arr[ind][0] == key:
                return self.arr[ind][1]
            else:
                ind += 1
            if ind == len(self.arr):
                ind = 0
        return None

    def remove(self, key):
        ind = self.hash(key) % self.capacity
        while self.arr[ind] is not None:
            if self.arr[ind] == -1:
                ind += 1
            elif self.arr[ind][0] == key:
                val = self.arr[ind][1]
                self.arr[ind] = -1
                return val
            else:
                ind += 1
            if ind == len(self.arr):
                ind = 0
        return None


h = Hashmap()
h.put("A", 1)
h.put("B", 2)
h.put("B", 4)
h.put("A", 3)
h.put("AB", 1)
h.put("BA", 2)
h.remove("AB")
h.remove("BA")


print()
