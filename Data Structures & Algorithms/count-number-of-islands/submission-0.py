class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def in_grid (y, x):
            return 0 <= y < rows and 0 <= x < cols
        
        for j in range(0, rows):
            for i in range(0, cols):
                if grid[j][i] == "1":
                    q = deque([(j, i)])
                    num_islands += 1
                    while q:
                        y, x = q.popleft()
                        for dy, dx in directions:
                            new_y, new_x = y + dy, x + dx
                            if in_grid(new_y, new_x) and grid[new_y][new_x] == "1":
                                grid[new_y][new_x] = "0"
                                q.append((new_y, new_x))
                        
        return num_islands
        
        