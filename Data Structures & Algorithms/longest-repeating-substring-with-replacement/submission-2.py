class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_sub = l = r = 0
        n = len(s)
        c = [0] * 26

        def index(c):
            return ord(c) - ord('A')

        for r in range(n):
            c[index(s[r])] += 1

            while r - l + 1 - max(c) > k:
                c[index(s[l])] -= 1
                l += 1

            max_sub = max(max_sub, r - l + 1)                

        return max_sub
        