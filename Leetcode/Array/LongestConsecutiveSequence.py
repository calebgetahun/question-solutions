class Solution:
    def longestConsecutiveSorting(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums_ = list(set(nums))
        nums_.sort()
        max_sub = 1
        curr_max = 1
        i = 1
        for i in range(len(nums_)):
            if nums_[i] == nums_[i-1] + 1:

                curr_max += 1
                max_sub = max(max_sub, curr_max)
                
            else:
                curr_max = 1
                
        return max_sub

    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        
        max_sub = 0
        for num in nums:
            if num-1 not in nums:
                curr_max = 1
                while num + curr_max in nums:
            # check for each subsequent value in n
                    curr_max += 1

                max_sub = max(curr_max, max_sub)

        return max_sub
        
if __name__ == "__main__":
    sol = Solution()
    test_case = [0,3,7,2,5,8,4,6,0,1]
    print(sol.longestConsecutiveSorting(test_case))
    print(sol.longestConsecutive(test_case))

# TC: O(N)
# SC: O(N)