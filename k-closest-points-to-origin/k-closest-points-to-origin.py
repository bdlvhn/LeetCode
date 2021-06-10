class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDist(point: List[int]) -> float:
            return math.sqrt(abs(point[0])**2 + abs(point[1])**2)
        lst = []
        for point in points:
            lst.append((findDist(point),point))
        lst.sort()
        return list(map(lambda x: x[1],lst[:k]))