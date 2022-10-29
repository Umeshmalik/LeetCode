class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.sum = 0

class MapSum:

    def __init__(self):
        self.root = {}
        

    def insert(self, key: str, val: int) -> None:
        self.root[key] = val
            

    def sum(self, prefix: str) -> int:
        ans = 0
        for key, val in self.root.items():
            isFound = True if len(key) >= len(prefix) else False
            for i in range(len(prefix)):
                if isFound and key[i] != prefix[i]:
                    isFound = False
                    break
            if isFound: ans += val
        return ans

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)