class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.index += 1

        if self.index < len(self.pages):
            self.pages[self.index] = url
            self.pages = self.pages[:self.index + 1]
        else:
            self.pages.append(url)

    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)
        return self.pages[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(len(self.pages) - 1, self.index + steps)
        return self.pages[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)