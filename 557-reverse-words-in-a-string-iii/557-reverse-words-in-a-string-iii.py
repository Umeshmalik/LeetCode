class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        for i, n in enumerate(arr):
            t = n[::-1]
            arr[i] = t
        return " ".join(arr)