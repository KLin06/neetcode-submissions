class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        stack = []
        for i, height in enumerate(heights):
            rect_start = i
            while stack and stack[-1][0] >= height:
                rect_height, rect_start = stack.pop()
                max_area = max(max_area, rect_height * (i - rect_start))
            stack.append((height, rect_start))

        for height, start in stack:
            max_area = max(max_area, height * (n - start))
        return max_area
        