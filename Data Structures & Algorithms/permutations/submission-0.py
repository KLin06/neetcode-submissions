class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        used = [False] * n
        
        def backtrack(permutations, n, nums, used, size, curr):
            if size == n:
                permutations.append(curr[:])
                return 
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    backtrack(permutations, n, nums, used, size + 1, curr)
                    used[i] = False
                    curr.pop()
        
        backtrack(permutations, n, nums, used, 0, [])
        return permutations