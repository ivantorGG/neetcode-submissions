class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []

        for char in s:
            if char in parentheses_dict:
                prev = stack.pop() if stack else ''

                if parentheses_dict[char] != prev:
                    return False

            else:
                stack.append(char)

        return not stack

