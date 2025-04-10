class MinHeap():
    def __init__(self):
        self.heap = []

    def find_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _parent(self, i):
        return (i - 1) // 2
    
    def _left_child(self, i):
        return (i * 2) + 1
    
    def _right_child(self, i):
        return (i * 2) + 2

    def _heapify(self, i):
        smallest = i
        left_child = self._left_child(i)
        right_child = self._right_child(i)

        if left_child < len(self.heap) and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        
        if right_child < len(self.heap) and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child
        
        if smallest != i: #aka we are not holding the smallest value in our root
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify(smallest)
        

    def heap_push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def heap_pop(self):
        #extract the minimum and maintain heap property for rest of heap
        if not self.heap:
            return None
        
        popped = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify(0)

        return popped

    def build_heap_from_array(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(i)


class MaxHeap():
    def __init__(self):
        self.heap = []
    
    def find_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _parent(self, i):
        return (i - 1) // 2
    
    def _left_child(self, i):
        return (i * 2) + 1
    
    def _right_child(self, i):
        return (i * 2) + 2

    def _heapify(self, i):
        largest = i
        left_child = self._left_child(i)
        right_child = self._right_child(i)

        if left_child < len(self.heap) and self.heap[largest] < self.heap[left_child]:
            largest = left_child
        
        if right_child < len(self.heap) and self.heap[largest] < self.heap[right_child]:
            largest = right_child
        
        if largest != i: #aka we are not holding the smallest value in our root
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify(largest)

    def heap_push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)
        
    def heap_pop(self):
        if not self.heap:
            return None
        
        popped = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify(0)

        return popped    

    def build_heap_from_array(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(i)    

if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.heap_push(2)
    min_heap.heap_push(3)

    min_heap.heap_push(1)
    print(min_heap.heap)
    print(min_heap.heap_pop())
    print(min_heap.heap)
    print(min_heap.heap_pop())
    print(min_heap.heap)
    print(min_heap.heap_pop())
    print(min_heap.heap)
    print(min_heap.heap_pop())
    print(min_heap.heap)

    max_heap = MaxHeap()
    max_heap.heap_push(2)
    max_heap.heap_push(5)
    max_heap.heap_push(1)
    max_heap.heap_push(10)
    max_heap.heap_push(4)
    print(max_heap.heap)

    max_heap.heap_push(10)
    print(max_heap.heap)
    print(max_heap.heap_pop())
    print(max_heap.heap_pop())
    print(max_heap.heap)

    arr = [3,6,4,1,2,0,8]
    mh = MaxHeap()
    mh.build_heap_from_array(arr)
    print(mh.heap)