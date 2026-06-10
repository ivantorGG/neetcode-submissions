class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total_sum = 0
        record = []

        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(2 * int(record[-1]))
            elif op == 'C':
                total_sum -= record.pop()
            else:
                record.append(int(op))

        return sum(record)
        