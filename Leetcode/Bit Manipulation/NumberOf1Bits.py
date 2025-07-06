class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            weight += (n & 1)
            n = n >> 1
        return weight
    
if __name__ == "__main__":
    sol = Solution()
    test_cases = [1, 23, 129, 128, 63]
    for case in test_cases:
        print(sol.hammingWeight(case))

# TC: O(log(N)) where log(N) is the number of bits in N
# SC: O(1)