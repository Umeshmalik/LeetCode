class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        arr = []
        for j in range(len(strs[0])):
            s = []
            for i in range(len(strs)):
                s.append(strs[i][j])
            arr.append("".join(s))
        ans = 0
        for i in arr:
            for j in range(1, len(i)):
                if i[j-1] > i[j]:
                    ans += 1
                    break
        return ans