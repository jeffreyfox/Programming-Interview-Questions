# TAGS: array

# Track the latest position of each target word while scanning once, and update the minimum distance whenever the other word has already been seen.

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = idx2 = -1
        best = float("inf")

        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i
                if idx2 != -1:
                    best = min(best, idx1 - idx2)
            elif word == word2:
                idx2 = i
                if idx1 != -1:
                    best = min(best, idx2 - idx1)

        return best