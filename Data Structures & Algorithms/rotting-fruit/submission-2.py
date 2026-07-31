class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_time = 0
        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def in_grid(i, j):
            return 0 <= i < rows and 0 <= j < cols

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            x, y, time = q.popleft()
            max_time = max(time, max_time)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_grid(nx, ny) and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny, time + 1))   

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return max_time 