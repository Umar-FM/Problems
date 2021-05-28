class Solution(object):
    
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    
    def getNum(self,s):
        index=0
        if len(s)==0: return "0"
        if s[index] not in digits:
            return "0"
        
        while s[index] in digits:
            if index == len(s) - 1:
                break
            index = index + 1
        
        return(s[:index+1])
    
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s=s.lstrip()
        if len(s)==0: return 0
        
        
    
        if s[0] == '-': 
            pos = False
            num = self.getNum(s[1:])
        elif s[0] == '+': 
            pos = True
            num = self.getNum(s[1:])
        elif s[0] in digits:
            pos = True
            num = self.getNum(s)   
        else:
            return 0
        
        if num[-1] not in digits:
            num = num[:-1]
        
        for i in range(len(num)):
            if num[i] not in digits:
                return 0
        
        
        num = int(num)
        if not(pos):
            num = num * -1
            
        
        if num < -2**31: num = -2**31
        if num > (2**31 - 1): num = 2**31 - 1
            
        return num
        
    
            
        
        