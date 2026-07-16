class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_s = Counter(s)
        letter_t = Counter(t)

        return letter_s == letter_t
        