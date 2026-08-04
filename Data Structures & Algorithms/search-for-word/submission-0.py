class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n = len(word)
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        exists = False

        def dfs (index, row, col):
            nonlocal exists
            if exists: return
            if index == n - 1:
                exists = True
                return
            visited[row][col] = True
            for d_row, d_col in directions:
                n_row, n_col = row + d_row, col + d_col
                if 0 <= n_row < rows and 0 <= n_col < cols and word[index + 1] == board[n_row][n_col] and not visited[n_row][n_col]:
                    dfs(index + 1, n_row, n_col)
            visited[row][col] = False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    dfs(0, row, col)
                    if exists: return True
        return False
