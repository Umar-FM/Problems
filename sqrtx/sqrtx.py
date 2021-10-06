class Solution:
    def mySqrt(self, x: int) -> int:
        min=0
        
        while True:
            if min*min <= x and x < (min+1)*(min+1): return min
            
            min+=1
            