from itertools import accumulate

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lesser = [0] * (n)
        greater = [0] * (n)
        left_max = right_max = 0
        for i in range(1, n):
            lesser[i] = left_max = max(left_max, height[i - 1])
            greater[n - i - 1] = right_max = max(right_max, height[n - i])

        water = 0
        for i in range(n):
            water += max(min(lesser[i], greater[i]) - height[i], 0)
        return water
        
