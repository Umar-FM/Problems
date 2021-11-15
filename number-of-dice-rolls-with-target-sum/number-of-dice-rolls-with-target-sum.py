class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int,memo={}) -> int:
        if (d,f,target) in memo: return memo[(d,f,target)]
        
        if d==1: 
            if target > f or target < 1: 
                memo[(d,f,target)] = 0
                return 0
            memo[(d,f,target)] = 1
            return 1
        
        ans=0
        for i in range(1,f+1):
            ans += self.numRollsToTarget(d-1,f,target-i)
        
        memo[(d,f,target)] = ans%(10**9+7)
        return memo[(d,f,target)]