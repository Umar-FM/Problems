class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        if len(s) == 1: return conv[s[0]]
        i=0
        num = 0
        while i< len(s):
            if i < len(s)-1 and conv[s[i]] < conv[s[i+1]]:
                num += conv[s[i+1]] - conv[s[i]]
                i+=1
            else: num += conv[s[i]]
            i+=1
        return num
        