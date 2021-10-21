class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        
        for i in range(len(nums)):
            if i == len(nums)-1:return True
            if nums[i+1]>nums[i]: 
                increasing = True
                break
            elif nums[i+1] < nums[i]: 
                increasing = False
                break
        
        if increasing:
            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]: return False
        else:
            for i in range(1,len(nums)):
                if nums[i] > nums[i-1]: return False
        return True