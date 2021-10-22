class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 #0 XOR with anything is that thing
        for i in nums:
            res ^= i
        
        return res
        