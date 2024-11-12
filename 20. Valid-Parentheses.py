class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_parenthesis = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_parenthesis.values():
                # If it's an opening bracket, push it onto the stack.
                stack.append(char)
            elif char in matching_parenthesis:
                # If it's a closing bracket, check for matching opening bracket.
                if stack and stack[-1] == matching_parenthesis[char]:
                    stack.pop()  # Pop the matching opening bracket from the stack.
                else:
                    return False  # Mismatch found or stack is empty when it shouldn't be.
            else:
                # If the character is not a valid parenthesis, return False.
                return False
        
        return not stack  # If stack is empty, all opening brackets had matching closing    brackets.
