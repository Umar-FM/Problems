class Solution:
    def reverseWords(self, s: str) -> str:
        wordStack = []
        i=0
        while i < len(s):
            word = ""
            
            while i < len(s) and s[i] != " ":
                word += s[i]
                i+=1
            else: i+=1
            if word != "": wordStack.append(word)
            
            
        res = ""
        for i in range(len(wordStack)):
            res += wordStack.pop() + " "
            
        res = res.strip()
        
        return res