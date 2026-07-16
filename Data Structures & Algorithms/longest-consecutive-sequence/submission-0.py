class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        maxLength = 0
        for num in nums:
            if num - 1 in nums:
                continue
            
            length = 1
            while num + 1 in nums:
                num += 1
                length += 1
            
            maxLength = max(maxLength, length)

        return maxLength
        