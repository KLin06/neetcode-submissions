from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if n < m:
            return False

        c2 = Counter(s2[0: m - 1])
        c1 = Counter(s1)

        for r in range(m - 1, n):
            c2[s2[r]] += 1
            print(c1, c2)

            if c2 == c1:
                return True

            c2[s2[r - m + 1]] -= 1

        return False

        