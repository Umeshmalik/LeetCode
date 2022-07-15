class Solution:
    max_area = 0
    curr_max = 0 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.curr_max = 0
                    self.getMax(i, j, grid)
        return self.max_area
    
    def getMax(self, a, b, grid):
        if  a < 0 or b < 0 or a >= len(grid) or b >= len(grid[0]) or grid[a][b] == 0:
            return
        grid[a][b] = 0
        self.curr_max += 1
        self.max_area = max(self.max_area, self.curr_max)
        self.getMax(a-1, b, grid)
        self.getMax(a, b-1, grid)
        self.getMax(a, b+1, grid)
        self.getMax(a+1, b, grid)
        return