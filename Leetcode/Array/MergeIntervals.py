from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        curr_interval = intervals[0]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= curr_interval[1]:
                curr_interval[1] = max(end, curr_interval[1])
            else:
                merged.append(curr_interval)
                curr_interval = intervals[i]

        merged.append(curr_interval)

        return merged
    
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [3, 6], [7, 8]]
    print(sol.merge(intervals))

# TC: O(NlogN) because of our sorting at the beginning
# SC: O(1) not counting the output array and the space required for it to exist