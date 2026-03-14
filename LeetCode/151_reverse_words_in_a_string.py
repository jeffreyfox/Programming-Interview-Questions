# Python cheating solution
class Solution:
    def reverseWords(self, s: str) -> str:
        parts = [p for p in s.split(" ") if p]
        parts = reversed(parts)
        return " ".join(parts)
