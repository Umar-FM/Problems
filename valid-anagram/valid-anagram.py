class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c in s:
            if c in dic: dic[c]+=1
            else: dic[c] = 1
        
        for c in t:
            if c not in dic: return False
            dic[c]-=1
            
        for k in list(dic.keys()):
            if dic[k] != 0: return False
            
        return True