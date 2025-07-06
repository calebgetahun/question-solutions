from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            curr = strs[0][i]
            for s in strs:
                if s[i] != curr:
                    return "".join(prefix)
            prefix.append(curr)
        
        return "".join(prefix)

if __name__ == "__main__":
    sol = Solution()
    test_case = ["flow", "flight", "flounder", "flowing"]
    print(sol.longestCommonPrefix(test_case))

# TC: O(N * M), where N is the number of strings in our list and M is the min length of all the strings in our list
# SC: O(1)