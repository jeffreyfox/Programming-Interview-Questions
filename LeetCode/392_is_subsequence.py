# TAGS: two pointers,string

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s):
            # find a character in t matching s[i]
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j == len(t):
                return False
            
            i += 1
            j += 1
        return True