class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        #inserted the interval
        intervals.insert(-1, newInterval)

        for i in range(len(intervals)-1, 0, -1):
            if intervals[i][0] < intervals[i-1][0]:
                intervals[i], intervals[i-1] = intervals[i-1], intervals[i]
        
        #merging intervals
        curr = 1
        curr_interval = intervals[0]
        merged_intervals = [curr_interval]
        while curr < len(intervals):
            if intervals[curr][0] <= curr_interval[1]:
                merged_intervals[-1][1] = max(intervals[curr][1], curr_interval[1])
            else:
                merged_intervals.append(intervals[curr])
            curr += 1
            curr_interval = merged_intervals[-1]
        return merged_intervals
    
# TC: O(N)
# SC: O(N) for output array, O(1) if output array not counted