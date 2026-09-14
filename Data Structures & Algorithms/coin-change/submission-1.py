class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        values = [float('inf')] * (amount + 1)
        values[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    values[i] = min(values[i], values[i - coin] + 1)

        return values[amount] if not values[amount] == float('inf') else -1

        