from typing import List
from collections import defaultdict, deque

class Solution:
    def isWordLink(self, s, t):
            #we are given assumption that word lengths are equal
            allowed = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    allowed += 1
                    if allowed != 1:
                        return False
            return True
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        """
        represent the words as nodes in a graph and the connections between them as 
        possible combinations based on our rule (differing by at most one letter). So
        the words "hit" and "hot" would be connected in our graph. This would be an
        undirected graph that is possible cyclical. Our tast is to find the shortest
        path from beginWord (which we'd also add to our graph) to endWord
        """

        wGraph = defaultdict(list)
        # {word: set(words) that satisfy the one char difference}
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if self.isWordLink(wordList[i], wordList[j]):
                    wGraph[wordList[i]].append(wordList[j])
                    wGraph[wordList[j]].append(wordList[i])

        min_len = float('inf')

        start_words = []
        for word in wordList:
            if self.isWordLink(beginWord, word):
                start_words.append(word)

        #BFS on word graph
        for word in start_words:
            seen = set()
            q = deque()
            if beginWord == word:
                q.append((word, 1))
            else:
                q.append((word, 2))
            
            while q:
                popped, dist = q.popleft()
                seen.add(popped)
                if popped == endWord:
                    min_len = min(min_len, dist)
                
                for next_word in wGraph[popped]:
                    if next_word not in seen:
                        q.append((next_word, dist+1))

        return min_len if min_len != float('inf') else 00

    # TC: O(N^2 * M), where N is the number of words in wordList and M is the size of the strings
    # SC: O(N^2 * M)

    def ladderLengthOptimized(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patterns = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)

        #BFS on word graph

        seen = {beginWord}
        q = deque()
        q.append(beginWord)
        dist = 1
        while q:
            for i in range(len(q)):
                popped = q.popleft()
                seen.add(popped)
                if popped == endWord:
                    return dist
                
                for i in range(len(beginWord)):
                    pattern = popped[:i] + "*" + popped[i+1:]
                    for next_word in patterns[pattern]:
                        if next_word not in seen:
                            q.append(next_word)
                    
            dist += 1

        return 0
    
    # TC: O(M^2 * N)
    # SC: O(M^2 * N)

if __name__ == "__main__":
    sol = Solution()
    beginWord, endWord, wordList = "hit", "cog", ["hot","dot","dog","lot","log","cog"]
    print(sol.ladderLength(beginWord, endWord, wordList))
    print(sol.ladderLength(beginWord, endWord, wordList))