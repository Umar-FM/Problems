class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.append(0) #because we want to increase the len of the list as the first missing positive will be between 1-L+1
        n = len(nums)
        # remove all negative values and numbers > len of array. All remaining numbers are smaller than n(the len) 
        # which are in the possibility of the allowed domain
        for i in range(n):
            if nums[i] <0 or nums[i]>=n:nums[i]=0
        
        #the index of the array will be used as the hash key and the value will be the frequency of how many
        #times the number appears
        for i in range(n):
            #the reason for %n is that we want to preserve the original value, but also mark that number, so 
            #we just add n to it
            nums[nums[i]%n] += n
        
        #to retrieve first missing positive, it will be the first index which is less than n because no n was
        #added to it in the previous step because it was missing.
        for i in range(1,n): #skip the first value, because it just counts all the zeros which are meaningless.
            if nums[i]<n: return i
        
        return n #for the case where all were available then this is the last possible value