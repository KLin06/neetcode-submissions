class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        longest = 0
        start = 0

        for i, c in enumerate(s):
            if c in letters:
                start = max(start, letters[c] + 1)
            letters[c] = i
            longest = max(longest, i - start + 1)

        return longest