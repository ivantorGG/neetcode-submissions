class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total_sum = 0
        record = []

        for op in operations:
            if op[0] == '-' and op[1:].isdigit() or op.isdigit():
                total_sum += int(op)
                record.append(int(op))
            elif op == 'D':
                total_sum += 2 * int(record[-1])
                record.append(2 * int(record[-1]))
            elif op == 'C':
                total_sum -= record.pop()
            elif op == '+':
                total_sum += record[-1] + record[-2]
                record.append(record[-1] + record[-2])

        return total_sum
        