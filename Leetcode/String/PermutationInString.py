class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        for i in range(m):
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == s2_count:
            return True
        
        for j in range(m, n):
            s2_count[ord(s2[j-m]) - ord('a')] -= 1
            s2_count[ord(s2[j]) - ord('a')] += 1

            if s1_count == s2_count:
                return True
        
        return False

if __name__ == "__main__":
    sol = Solution()
    s = "ab"
    s_1 = "eidbaoo"
    s_2 = "abc"
    s_3 = "eibadacmb"

    print(sol.checkInclusion(s, s_1))
    print(sol.checkInclusion(s_2, s_3))

# TC: O(M + N) where M and N are the length of string s1 and s2
# SC: O(1) since our char arrays are of constant space