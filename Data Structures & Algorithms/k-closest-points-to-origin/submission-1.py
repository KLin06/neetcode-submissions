class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(x**2 + y**2, x, y) for x, y in points]
        dist.sort()
        return [[x, y] for d, x, y in dist[:k]]
        