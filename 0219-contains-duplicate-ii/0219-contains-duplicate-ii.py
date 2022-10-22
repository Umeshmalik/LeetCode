class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i, n in enumerate(nums):
            if n in mp.keys() and abs(mp[n] - i) <= k: return True
            mp[n] = i
        return False