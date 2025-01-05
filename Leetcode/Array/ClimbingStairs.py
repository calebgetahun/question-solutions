class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        first, second = 2, 3
        curr = 3
        for _ in range(3, n):
            curr = first + second
            first = second
            second = curr
            
        return curr

if __name__ == "__main__":
    sol = Solution()
    for i in range(45):
        print(sol.climbStairs(i))

# TC: O(N)
# SC: O(1)