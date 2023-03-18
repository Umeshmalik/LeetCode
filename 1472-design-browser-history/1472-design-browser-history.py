class BrowserHistory:
    def __init__(self, homepage: str):
        self.start = homepage
        self.backwardStack = []
        self.forwardStack = []

    def visit(self, url: str) -> None:
        self.forwardStack = []
        self.backwardStack.append(url)

    def back(self, steps: int) -> str:
        if len(self.backwardStack) == 0:
            return self.start
        start = len(self.backwardStack) - steps if len(self.backwardStack) - steps > 0 else 0
        temp = self.backwardStack[start:len(self.backwardStack)]
        self.backwardStack = self.backwardStack[:start]
        self.forwardStack = temp + self.forwardStack
        return self.backwardStack[-1] if self.backwardStack else self.start

    def forward(self, steps: int) -> str:
        temp = self.forwardStack[:steps]
        self.forwardStack = self.forwardStack[steps:]
        self.backwardStack = self.backwardStack + temp
        return self.backwardStack[-1] if self.backwardStack else self.start

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)