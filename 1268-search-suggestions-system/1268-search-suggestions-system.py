class TrieNode:
    def __init__(self):
        self.children = {}
        self.data = []

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        rt = self.root
        for i in word:
            if i not in rt.children:
                rt.children[i] = TrieNode()
            if(len(rt.data)<3):
                rt.data.append(word)
            rt = rt.children[i]
        rt.data.append(word)
                

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        dict = Trie()
        for i in products:
            dict.insert(i)
        arr = []
        rt = dict.root
        for i in searchWord:
            if i in rt.children:
                rt = rt.children[i]
                arr.append(rt.data)
            else:
                arr.append([])
                rt.children = []
        return arr