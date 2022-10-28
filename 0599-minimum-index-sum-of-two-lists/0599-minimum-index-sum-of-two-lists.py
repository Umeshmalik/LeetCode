class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idxSum = 10e9
        ans = set()
        for i, l in enumerate(list1):
            if l in list2 and idxSum >= i+list2.index(l):
                if idxSum > i+list2.index(l): ans = set()
                idxSum = i+list2.index(l)
                ans.add(l)
                if list2.index(l) < len(list1) and i < len(list2) and list1[list2.index(l)] == list2[i]:
                    ans.add(list2[i])
        return list(ans)