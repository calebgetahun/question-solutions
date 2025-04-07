from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #immediately looks to me like a situation where we use backtracking to iterate through all possibilities. Go through all possible combinations for each letter.
        if not digits:
            return []
        
        res = []
        numberLetters = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        n = len(digits)

        def backtrack(currString, res, index):
            if len(currString) == n:
                res.append("".join(currString))
                return
            
            letters = numberLetters[digits[index]]
            
            for i in range(len(letters)):
                currString.append(letters[i])
                backtrack(currString, res, index+1)
                currString.pop()
        
        backtrack([], res, 0)
        return res

if __name__ == "__main__":
    sol = Solution()
    digits = "236"
    print(sol.letterCombinations(digits))

# TC: O(4^N)
# SC: O(N) (not counting output array) for recursion depth, as we can extend as far as the length of one of the strings in our answer, which depends on the # of digits