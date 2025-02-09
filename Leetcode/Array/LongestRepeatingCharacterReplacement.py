class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #answer is at least as large as k. if len(s) == k, the answer is k
        if len(s) == k:
            return k
        
        chars = dict()
        i = j = 0
        ans = 0
        curr_max = 0

        while j < len(s):
            chars[s[j]] = chars.get(s[j], 0) + 1
            if chars[s[j]] > curr_max:
                curr_max = chars[s[j]]

            if (j - i + 1 - k) <= curr_max:
                ans = max(ans, j-i+1)
            else:
                chars[s[i]] -= 1
                i += 1
            j += 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "AABABBA"
    k = 1
    print(sol.characterReplacement(s, k))

# TC: O(N)
# SC: O(1) since our input string only consists of 26 characters. We utilize extra space, however it is not dependent on the size of the input string. O(26) = O(1)

# Note: once a maximal size window is found, we continue to search for elements within that window size. We could technically shorten the 
# window size until we hit another valid string size, but since we are trying to find the maximal window size, we could just continue with the 
# maximal size we have seen thus far, which is why we do not continuously update i until we find a variable that works. We also won't override 
# our ans in any case until the condition is met, thus ensuring correctness