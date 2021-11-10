class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxStreak=0
        for i in nums:
            if i-1 not in nums:
                streak=0
                curr=i
                while curr in nums:
                    curr+=1
                    streak+=1
                maxStreak=max(streak,maxStreak)
        return maxStreak