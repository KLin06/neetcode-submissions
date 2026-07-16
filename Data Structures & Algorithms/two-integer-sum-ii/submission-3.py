class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        s = numbers[l] + numbers[r]
        while (target != s):
            if target < s:
                r -= 1
            if target > s:
                l += 1
            s = numbers[l] + numbers[r]
        

        return [l + 1, r + 1]
        