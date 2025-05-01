class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                tmpString = ''
                while stack[-1] != '[':
                    tmpString = stack.pop() + tmpString

                stack.pop() # '[' 꺼내기

                numString = ''
                while stack and '0' <= stack[-1] <= '9':
                    numString = stack.pop() + numString

                stack.append(int(numString) * tmpString)
            else:
                stack.append(ch)

        return ''.join(stack)
