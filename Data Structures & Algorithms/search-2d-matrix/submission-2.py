class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows * cols - 1
        while l <= r:
            m = l + (r - l) // 2
            x = m % cols
            y = m // cols
            if matrix[y][x] == target:
                print(x, y)
                return True
            elif matrix[y][x] > target:
                r = m - 1
            else: 
                l = m + 1

        return False