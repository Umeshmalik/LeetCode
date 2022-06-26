class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints)
        res = len(cardPoints) - k
        currSum = 0
        for i in range(res):
            currSum += cardPoints[i]
        maxSum = totalSum - currSum
        for i in range(res, len(cardPoints)):
            currSum = currSum - cardPoints[i - res] + cardPoints[i]
            maxSum = max(maxSum, totalSum - currSum)
        return maxSum