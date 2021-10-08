class Solution:

    

    def numberToWords(self, num: int) -> str:
        s=""
        if num==0:return "Zero"
        billion = int(num/1000000000)
        million = int(num/1000000)
        thousand = int(num/1000)

        if billion:
            b=self.toEng(billion%1000)
            if len(b):
                s += b + " Billion"

            num %= 1000000000
            if not num: return s
        if million:
            m=self.toEng(million%1000)
            if len(m):
                if len(s): s+= " "
                s+= m + " Million"
            num %= 1000000
            if not num: return s
        if thousand:
            t = self.toEng(thousand%1000)
            if len(t):
                if len(s): s+= " "
                s+= t + " Thousand"
            num %= 1000
            if not num: return s
        if num != 0:
            if len(s): s+= " "
            s+= self.toEng(num%1000)
        return s





    def toEng(self, num):
        ones = {
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine"     
        }

        teens = {
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen",
        }

        tens = {
            1:"Ten",
            2:"Twenty",
            3:"Thirty",
            4:"Forty",
            5:"Fifty",
            6:"Sixty",
            7:"Seventy",
            8:"Eighty",
            9:"Ninety",
        }
        s=""
        if int(num/100): 
            s+= ones[int(num/100)] + " Hundred"
            num = num%100
        if num >=20 or num == 10:
            if len(s): s+= " "
            s+=tens[int(num/10)]
            num=num%10
        elif num >=11 and num <= 19:
            if len(s): s+= " "
            s+= teens[num]
            return s
        if num != 0:
            if len(s): s+= " "
            s+= ones[num]
        return s