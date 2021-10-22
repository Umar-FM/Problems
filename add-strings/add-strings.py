class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c=0
        if len(num1) < len(num2): num1='0'*abs(len(num1)-len(num2))+num1
        elif len(num2) < len(num1): num2='0'*abs(len(num1)-len(num2))+num2
        ans=""
        for i in range(len(num1)-1,-1,-1):
            a = ord(num1[i])-ord('0')
            b = ord(num2[i])-ord('0')
            s=(a+b+c)%10
            c = (a+b+c)//10
            ans = str(s) + ans
        if c: ans=str(c)+ans
        return ans