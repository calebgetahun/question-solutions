class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if curr.children[ind]:
                curr = curr.children[ind]
            else:
                new_node = TrieNode()
                curr.children[ind] = new_node
                curr = new_node
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            ind = ord(char) - ord('a')
            if curr.children[ind]:
                curr = curr.children[ind]
            else:
                return False
        if curr.is_word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            ind = ord(char) - ord('a')
            if curr.children[ind]:
                curr = curr.children[ind]
            else:
                return False
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