class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k=0
        currentString=""
        
        for c in s:
            if c == '[': #start of a new stack item, so save what we have on the top of stack
                stack.append((currentString,k))
                k=0
                currentString=""
                
                
            elif c == ']': #end of stack, parse into string
                previousString,previousK=stack.pop(-1)
                currentString = previousString+previousK*currentString
                
            elif c.isdigit():
                k=k*10+int(c)
            else:
                currentString+=c
        return currentString   