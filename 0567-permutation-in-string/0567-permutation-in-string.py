class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        arr = [0] * 26
        for i in s1: arr[ord(i)-97] += 1
        arr2 = [0] * 26
        for i in range(0, len(s1)): arr2[ord(s2[i])-97] += 1
        if arr == arr2: return True
        for i in range(len(s1), len(s2)):
            arr2[ord(s2[i-len(s1)])-97] -= 1
            arr2[ord(s2[i])-97] += 1
            if arr == arr2: return True
        return False