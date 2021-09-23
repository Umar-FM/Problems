class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = [target-x for x in nums]
        for i in range(len(nums)):
            if nums[i] in temp and i != temp.index(nums[i]): return [i,temp.index(nums[i])]