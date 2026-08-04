class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area, stack = 0, [(row, col)]
                    grid[row][col] = 0
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                stack.append((nr, nc))
                    max_area = max(max_area, area)

        return max_area