"""
Problem description:
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        start, end = 0, n - 1
        while start < end:
            if s[start] != s[end]:
                return self.checkPalindrome(s, start+1, end) or self.checkPalindrome(s, start, end-1)
            else:
                start += 1
                end -= 1
        return True
            
    def checkPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
#test cases
testCases = ['aba', 'eceec', 'zrtetruz', 'aaaa', 'frghuhewrurwehihgrf', " ' ' kd"]
solution = Solution()
for word in testCases:
    print(solution.validPalindrome(word))

"""
TC: O(n) since we are iterating through the string once until we encounter mismatched strings. When this occurs we check 2 instances
of the problem space by looking at the different strings that could be our answer if we deleted one char or the other
SC: O(1) since we are storing the information of 2 pointers throughout the implementation
"""