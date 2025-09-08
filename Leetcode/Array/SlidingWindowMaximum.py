from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i, curr in enumerate(nums):
            while q and nums[q[-1]] <= curr:
                q.pop()

            q.append(i)
            
            if q[0] == i - k:
                q.popleft()
            
            if i >= k - 1:
                res.append(nums[q[0]])

        return res

if __name__ == "__main__":
    sol = Solution()
    arr = [1,3,-1,-3,5,3,6,7]
    print(sol.maxSlidingWindow(arr, k=3))

# TC: O(N)
# SC: O(k)