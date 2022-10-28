class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in strs:
            word = "".join(sorted(i))
            if word in mp:
                mp[word].append(i)
            else:
                mp[word] = [i]
        return list(mp.values())