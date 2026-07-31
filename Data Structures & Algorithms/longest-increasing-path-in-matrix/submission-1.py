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

        def in_matrix(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def local_min(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_matrix(nx, ny) and matrix[x][y] > matrix[nx][ny]:
                    return False
            return True

        visited = [[-1] * cols for _ in range(rows)]
        stack = []

        for x in range(rows):
            for y in range(cols):
                if local_min(x, y):
                    stack.append((1, x, y))
        
        while stack:
            length, x, y = stack.pop()

            if length <= visited[x][y]:
                continue

            visited[x][y] = length

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_matrix(nx, ny) and matrix[x][y] < matrix[nx][ny]:
                    stack.append((length + 1, nx, ny))

        return max(cell for row in visited for cell in row)







