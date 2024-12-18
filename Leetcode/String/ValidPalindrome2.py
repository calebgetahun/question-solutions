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
    

testCases = ['aba', 'eceec', 'zrtetruz', 'aaaa', 'frghuhewrurwehihgrf', " ' ' kd"]
solution = Solution()
for word in testCases:
    print(solution.validPalindrome(word))