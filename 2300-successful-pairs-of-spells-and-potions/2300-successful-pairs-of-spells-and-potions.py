class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        for i in spells:
            start = 0
            end = len(potions) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if potions[mid] * i >= success: end = mid - 1
                else: start = mid + 1
            ans.append(len(potions) - start)
        return ans