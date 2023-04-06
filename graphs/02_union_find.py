class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = i

    def find(self, i):
        while i != self.par[i]:
            # path compression
            self.par[i] = self.par[self.par[i]]
            i = self.par[i]
        return i

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        # if they have the same parent, we can't perform a join
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True
