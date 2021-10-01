class Solution:
    def maxScore(self, cardPoints: List[int], k: int,memo={}) -> int:
        maximum = 0
        l=0
        r=len(cardPoints)-1-k
        
        s = sum(cardPoints[:l])+sum(cardPoints[r+1:])
        maximum = max(maximum,s)
        for i in range(k):
            l+=1
            r+=1
            s=s+cardPoints[l-1]-cardPoints[r]
            maximum = max(maximum,s)
            
            
        
        return maximum
        