class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            numBottles,remainder = divmod(numBottles,numExchange)
            ans+= numBottles
            numBottles+=remainder
        return ans