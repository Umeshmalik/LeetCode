class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfString = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        rt = self.root
        for i in word:
            if i not in rt.children:
                rt.children[i] = TrieNode()
            rt = rt.children[i]
        rt.isEndOfString = True

    def search(self, word: str) -> bool:
        rt = self.root
        for i in word:
            if i not in rt.children:
                return False
            rt = rt.children[i]
        return True if rt.isEndOfString else False

    def startsWith(self, prefix: str) -> bool:
        rt = self.root
        for i in prefix:
            if i not in rt.children:
                return False
            rt = rt.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)