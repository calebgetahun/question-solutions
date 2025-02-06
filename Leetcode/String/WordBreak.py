from typing import List

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.chars = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not curr.chars[index]:
                new_char = TrieNode()
                curr.chars[index] = new_char
                curr = new_char
            else:
                curr = curr.chars[index]
        
        curr.isWord = True
    
    def isWord(self, word):
        curr = self.root

        for char in word:
            index = ord(char) - ord('a')
            if not curr.chars[index]:
                return False
            else:
                curr = curr.chars[index]

        if curr.isWord:
            return True
        else:
            return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                
                if i == len(word)-1 or dp[i-len(word)]:
                    if s[i-len(word)+1:i+1] == word:
                        dp[i] = True

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    s = "catsandog"
    words = ["cats","dog","sand","and","cat"]
    s_1 = "goalspecial"
    words_1 = ["go", "goal", "goals", "special"]
    print(sol.wordBreak(s, words))
    print(sol.wordBreak(s_1, words_1))

# TC: O(N*M*k), where N is the total number of characters in s, M is the number of words in wordDict, and k is the time it takes to take a substring for our dp table check
# SC: O(N), for our dp table