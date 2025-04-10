class SortingAlgorithms():

    def heapsort(self, arr):
        n = len(arr)

        def _heapify(n, i):
            largest = i
            left, right = 2 * i + 1, 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                _heapify(n, largest)

        for i in range(n // 2 - 1, -1, -1):
            _heapify(n, i)
        
        for j in range(n - 1, 0, -1):
            arr[0], arr[j] = arr[j], arr[0]
            _heapify(j, 0)
       
    
if __name__ == "__main__":
    sorter = SortingAlgorithms()
    arr = [4, 7, 23, 1, 2, 9, 8, 6]
    sorter.heapsort(arr)
    print(arr)
