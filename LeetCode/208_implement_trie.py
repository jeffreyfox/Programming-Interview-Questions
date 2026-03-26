class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_key = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.links[idx] is None:
                node.links[idx] = TrieNode()
            node = node.links[idx]
        node.is_key = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.links[idx] is None:
                return False
            node = node.links[idx]
        return node.is_key

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if node.links[idx] is None:
                return False
            node = node.links[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)