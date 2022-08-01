class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        if homePos[0] == startPos[0] and homePos[1] == startPos[1]:
            return 0
        su = 0
        if startPos[0] < homePos[0]:
            for i in range(startPos[0], homePos[0]):
                su += rowCosts[i+1]
        else:
            for i in range(startPos[0], homePos[0], -1):
                su += rowCosts[i-1]
        if startPos[1] < homePos[1]:
            for i in range(startPos[1], homePos[1]):
                su += colCosts[i+1]
        else:
            for i in range(startPos[1], homePos[1], -1):
                su += colCosts[i-1]
        return su