
from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(b + a)
                elif i == "-":
                    stack.append(b - a)
                elif i == "*":
                    stack.append(b * a)
                else:
                    r = ceil(b/a) if (b / a) < 0 else floor(b/a)
                    stack.append(r)
            else:
                stack.append(int(i))
        return stack.pop()