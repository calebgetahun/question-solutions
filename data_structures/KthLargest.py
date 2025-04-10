import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = [] #min heap of k elements
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k or val >= self.heap[0]:
            heapq.heappush(self.heap, val)
            #pop min from heap and add new value to heap. then return root of heap
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
        return self.heap[0]

if __name__ == "__main__":
    k, nums = 3, [4, 5, 8, 2]
    obj = KthLargest(k, nums)
    vals = [3, 5, 10, 9, 4]

    for val in vals:
        print(obj.add(val))

# TC: initialization: O(NlogK), add: O(logK)
# SC: O(k) for heap