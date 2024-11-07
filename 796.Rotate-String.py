class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        elif goal in s + s:
            return True
        else:
            return False
