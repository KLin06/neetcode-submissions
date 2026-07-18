class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        max_val = [0] * (n + 1)
        max_val[1] = nums[0]
        max_val[2] = nums[1]

        for i in range(2, n):
            max_val[i + 1] = max(max_val[i - 1], max_val[i - 2]) + nums[i]
        
        return max(max_val[n-1], max_val[n])
        