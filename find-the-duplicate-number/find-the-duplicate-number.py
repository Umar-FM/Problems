class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #binary search of array [1,n] because each element will have exactly itself elems >= itself, except the duplicate
        l=1
        r=len(nums)-1
        
        while l<=r:
            c = (l+r)//2
            
            count = sum(num<=c for num in nums) #returns a list of true,false values THIS MAY BE MORE THAN CONSTANT SPACE
            if count>c:
                ans = c
                r = c-1
            else:
                l=c+1
                
        return ans
        