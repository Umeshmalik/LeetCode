class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        li = [[1], [1,1]]
        for i in range(3, numRows+1):
            new_li = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    new_li.append(1)
                else:
                    new_li.append(li[i-2][j] + li[i-2][j-1])
            li.append(new_li)
        return li