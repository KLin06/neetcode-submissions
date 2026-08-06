class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for interval in intervals:
            if not res: 
                res.append(interval)
                continue
            if res[-1][1] >= interval[0]: 
                res[-1][1] = max(res[-1][1], interval[1])
            else: res.append(interval)

        return res        