class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        arr = []
        sm = 0
        for n in nums:
            if n&1 == 0:
                sm += n
        for num, idx in queries:
            nums[idx] += num
            if nums[idx]&1 == 0 and (nums[idx] - num)&1 != 0:
                sm += nums[idx]
            elif (nums[idx] - num)&1 == 0 and nums[idx]&1 == 0:
                sm += num
            elif (nums[idx] - num)&1 == 0 and nums[idx]&1 != 0:
                sm -= nums[idx] - num
            arr.append(sm)
        return arr