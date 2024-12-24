class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_counts = dict()
        
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        for charT in t:
            if charT not in char_counts:
                return False
            if char_counts[charT] == 0:
                return False
            char_counts[charT] -= 1
        
        return True

if __name__ == "__main__":
    sol = Solution()
    s_1 = "anagram"
    s_2 = "nagaram"

    s_3 = "rat"
    s_4 = "car"
    print(sol.isAnagram(s_1, s_2))
    print(sol.isAnagram(s_3, s_4))


# TC: O(s + t)
# SC: O(26) -> O(1) since each letter contains lowercase English letters and our hashmap will store at most 26 keys, not strictly depending on the size of s