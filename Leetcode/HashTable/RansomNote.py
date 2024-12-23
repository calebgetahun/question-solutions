"""
Ransom Note

https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = dict()
        for char in magazine:
            mag[char] = mag.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in mag or mag[char] < 1:
                return False
            mag[char] -= 1
        return True