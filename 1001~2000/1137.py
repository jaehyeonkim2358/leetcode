class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        for i in range(n-2):
            t[i%3] = t[i%3] + t[(i%3+1)%3] + t[(i%3+2)%3]
        return t[n%3]
