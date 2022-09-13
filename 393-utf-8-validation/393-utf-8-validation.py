class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def ones(num):
            bn = bin(num)[2:]
            rem = 8 - len(bn)
            bn = "0" * rem + bn
            curr = 0
            for k in bn:
                if k == '1':
                    curr += 1
                else:
                    break
            return curr
        last = 0
        i = 0
        while i < len(data):
            curr = ones(data[i])
            if curr > 4 or curr == 1: return False
            if curr == 4 and i + 3 >= len(data):
                return False
            elif curr == 4 and i + 3 < len(data):
                ans = ones(data[i+1]) + ones(data[i+2]) + ones(data[i+3])
                if ans != 3: return False
                i += 3
            elif curr == 3 and i + 2 >= len(data):
                return False
            elif curr == 3 and i + 2 < len(data):
                ans = ones(data[i+1]) + ones(data[i+2])
                if ans != 2: return False
                i += 2
            elif curr == 2 and i + 1 >= len(data):
                return False
            elif curr == 2 and i + 1 < len(data):
                ans = ones(data[i+1])
                if ans != 1: return False
                i += 1
            i += 1
        return True