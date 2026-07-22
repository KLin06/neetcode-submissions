import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time = [-1] * n
        min_time[k - 1] = 0

        adj_list = {}
        for source, target, time in times:
            adj_list.setdefault(source - 1, []).append((target - 1, time))
        
        q = [(time, k - 1, target) for (target, time) in adj_list.get(k - 1, [])]
        heapq.heapify(q)
        visited = 1

        while q:
            time, source, target = heapq.heappop(q)

            if min_time[target] != -1:
                continue

            min_time[target] = time
            visited += 1

            if visited == n:
                return max(min_time)

            for next_target, next_time in adj_list.get(target, []):
                if min_time[next_target] == -1:
                    heapq.heappush(q, (time + next_time, target, next_target))

        return -1
        