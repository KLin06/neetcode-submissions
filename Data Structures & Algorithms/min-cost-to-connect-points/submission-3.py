class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance (xi, yi, xj, yj):
            return abs(xi - xj) + abs(yi - yj)

        distances = []
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                distances.append((manhattan_distance(xi, yi, xj, yj), i, j))
        distances.sort(key=lambda x: x[0])

        parents = [i for i in range(n)]

        def get_parent(point):
            if parents[point] == point: return point
            parents[point] = get_parent(parents[point])
            return parents[point]

        def merge(point_a, point_b):
            root_a, root_b = get_parent(point_a), get_parent(point_b)
            if root_a != root_b:
                parents[root_a] = root_b

        def same(point_a, point_b):
            return get_parent(point_a) == get_parent(point_b)
        
        min_cost = 0

        for distance, i, j in distances:
            if same(i, j): continue
            min_cost += distance
            merge(i, j)

        return min_cost
        
        