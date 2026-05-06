class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their matching opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                # Pop the top element if stack is not empty, else assign a dummy value '#'
                top_element = stack.pop() if stack else '#'

                # If the popped bracket doesn't match the required opening bracket, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched. Return True.
        return not stack