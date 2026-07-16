class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = []

        def combination (index, sum, target, stack, nums):
            if sum == target:
                ans.append(stack[:])
                return

            if sum > target or index > len(nums) - 1:
                return
            
            stack.append(nums[index])
            combination(index, sum + nums[index], target, stack, nums)
            stack.pop()
            combination(index + 1, sum, target, stack, nums)

        combination(0, 0, target, stack, nums)
        return ans