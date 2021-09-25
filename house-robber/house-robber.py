class Solution:
    def rob(self, nums: List[int],memo={}) -> int:
        if len(nums) == 0: return 0
        if str(nums) in memo: return memo[str(nums)]
        if len(nums) == 1:
            memo[str(nums)] = nums[0]+self.rob(nums[2:],memo)
            return memo[str(nums)]
        memo[str(nums)] = max(nums[0]+self.rob(nums[2:],memo),nums[1]+self.rob(nums[3:],memo))
        return memo[str(nums)]