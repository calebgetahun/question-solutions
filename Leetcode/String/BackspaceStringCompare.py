class Solution:
    def backSpaceCompareStacks(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for char in s:
            if char != "#":
                s_stack.append(char)
            else:
                if s_stack:
                    s_stack.pop()

        for char in t:
            if char != "#":
                t_stack.append(char)
            else:
                if t_stack:
                    t_stack.pop()

        return s_stack == t_stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(string, index):
            hash_count = 0
            while index >= 0:
                if hash_count == 0 and string[index] != "#":
                    break
                elif string[index] == "#":
                    hash_count += 1
                else:
                    hash_count -= 1
                index -= 1
            return index 

        ps = len(s) - 1
        pt = len(t) - 1

        while ps >= 0 or pt >= 0:
            ps = nextValidChar(s, ps)
            pt = nextValidChar(t, pt)

            if ps == -1 and pt == -1:
                return True

            elif ps == -1 or pt == -1:
                return False

            elif s[ps] != t[pt]:
                return False
                
            ps -= 1
            pt -= 1
            
        return True
    
if __name__ == "__main__":
    sol = Solution()
    s, t = "nzp#o#g", "b#nzp#o#g"
    print(sol.backspaceCompare(s, t))
    print(sol.backSpaceCompareStacks(s, t))

# TC: O(N + M), where N and M represent our two input strings
# SC: O(N+M) with stacks, O(1) with two pointers
