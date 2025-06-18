class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(k):
            total = 0
            for p in piles:
                # `p + alpha`가 k로 나누어 떨어지도록 하는 alpha값을 계산
                alpha = (k - (p % k)) % k
                total += p + alpha
            return total // k <= h

        s, e = 1, max(piles)
        while s < e:
            m = (s+e)//2
            if canEatAll(m):
                e = m
            else:
                s = m + 1
        return e
