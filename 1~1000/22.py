class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gen(left, right, result):
            if left + right == n * 2:
                ans.append(result)
                return
            if left < n:
                gen(left + 1, right, result + '(')
            if right < left:
                gen(left, right + 1, result + ')')

        gen(0, 0, '')
        return ans
