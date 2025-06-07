from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        ans = []
        min_ch = 'a'
        for i in range(len(s)):
            ch = s[i]
            stack.append(ch)
            counter[ch] -= 1
            while min_ch != 'z' and counter[min_ch] == 0:
                min_ch = chr(ord(min_ch) + 1)
            while stack and stack[-1] <= min_ch:
                ans.append(stack.pop())
        return ''.join(ans)
