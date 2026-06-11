from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        q, _ = self._get_queue()
        q.append(x)

    def pop(self) -> int:
        q, empty_q = self._get_queue()
        while len(q) > 1:
            empty_q.append(q.popleft())

        return q.popleft()

    def top(self) -> int:
        q, empty_q = self._get_queue()
        while len(q) > 1:
            empty_q.append(q.popleft())

        last = q.popleft()
        empty_q.append(last)
        return last

    def empty(self) -> bool:
        return not self.q1 and not self.q2

    def _get_queue(self):
        return (self.q1, self.q2) if self.q1 else (self.q2, self.q1)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()