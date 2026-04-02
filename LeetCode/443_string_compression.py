# TAGS: array,two pointers

# Two pointers
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        k = 0
        while i < n:
            # j will point to the new character (different) or end
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            count = j - i
            chars[k] = chars[i]
            k += 1
            # render the count
            if count > 1:
                for c in str(count):
                    chars[k] = c
                    k += 1
            i = j

        return k