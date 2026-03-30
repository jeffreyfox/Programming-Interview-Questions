# string, two pointers

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []
        for k in range(len(word1) + len(word2)):
            if i == len(word1):
                result.append(word2[j])
                j += 1
            elif j == len(word2):
                result.append(word1[i])
                i += 1
            elif k % 2 == 0:
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1
        return "".join(result) 
        
# A simpler solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)