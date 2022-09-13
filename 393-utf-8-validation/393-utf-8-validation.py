class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def ones(n):
            for i, num in enumerate([128, 192, 224, 240, 248, 256]):
                if n < num: return i
        
        i = 0
        while i < len(data):
            curr = ones(data[i])
            if curr > 4 or curr == 1: return False
            
            if curr == 4 and i + curr - 1 >= len(data):
                return False
            elif curr == 4 and i + 3 < len(data):
                if ones(data[i+1]) + ones(data[i+2]) + ones(data[i+3]) != 3: return False
                i += 3
            elif curr == 3 and i + 2 >= len(data):
                return False
            elif curr == 3 and i + 2 < len(data):
                if ones(data[i+1]) + ones(data[i+2]) != 2: return False
                i += 2
            elif curr == 2 and i + 1 >= len(data):
                return False
            elif curr == 2 and i + 1 < len(data):
                if ones(data[i+1]) != 1: return False
                i += 1
            i += 1
        return True