# TAGS: stack

# Scan left → right, building `num` and tracking `sign` and `result`.
# Do NOT compute immediately when seeing "a + b".
# Instead, delay evaluation until we hit the next operator (+ / -) or ')',
# which means the current number is complete.
# At that point, apply: result += sign * num.
#
# For '(':
#   - push current (result, sign) onto stack
#   - reset result and sign for the sub-expression
#
# For ')':
#   - finalize current number
#   - combine sub-expression with previous context:
#       result = prev_result + prev_sign * result
#
# Wrapping the whole string with () ensures the last number is always processed.

# Can combine the two stacks into one. First push num, then push sign (+1/-1).

class Solution:
    def calculate(self, s: str) -> int:
        s = f"({s})"
        num_stack = []
        sign_stack = []
        result = 0
        num = 0
        sign = 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                result += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                num_stack.append(result)
                sign_stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += sign * num
                sign = sign_stack.pop()
                result = num_stack.pop() + sign * result
                num = 0
                sign = 1
        return result