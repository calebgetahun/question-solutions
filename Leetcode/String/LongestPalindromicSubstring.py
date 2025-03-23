class Solution:
    def longestPalindrome(self, s: str) -> str:
        #iterate through s twice: once for odd and once for even and expand outwards to check for palindromes
        res = s[0]
        resLen = 1

        #odd
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    if (right - left + 1) > resLen:
                        res = s[left:right+1]
                        resLen = right-left+1
                else:
                    break
                left -= 1
                right += 1

        #even
        for i in range(len(s) - 1):
            left, right = i, i + 1
            if s[left] != s[right]:
                continue
            
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    if (right - left + 1) > resLen:
                        res = s[left:right+1]
                        resLen = right - left + 1
                    left -= 1
                    right += 1

                else:
                    break

        return res

if __name__ == "__main__":
    sol = Solution()
    s = "abacdcadxf"
    print(sol.longestPalindrome(s))

# TC: O(N^2)
# SC: O(1)

# Note: Brute force solution runs in O(N^3) by checking if every substring is a palindrome. Solution above takes advantage of looking at each letter and expanding outwards. Linear time solution exists with Manacher's Algorithm
