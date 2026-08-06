import bisect 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # binary search for indices
        # insert[1] binary search from intervals[0], insert[0] on binary search from intervals [1]
        # merge all from these indices
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        start_index = bisect.bisect_right(starts, newInterval[1])
        end_index = bisect.bisect_left(ends, newInterval[0])
        res = intervals[:end_index]
        combined = [float('inf'), -float('inf')]
        for i in range(end_index, start_index):
            combined[0] = min(newInterval[0], intervals[i][0], combined[0])
            combined[1] = max(newInterval[1], intervals[i][1], combined[1])
        res.append(combined if combined != [float('inf'), -float('inf')] else newInterval)       
        res.extend(intervals[start_index:])

        return res
        