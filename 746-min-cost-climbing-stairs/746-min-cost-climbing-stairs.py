class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr, last = cost[1], cost[0]
        for i in range(2, len(cost)):
            curr, last = cost[i] + min(last, curr), curr
        return min(curr, last)