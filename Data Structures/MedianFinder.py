import heapq

class MedianFinder:

    def __init__(self):
        #two heaps, one min and one max. if the val to be added is greater than the median, it geos to the min heap. if not, it goes to the max heap. If either heap gets to be greater than 1 difference, shift the numbers around by popping and adding to other heaps. maintain min and max property and median will either be the mean of the two top values or the one that has a length greater than the other (k + 1) length
        self.min_heap = []
        self.max_heap = []
        self.median = float('inf')
        
    def addNum(self, num: int) -> None:
        if num < self.median:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped)

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            self.median = (self.min_heap[0] + self.max_heap[0]*-1) / 2
        elif len(self.min_heap) > len(self.max_heap):
            self.median = self.min_heap[0]
        else:
            self.median = -1*self.max_heap[0]
        return self.median

if __name__ == "__main__":
    mF = MedianFinder()
    mF.addNum(4)
    mF.addNum(3)
    print(mF.findMedian())
    mF.addNum(10)
    print(mF.findMedian())
    mF.addNum(2)
    print(mF.findMedian())

# TC: addNum: O(logN), findMedian: O(1)
# SC: O(N) to store the elements