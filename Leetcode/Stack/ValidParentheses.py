class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if stack:
                    par = stack.pop()
                    if pairs[par] != char:
                        return False
                else:
                    return False
        return not stack
    
valid_parenthesis = Solution()
test_par = "()[]{()[]}"
test_par_invalid = "()[]{()[]}{}{]"
test_par_single = "["
test_empty_string = ""

print(valid_parenthesis.isValid(test_par))
print(valid_parenthesis.isValid(test_par_invalid))
print(valid_parenthesis.isValid(test_par_single))
print(valid_parenthesis.isValid(test_par_single))
    
# TC: O(N)
# SC: O(N)