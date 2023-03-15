# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y
# plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
import heapq


def get_dist(pt):
    return pt[0] ** 2 + pt[1] ** 2


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    dists = [(get_dist(points[i]), i) for i in range(len(points))]

    final = []

    heapq.heapify(dists)
    total = 0
    while total < k:
        popped = heapq.heappop(dists)
        final.append(points[popped[1]])
        total = total + 1
    return final


points = [[1, 3], [-2, 2]]
k = 1
print(k_closest(points, k))
