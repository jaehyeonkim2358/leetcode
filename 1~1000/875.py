class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s, e = 1, max(piles)
        while s < e:
            m = (s+e)//2
            if sum(math.ceil(p / m) for p in piles) <= h:
                e = m
            else:
                s = m + 1
        return e
