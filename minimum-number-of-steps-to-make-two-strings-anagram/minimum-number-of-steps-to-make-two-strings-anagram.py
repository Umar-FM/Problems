class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds = {}
        for c in s:
            if c in ds: ds[c] +=1
            else: ds[c] =1
        res=0
        for c in t:
            if not c in ds: res+=1
            elif ds[c] > 0: ds[c] -=1
            else: res+=1
        return res