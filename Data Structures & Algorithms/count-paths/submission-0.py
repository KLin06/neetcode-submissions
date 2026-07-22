import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fact_m_n = math.factorial(m + n - 2)
        fact_m = math.factorial(m - 1)
        fact_n = math.factorial(n - 1)
        return fact_m_n // (fact_m * fact_n)
        