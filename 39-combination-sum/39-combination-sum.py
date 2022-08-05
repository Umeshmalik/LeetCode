class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(index, rem_target, array):
            if rem_target < 0: return
            if rem_target == 0:
                ans.append(array[:])
                return
            for i in range(index, len(candidates)):
                if candidates[i] > rem_target: continue 
                array.append(candidates[i])
                helper(i, rem_target - candidates[i], array)
                array.pop()
            return
        helper(0, target, [])
        return ans