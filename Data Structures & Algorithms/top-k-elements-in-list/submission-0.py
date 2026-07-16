class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1
        
        heap = [(-freq, num) for num, freq in num_freq.items()]
        heapq.heapify(heap)

        sol = heapq.nsmallest(k, heap)
        print(sol)
        sol = [val for freq, val in sol]
        return sol