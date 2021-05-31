class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2: return False
        
        for i in range(len(s)):
            if s[i] in ['(','[','{']: stack.append(s[i])
            else:
                if len(stack) == 0: return False
                if s[i] == ')':                    
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False    
        if len(stack) == 0: return True
        else: return False