class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5

        mod = 10**9 + 7
        n_3 = 1
        n_2 = 2
        n_1 = 5
        ans = 0
        for i in range(4, n+1):
            # f(n) = 2 * f(n-1) + f(n-3)
            ans = (n_1 * 2 + n_3) % mod
            n_3 = n_2
            n_2 = n_1
            n_1 = ans

        return ans
