class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start = 0
        maxSub = 1
        seen = {s[0]}

        for end in range(1, len(s)):
            curr = s[end]
            while curr in seen:
                seen.remove(s[start])
                start += 1
                
            seen.add(curr)
            maxSub = max(maxSub, end - start + 1)

        return maxSub

if __name__ == "__main__":
    sol = Solution()
    test_strings = ["abcabcbb", "bbbbb", "pwwkek"]
    for s in test_strings:
        print(sol.lengthOfLongestSubstring(s))

# TC: O(N)
# SC: O(1) for the set holding our characters since there is a max number of values (256) that could be in our string.