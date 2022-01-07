class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        dp[-1] = True
        
        for i in list(range(len(dp)))[::-1]:
            for word in wordDict:
                if i + len(word) <= len(s) and dp[i+len(word)] and s[i:i+len(word)]==word:
                    dp[i]=True
        return dp[0]