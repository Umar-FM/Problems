class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0: return 0
        res=[0 for i in range(n+1)]
        res[1] = 1
        
        for i in range(1,n//2+1):
            if i*2 <= n: res[i*2] = res[i]
            if i*2+1 <= n:res[i*2+1] = res[i] + res[i+1]
            
        return max(res)