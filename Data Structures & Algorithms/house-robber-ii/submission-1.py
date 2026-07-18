class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev2, prev1 = 0, 0
        for num in nums[:-1]:
            curr = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = curr
        
        first_house = prev1

        prev2, prev1 = 0, 0
        for num in nums[1:]:
            curr = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = curr
        
        return max(prev1, first_house)


        