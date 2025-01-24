from typing import List

class Solution:
    def majorityElementUsingDictionary(self, nums: List[int]) -> int:
        counter = dict()

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        return max(counter, key=counter.get)
    def majorityElement(self, nums: List[int]) -> int:
        

        count = 0
        curr = 0

        for num in nums:
            if not count:
                count += 1
                curr = num
                continue
            if num == curr:
                count += 1
            else:
                count -= 1
                if count < 0:
                    curr = num
        
        return curr
    
if __name__ == "__main__":
    sol = Solution()
    arr = [2,3,4,2,2]
    print(sol.majorityElement(arr))
    print(sol.majorityElementUsingDictionary(arr))

# TC: O(N) for both solutions
# SC: O(N) for dictionary implementation, O(1) for counting method
# Considerations: if the majority element is not present in greater than n / 2 occurences, where n is the length of the array, the dictionary method might be more preferred as there needs to be a clear majority for method 2 to work.
