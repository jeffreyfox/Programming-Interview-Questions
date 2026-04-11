# TAGS: DP,string

# Build all valid sentences for prefixes of s.
# ways[i] contains all decompositions of s[:i].
# For each split j < i, if s[j:i] is in dict, append it to each sentence in ways[j].

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)

        # ways[i] lists the ways to break the prefix s[:i]
        ways = [[] for _ in range(n + 1)]
        ways[0] = [""]
        
        for i in range(1, n + 1):
            for j in range(i):
                word = s[j:i]
                if word not in word_set:
                    continue
                for prev in ways[j]:
                    if prev == "":
                        ways[i].append(word)
                    else:
                        ways[i].append(prev + " " + word)
        return ways[n]
