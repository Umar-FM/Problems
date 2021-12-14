class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1: return [0]
        ans=[]
        last = n//2
        for i in range(last,0,-1):
            ans.append(-1*i)
        if n%2: ans.append(0)
        for i in range(1,last+1):
            ans.append(i)
        return ans