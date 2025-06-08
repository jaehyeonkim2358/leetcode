class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', '}':'{', ']':'['}
        left_brackets = set(['(', '[', '{'])
        stack = []
        for ch in s:
            if ch in left_brackets:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != pair[ch]:
                    return False
                stack.pop()

        return False if stack else True
