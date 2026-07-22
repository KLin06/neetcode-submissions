class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        p = len(text1)
        q = len(text2)
        dp = [[0] * q for _ in range(p)]
        
        def get_length(i, j):
            if i >= 0 and j >= 0:
                return dp[i][j]
            return 0

        # p tall, q wide
        for i in range(p):
            c_1 = text1[i]
            for j in range(q):
                c_2 = text2[j]

                if c_1 == c_2:
                    dp[i][j] = max(get_length(i - 1, j - 1) + 1, get_length(i - 1, j), get_length(i, j - 1))
                else:
                    dp[i][j] = max(get_length(i - 1, j), get_length(i, j - 1))
                
        return dp[p - 1][q - 1]
