class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''        # brute force: O(n^2) iterate every element (i) and match with every other element(j). Calculate area
        # by min(i,j)*(abs(i-j)). Return max area
        
        #area is maximized with difference btn h(i) and h(j) is minimized and difference between i & j is maximized
        #but also h(i and j) must be relatively high
        #min(abs(h(i)-h(j))) max(abs(i-j))
        
        #optimal strategy: Start from both ends, calculate area, move end thats lower closer to center, because not moving lower point will always be 'locking' in the area because the constraint will always be the lower line's height
        
        '''
        left = 0
        right = len(height)-1
        MAX = 0
        while(left!=right): #once they are equal, both points have met, no area. Going in reverse is just overlap
            if(height[left]>height[right]):
                MAX = max(MAX,(right-left)*height[right])
                right-=1
            else: #for the case both are equal, doesn't matter which one moves, the constraint still applies
                MAX = max(MAX,(right-left)*height[left])
                left+=1
        return MAX