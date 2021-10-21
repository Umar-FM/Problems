class Solution:
    
    has = {
        'I':1,
        'V':5,
        "X":10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
    def intToRoman(self, num: int) -> str:
        ls = []
        for i in range(len(str(num))-1,-1,-1):
            
            ls.append(self.getDigit((num//10**i)*10**i))
            num%=10**i
        for i in range(len(ls)):
            if ls[i]=='IIII': ls[i] = 'IV'
            if ls[i]=='VIIII': ls[i] = 'IX'
            if ls[i]=='XXXX': ls[i] = 'XL'
            if ls[i]=='LXXXX': ls[i] = 'XC'
            if ls[i]=='CCCC': ls[i] = 'CD'
            if ls[i]=='DCCCC': ls[i] = 'CM'

        return ''.join(ls)
        
            
            
    def getDigit(self,num):
        s = ''
        vals = list(self.has.values())
        vals.reverse()
        for i in vals:
            div = num//i
            if div < 5 and div >= 1:
                s += div*list(self.has.keys())[list(self.has.values()).index(i)]
                num%=i
                if num==0: break
        return s