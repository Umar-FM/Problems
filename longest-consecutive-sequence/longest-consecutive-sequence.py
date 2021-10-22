class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):return 0
        longest,streak = 0,0
        nums = set(nums)
        
        for n in nums:
            if n-1 not in nums:
                #c = n
                streak = 1
                
                while n+1 in nums:
                    streak+=1
                    n+=1
                
            longest=  max(longest,streak)
            
        return longest