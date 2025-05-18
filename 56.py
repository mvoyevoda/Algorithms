class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(reverse=True)
        idx = len(intervals)-1
        while idx > 0:
            interval, next_interval = intervals[idx], intervals[idx-1]
            if interval[1] >= next_interval[0]:
                intervals.pop()
                intervals.pop()
                intervals.append([interval[0], max(next_interval[1], interval[1])])
            else:
                intervals.pop()
                output.append(interval)
            idx -= 1
                
        return output + intervals

# Different types of intervals when sorted
# 1. non-merge interval
# 2. merge interval [a,b] behind [c,d] where c < b < c
# 3. merge interval [a,b] behind [c,d] where c < d < b

# Type 3 Interval Scenario:
# [1, 7] [3, 5] [4, 6]