# TAGS: DP,string

# DP over prefix: dp[i] = True if ∃ j < i with dp[j] and s[j:i] in dict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        n = len(s)

        # dp[i] = True if the prefix s[:i] (of length i) is breakable
        dp = [False] * (n + 1)
        dp[0] = True  # base case: empty string

        for i in range(1, n+1):
            for j in range(i):
                # prefix s[:j] is breakable and s[j:i] is a word
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[n]