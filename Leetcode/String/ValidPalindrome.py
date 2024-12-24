class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start, end = 0, n - 1
        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and end > start:
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
    
if __name__ == "__main__":
    sol = Solution()
    test_1 = "racecar"
    test_2 = "sator, arepo tenet :opera ./>rotas"
    test_3 = "The string was not a palindrome and this made it very sad"
    print(sol.isPalindrome(test_1))
    print(sol.isPalindrome(test_2))
    print(sol.isPalindrome(test_3))

# TC: O(N)
# SC: O(1)