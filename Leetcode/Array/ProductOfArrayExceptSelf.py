class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n
        
        for i in range(1, n):
            output[i] = nums[i-1] * output[i-1]

        curr_prod = nums[-1]
        for j in range(n-2, -1, -1):
            output[j] *= curr_prod
            curr_prod *= nums[j]

        return output

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4]
    print(sol.productExceptSelf(arr))

# TC: O(N)
# SC: O(1) not counting the output array

