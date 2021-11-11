class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[False for i in range(len(nums))]
        dp[0] = True
        
        for i in range(len(dp)):
            if dp[i]:
                k=nums[i]
                for j in range(1,k+1):
                    if i+j < len(dp): dp[i+j] = True
                if dp[-1]: return True
        
        return dp[-1]
        