class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.forward_pages = []

    def visit(self, url: str) -> None:
        self.pages.append(url)
        self.forward_pages = []

    def back(self, steps: int) -> str:
        n = min(steps, len(self.pages) - 1)
        for _ in range(n):
            self.forward_pages.append(self.pages.pop())

        return self.pages[-1]

    def forward(self, steps: int) -> str:
        n = min(steps, len(self.forward_pages))
        for _ in range(n):
            self.pages.append(self.forward_pages.pop())

        return self.pages[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)