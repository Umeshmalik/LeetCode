class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for i in arr:
            if i in ['.', ""]:
                continue
            elif i == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)