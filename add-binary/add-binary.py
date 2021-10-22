class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = len(a)
        nb = len(b)
        
        if na>nb: b = '0'*(na-nb) + b
        elif nb>na: a= '0'*(nb-na)+a
        c=0
        ans=''
        for i in range(len(a)-1,-1,-1):
            x = ord(a[i]) - ord('0')
            y = ord(b[i]) - ord('0')
            s = (x+y+c)%2
            c = (x+y+c)//2
            ans = str(s) + ans
        
        if c: ans = str(c) + ans
            
        return ans