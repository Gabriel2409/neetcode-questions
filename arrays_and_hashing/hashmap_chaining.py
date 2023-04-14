from typing import List, Optional


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def __repr__(self):
        r = f"{self.key}:{self.val}"
        while self.next:
            self = self.next
            r += f"->{self.key}:{self.val}"
        return r


class Hashmap:
    def __init__(self):
        self.capacity = 4
        self.nb_inserted = 0
        self.arr: List[Optional[Node]] = [None for _ in range(self.capacity)]

    def hash(self, key: str) -> int:
        """sums ascii chars"""
        total = 0
        for char in key:
            total += ord(char)
        return total

    def put(self, key: str, val):
        ind = self.hash(key) % self.capacity

        if self.arr[ind] is None:
            self.arr[ind] = Node(key, val)
            self.nb_inserted += 1
        else:
            node = self.arr[ind]
            while True:
                if key == node.key:
                    node.val = val
                    break
                if node.next is None:
                    node.next = Node(key, val)
                    self.nb_inserted += 1
                    break
                node = node.next
        if self.nb_inserted >= self.capacity // 2:
            self.resize()

    def resize(self):
        self.capacity = self.capacity * 2
        self.nb_inserted = 0
        oldarr = self.arr.copy()
        self.arr = [None for _ in range(self.capacity)]
        for el in oldarr:
            node = el
            while node:
                self.put(node.key, node.val)
                node = node.next

    def get(self, key):
        ind = self.hash(key) % self.capacity
        if self.arr[ind] is None:
            return None
        else:
            node = self.arr[ind]
            while node:
                if node.key == key:
                    return node.val
                node = node.next
            return None

    def remove(self, key):
        ind = self.hash(key) % self.capacity
        if self.arr[ind] is None:
            # no pop
            return None
        else:
            node = self.arr[ind]
            if key == node.key:
                self.arr[ind] = node.next
                self.nb_inserted -= 1
                return node.val

            else:
                prev = node
                cur = node.next
                while cur:
                    if cur.key == key:
                        prev.next = cur.next
                        self.nb_inserted -= 1
                        return cur.val
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
