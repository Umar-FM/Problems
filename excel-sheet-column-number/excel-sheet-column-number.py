class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        hash = {}
        for i in range(65,91):
            hash[chr(i)] = i - 64

        sum = 0
        base = 0

        for i in range(len(columnTitle)-1,-1,-1):
            sum += hash[columnTitle[i]]*26**base
            base+=1

        return sum