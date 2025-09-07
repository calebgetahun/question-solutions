import math
from collections import deque

def main(n, arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if math.gcd(arr[i], 2 * arr[j]) > 1:
                total += 1
    return total

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        size = int(input())
        arr = list(map(int, input().split()))
        sorted_arr = deque()
        for a in arr:
            if a % 2 == 0:
                sorted_arr.appendleft(a)
            else:
                sorted_arr.append(a)

        print(main(size, sorted_arr))

# TC: O(N^2)
# SC: O(N) for deque
