class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic.keys(): dic[i] += 1
            else: dic[i] = 1
            
        return list(dic.keys())[list(dic.values()).index(1)]
        