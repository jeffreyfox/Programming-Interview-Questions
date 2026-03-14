class Solution:
    def isMatch(self, a, b) -> bool:
        if a == '(' and b == ')':
            return True
        if a == '[' and b == ']':
            return True
        if a == '{' and b == '}':
            return True
        return False

    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if not stack:
                    return False
                last = stack.pop()
                if not self.isMatch(last, c):
                    return False
            
        return len(stack) == 0