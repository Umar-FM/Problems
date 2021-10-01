class Solution:
    def validPalindrome(self, s: str,delete=True) -> bool:
        if len(s)<=1: return True
        if s[0] == s[-1]:
            return self.validPalindrome(s[1:-1],delete)
        else:
            if delete:
                delete=False
                return self.validPalindrome(s[1:],delete) or self.validPalindrome(s[:-1],delete)
            else: return False