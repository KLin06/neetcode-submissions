import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[float('inf')] * n for _ in range(n)]
        adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pq = [(grid[0][0], 0, 0)]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < n

        while pq:
            time, x, y = heapq.heappop(pq)

            if time >= visited[y][x]:
                continue

            visited[y][x] = time
    
            for dx, dy in adj:
                nx, ny = x + dx, y + dy
                if valid(nx, ny) and visited[ny][nx] == float('inf'):
                    heapq.heappush(pq, (max(time, grid[ny][nx]), nx, ny))

        
        return visited[n - 1][n - 1]


        