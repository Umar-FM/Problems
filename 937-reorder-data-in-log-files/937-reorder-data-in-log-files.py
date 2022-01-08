class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            if log.split(" ")[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key= lambda x: x.split(" ")[0]) #first sort letters by numbers so same text can be sorted
        letters.sort(key= lambda x: x.split(" ")[1:]) #next sort by the text itself
        
        return letters + digits
        