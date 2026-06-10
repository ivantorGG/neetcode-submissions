class Solution:
    def isValid(self, s: str) -> bool:
        all_prev = []
        for char in s:
            if char in '})]':
                if not all_prev:
                    return False

                prev = all_prev.pop()
                if char == '}' and prev != '{':
                    return False
                elif char == ')' and prev != '(':
                    return False
                elif char == ']' and prev != '[':
                    return False

            else:
                all_prev.append(char)
        
        return not all_prev

