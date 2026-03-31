# TAGS: string, two pointers

# Python two pointers solution
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        j = len(s) - 1
        while j >= 0:
            # Skip spaces so j points to the end of a word
            while j >= 0 and s[j] == " ":
                j -= 1
            
            # IMPORTANT: after skipping spaces, j may become -1 (e.g., all spaces),
            # so we must stop to avoid appending an empty string
            if j < 0:
                break

            i = j
            # Move i to the left of the current word
            while i >= 0 and s[i] != " ":
                i -= 1

            words.append(s[i+1:j+1])
            j = i

        return " ".join(words)

# Python cheating solution
class Solution:
    def reverseWords(self, s: str) -> str:
        parts = [p for p in s.split(" ") if p]
        parts = reversed(parts)
        return " ".join(parts)
