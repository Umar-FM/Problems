class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    t = 4
                    if r+1 < len(grid): 
                        if grid[r+1][c] == 1: t-=1
                    if r-1 >=0: 
                        if grid[r-1][c] == 1: t-=1
                    if c+1 < len(grid[0]): 
                        if grid[r][c+1] == 1: t-=1
                    if c-1 >= 0: 
                        if grid[r][c-1] == 1: t-=1
                    p+=t
        
        return p
        