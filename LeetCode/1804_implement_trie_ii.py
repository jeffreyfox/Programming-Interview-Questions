# Track word count and prefix count in each trie node.
# Do not delete the nodes after removal to keep it simple.

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.word_count = 0
        self.prefix_count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        node.prefix_count += 1
        for c in word:
            idx = ord(c) - ord('a')
            if node.links[idx] is None:
                node.links[idx] = TrieNode()
            node = node.links[idx]
            node.prefix_count += 1
        node.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.links[idx] is None:
                return 0
            node = node.links[idx]
        return node.word_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if node.links[idx] is None:
                return 0
            node = node.links[idx]
        return node.prefix_count        

    def erase(self, word: str) -> None:
        node = self.root
        node.prefix_count -= 1
        for c in word:
            idx = ord(c) - ord('a')
            node = node.links[idx]
            node.prefix_count -= 1
        node.word_count -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)