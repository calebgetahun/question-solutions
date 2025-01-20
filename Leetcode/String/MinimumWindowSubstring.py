class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if not s or not t or m < n:
            return ""
        
        t_chars = dict()

        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1
        
        l, r = 0, 0
        ans_l, ans_r = 0, 0
        substring = dict()
        seen = 0
        min_substring_len = float('inf')
        dist_chars = len(t_chars.keys())

        while r < m:
            if s[r] in t_chars:
                substring[s[r]] = substring.get(s[r], 0) + 1

                if substring[s[r]] == t_chars[s[r]]:
                    seen += 1
            
            while seen == dist_chars:
                if (r-l+1) < min_substring_len:
                    min_substring_len = r-l+1
                    ans_l = l
                    ans_r = r

                if s[l] in substring:
                    substring[s[l]] -= 1
                    if substring[s[l]] < t_chars[s[l]]:
                        seen -= 1
                
                l += 1
            r += 1
        
        return "" if min_substring_len == float('inf') else s[ans_l:ans_r + 1]

if __name__ == "__main__":
    sol = Solution()
    s, t = "ADOBECODEBANC", "ABC"
    print(sol.minWindow(s, t))

# TC: O(M + N), where M is the length of the string s
# SC: O(M + N), where M, N are the lengths of s and t respectively