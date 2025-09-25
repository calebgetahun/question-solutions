class TrieNode:
    def __init__(self):
        self.chars = [None] * 26 #one for each letter
        self.end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.chars[index]:
                curr.chars[index] = TrieNode()

            curr = curr.chars[index]
        curr.end_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.chars[index]:
                return False
            curr = curr.chars[index]

        return curr.end_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not curr.chars[index]:
                return False
            curr = curr.chars[index]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))

# TC: O(N) for all operations, where N is the number of characters in the particular string
# SC: O(N), could be considered O(1) since we have a fixed number of characters

# Leetcode question: Implement Trie