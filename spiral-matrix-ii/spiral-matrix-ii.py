class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited=set()
        ans=[[0 for i in range(n)] for j in range(n)]
        i=0
        j=0
        x=1
        rotation = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
        r=0
        while x<(n*n+1):
            ans[i][j]=x
            visited.add(str([i,j]))
            x+=1
            oldR=r
            while True:
                qi,qj=rotation[r%4]
                qi,qj=qi+i,qj+j
                if 0<=qi<n and 0<=qj<n and str([qi,qj]) not in visited:
                    i,j=qi,qj
                    break
                else:
                    r+=1
                if r-oldR >=4: break
            
            
            
            
            
        return ans