class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sol = []
        q = deque()
        for i, val in enumerate(nums):
            while q and q[0][0] <= i - k:
                q.popleft()
            while q and q[-1][1] <= val:
                q.pop()
            q.append((i, val)) 
            if i >= k - 1: sol.append(q[0][1])

        return sol
