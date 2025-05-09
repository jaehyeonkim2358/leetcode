class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        r = 1
        flag = True
        result = defaultdict(list)
        for i in range(len(s)):
            if r == numRows: flag = False
            if r == 1: flag = True

            ch = s[i]
            result[r].append(ch)

            if flag: r += 1
            else: r -= 1

        return ''.join(sum(result.values(), []))
