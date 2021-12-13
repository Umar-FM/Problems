class Solution:
    def minDeletions(self, s: str) -> int:
        d={}
        for c in s:
            if c in d: d[c]+=1
            else: d[c] =1
        
        vals = list(d.values())
        vals.sort()
        ans=0
        for i in range(len(vals)-1,0,-1):
            while vals[i-1] >= vals[i] and vals[i-1]>0:
                ans+=1
                vals[i-1]-=1
        return ans