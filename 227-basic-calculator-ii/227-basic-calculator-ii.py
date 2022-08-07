class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        opr = []
        i = 0
        s = s.replace(" ", "")
        while i < len(s):
            n = ""
            while i < len(s) and s[i].isdigit():
                n += s[i]
                i += 1
            if n:
                if len(opr) > 0 and opr[-1] == '*':
                    n = int(n) * int(stack.pop())
                    opr.pop()
                elif len(opr) > 0 and opr[-1] == '/':
                    n = int(stack.pop()) // int(n)
                    opr.pop()
                if len(stack) == 0:
                    stack.append(int(n))
                    if i < len(s):
                        opr.append(s[i])
                else:
                    stack.append(int(n))
                    if i < len(s):
                        opr.append(s[i])
                i += 1
        ans = stack[0]
        for i in range(1, len(stack)):
            if opr[i-1] == '+':
                ans += stack[i]
            elif opr[i-1] == '-':
                ans -= stack[i]
        return ans