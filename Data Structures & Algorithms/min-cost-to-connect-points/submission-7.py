class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(i, j):
            xi, yi = i
            xj, yj = j
            return abs(xi - xj) + abs(yi - yj)

        n = len(points)
        visited = [False] * n
        min_edge = [float("inf")] * n
        min_edge[0] = 0
        min_cost = 0

        for _ in range(n):
            closest_node = -1
            closest_distance = float("inf")
            for j in range(n):
                if not visited[j] and min_edge[j] < closest_distance:
                    closest_distance = min_edge[j]
                    closest_node = j

            visited[closest_node] = True
            min_cost += closest_distance

            for j in range(n):
                if not visited[j]:
                    d = manhattan_distance(points[closest_node], points[j])
                    if d < min_edge[j]:
                        min_edge[j] = d

        return min_cost