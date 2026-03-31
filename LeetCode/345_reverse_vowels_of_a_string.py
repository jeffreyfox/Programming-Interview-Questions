# TAGS: string,two pointers

# Two pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(s: str):
            return s in 'aeiouAEIOU'

        result = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not is_vowel(result[i]):
                i += 1
            while i < j and not is_vowel(result[j]):
                j -= 1
            
            if i >= j:
                break
            
            result[i], result[j] = result[j], result[i]

            i += 1
            j -= 1
        return "".join(result)