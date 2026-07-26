class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        pairs = defaultdict(list)

        for i, num in enumerate(nums):
            pairs[-num].append(i)

        print(pairs)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                sum = nums[i] + nums[j]
                missing = pairs.get(sum, [])
                for k in missing:
                    if k > j:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return list(res)