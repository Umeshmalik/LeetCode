class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        ans = []
        if len(s1) > len(s2): return ans
        arr = [0] * 26
        for i in s1: arr[ord(i)-97] += 1
        arr2 = [0] * 26
        for i in range(0, len(s1)): arr2[ord(s2[i])-97] += 1
        if arr == arr2: ans.append(0)
        for i in range(len(s1), len(s2)):
            arr2[ord(s2[i-len(s1)])-97] -= 1
            arr2[ord(s2[i])-97] += 1
            if arr == arr2: ans.append(i-len(s1)+1)
        return ans