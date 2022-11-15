from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr1 = Counter(s)
        arr2 = Counter(t)
        for i in arr2.keys():
            if arr1[i] < arr2[i]: return i
        return " "