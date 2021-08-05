class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x, y):
            return (x ** 2 + y ** 2) ** (1 / 2)
        return sorted(points, key = lambda x: euclidean_distance(x[0], x[1]))[:k]