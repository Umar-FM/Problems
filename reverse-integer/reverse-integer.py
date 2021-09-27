class Solution:
    def reverse(self, x: int) -> int:
        ans = self.myReverse(abs(x))
        if x<0: ans *= -1
        if ans > 2**31-1 or ans < -2**31: return 0
        return ans
    
    def myReverse(self,x,y=0):
        if x == 0: return y
        y = y*10 + x%10
        return self.myReverse(int(x/10),y)