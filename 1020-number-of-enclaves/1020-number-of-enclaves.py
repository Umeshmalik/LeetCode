class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def reach(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0: return
            grid[x][y] = 0
            mt = [[0, -1], [-1, 0], [1, 0], [0, 1]]
            for i, j in mt: reach(x+i, y+j)
        
        for i in range(len(grid)):
            reach(i, 0)
            reach(i, len(grid[0]) - 1)
        
        for i in range(len(grid[0])):
            reach(0, i)
            reach(len(grid) - 1, i)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])): count += grid[i][j]
        return count