class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                ans += 1
        return ans