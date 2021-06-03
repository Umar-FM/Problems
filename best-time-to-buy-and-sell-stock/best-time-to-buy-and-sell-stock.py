class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #get edge cases
        if len(prices) < 2: return 0
        
        #if descending order return false
        
        
        
        #basic algo:
        #find min, split list into a before min and after min point
        #search after min point list for max
        #calculate difference, if max-min<=0, no max val and if before list empty return 0
        #repeat above for before min list
        #if new diff > prev diff, prev diff = new diff
        #repeat until no elements in before min list
        
        before_list = prices
        diff = 0
        
        
        
        min_val = min(prices)
        min_index = prices.index(min_val)
        max_val = max(prices[min_index:])
        diff = max_val - min_val if max_val - min_val >0 else 0
        before_list = prices[:min_index]
        while len(before_list) > 1:
            min_val = min(before_list)
            min_index = before_list.index(min_val)
            max_val = max(before_list[min_index:])
            new_diff = max_val - min_val if max_val - min_val >0 else 0
            diff = new_diff if new_diff > diff else diff
            before_list = before_list[:min_index]
            
        return diff
        