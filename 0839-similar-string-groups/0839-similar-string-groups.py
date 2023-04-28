class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilarStr (st, st2):
            str1, str2 = '', ''
            for j in range(len(st)):
                if st[j] != st2[j]:
                    if not str1:
                        str1 = st2[j]
                        str2 = st[j]
                    elif str1 != st[j] or str2 != st2[j]: return False
            return True

        visited = set()
        def helper(index):
            visited.add(index);
            for j in range(len(strs)):
                if j not in visited and isSimilarStr(strs[index], strs[j]): helper(j)

        count = 0
        for j in range(len(strs)):
            if j in visited: continue
            helper(j)
            count += 1
        return count