class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # isolate local low points (if the 4 directions are not smaller)
        # add them to a priority queue, for each direction add it to the queue
        # pop from priority queue, adding its value to visited, and then explore all neighbours and add them to queue if they are larger
        # inside pq store (weight, index, index)
        # keep track of distance in a separate array, and use distance when evaluating
        # distance to neighbour is increased by 1
        # scan for highest value

        # scan for local low points
        # run bfs on it
        # only enqueue if the value is greater in the adj square and the visited count is lower

        rows, cols = len(matrix), len(matrix[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        memo = [[None] * cols for _ in range(rows)]

        def dfs(x, y):
            if memo[x][y]:
                return memo[x][y]
            
            best = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                    best = max(best, 1 + dfs(nx, ny))

            memo[x][y] = best
            return best

        for i in range(rows):
            for j in range(cols):
                dfs(i, j)


        return max(cell for row in memo for cell in row)







