class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        arr = [i for i in s]
        for i in range(len(shifts) - 2 , -1, -1):
            shifts[i] += shifts[i+1]
        for i in range(len(arr)):
            arr[i] =  chr((((ord(arr[i]) + shifts[i]) - ord('a'))%26) + ord('a')) 
        return "".join(arr)