class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(num, limit, result):
            if num > limit: return

            result.append(num)
            for i in range(10):
                nxt = num * 10 + i
                if nxt > limit: break

                dfs(nxt, limit, result)

        ans = []
        for i in range(1, 10):
            dfs(i, n, ans)
        return ans
