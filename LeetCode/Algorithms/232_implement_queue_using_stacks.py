# Use two stacks: in_stack for pushes and out_stack for pops/peeks.

# When pushing, simply push the element onto in_stack. When popping or peeking, if out_stack is empty, move all elements from in_stack to out_stack, which reverses their order so the oldest element is on top.

# Each element is moved at most once between stacks, so all operations run in amortized O(1) time.

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
