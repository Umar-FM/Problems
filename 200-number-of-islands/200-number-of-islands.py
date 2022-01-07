class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans=0
        
        def recurse(r,c):
            if (r,c) in visited or r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c] != "1": return
            visited.add((r,c))
            
            recurse(r+1,c)
            recurse(r-1,c)
            recurse(r,c+1)
            recurse(r,c-1)
        
        
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    ans+=1
                    recurse(r,c)
                    
        return ans
                    