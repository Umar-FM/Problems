class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        gm=nums[0]
        prev_max = nums[0]
        prev_min = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            curr_max = max(curr,curr*prev_max,curr*prev_min)
            curr_min = min(curr,curr*prev_max,curr*prev_min)
            gm=max(gm,curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return gm