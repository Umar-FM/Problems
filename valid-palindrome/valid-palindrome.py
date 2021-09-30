class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphaNum = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        l=0
        r=len(s)-1
        
        while l<r:
            while s[l] not in alphaNum: 
                l+=1
                if l > len(s)-1: return True
            while s[r] not in alphaNum:
                r-=1
                if r < 0: return True
            if s[l] != s[r]: return False
            l+=1
            r-=1
            
                
        return True