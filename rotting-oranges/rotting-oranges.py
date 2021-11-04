class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        q=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2: q.append((i,j))
        
        while q:
            rotten=False
            for x in range(len(q)):
                i,j=q.pop(0)
                
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append((i+1,j))
                    rotten=True
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append((i-1,j))
                    rotten=True
                if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q.append((i,j+1))
                    rotten=True
                if j-1 >=0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    q.append((i,j-1))
                    rotten=True
            if rotten: count+=1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1: return -1
        
        return count