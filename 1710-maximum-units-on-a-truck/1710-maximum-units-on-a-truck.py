class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        ans = 0
        
        for box in boxTypes:
            if box[0] <= truckSize:
                ans+= box[0]*box[1]
                truckSize-=box[0]
            else:
                ans+= box[1]*truckSize
                break
        
        return ans
            