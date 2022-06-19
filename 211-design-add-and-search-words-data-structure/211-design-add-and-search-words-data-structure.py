class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfString = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        rt = self.root
        for i in word:
            if i not in rt.children:
                rt.children[i] = TrieNode()
            rt = rt.children[i]
        rt.isEndOfString = True

    def search(self, word: str) -> bool:
        rt = self.root
        def dfs(rt, word):
            if len(word) == 0:
                return rt.isEndOfString
            if word[0] == '.':
                for i in rt.children:
                    if dfs(rt.children[i], word[1:]):
                        return True
                return False
            if word[0] in rt.children:
                return dfs(rt.children[word[0]], word[1:])
            return False
        return dfs(rt, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)