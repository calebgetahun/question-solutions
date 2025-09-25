import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter for elements
        counter = Counter(nums)
        #min heap that will store the top k elements. When we see a freq higher, we compare to the current highest and kick off if it is higher. Until we have k elements, just add them to the heap
        min_heap = []

        for num, freq in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                top_freq = min_heap[0][0]
                if freq > top_freq:
                    heapq.heappushpop(min_heap, (freq, num))
        
        return [num for freq, num in min_heap]
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,3,3,2,2,3,3]
    k = 2
    print(sol.topKFrequent(nums, k))

# TC: O(NlogK)
# SC: O(N)