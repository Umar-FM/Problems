class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for n in nums:
            if n in d: d[n]+=1
            else: d[n] = 1
        ans=[]
        j=0
        for i in sorted(d, key=d.get, reverse=True):
            if j==k: break
            j+=1
            ans.append(i)
        return ans