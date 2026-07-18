class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheapest = [float('inf')] * n
        cheapest[src] = 0
 
        for _ in range(k + 1):
            temp = cheapest[:]
            for from_i, to_i, price_i in flights:
                new_price_i = cheapest[from_i] + price_i
                if new_price_i < temp[to_i]:
                    temp[to_i] = new_price_i
            cheapest = temp

        return cheapest[dst] if not cheapest[dst] == float('inf') else -1