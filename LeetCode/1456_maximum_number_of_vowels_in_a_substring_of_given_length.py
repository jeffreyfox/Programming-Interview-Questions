# TAGS: sliding window,string

# Sliding window using right index i:
# - current window is s[i-k+1 : i+1]
# - s[i] enters the window
# - s[i-k] leaves the window
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        cnt = sum(1 for c in s[:k] if c in "aeiou")
        best = cnt
        for i in range(k, len(s)):
            if s[i] in "aeiou":
                cnt += 1
            if s[i-k] in "aeiou":
                cnt -= 1
            best = max(best, cnt)
        return best