class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)==1: return True
        dic = {}
        for i,c in enumerate(order,1):
            dic[c]=i
        dic['#'] = 0
        maxL = len(max(words, key=len))
        #pad # to end of strings
        for i in range(len(words)):
            words[i]+= '#' * (maxL-len(words[i]))
        nums = [0]
        for s in words:
            val=0
            for c in s:
                val =val * 26+ dic[c]
            if val < nums[-1]: return False
            nums.append(val)
            
        return True
            