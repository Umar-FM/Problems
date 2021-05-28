class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #negative value is not palindrome
        if x<0:
            return False
        
        list1 = []
        
        "convert to list"
        while x >= 1:
            list2 = [x%10]
            list1 = list1 + list2
            x = int(x/10)
    
        
        "Check palindrome"
        for i in range(int(len(list1)/2)):
            if list1[i] != list1[len(list1)-1-i]:
                return False
        else:
            return True