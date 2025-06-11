class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def biSearch(s):
            l, r = 0, len(potions)-1
            while l < r:
                m = (l+r)//2
                if potions[m] * s >= success:
                    r = m
                else:
                    l = m + 1
            return r

        potions.sort()
        ans = []
        for s in spells:
            idx = biSearch(s)
            alpha = 1 if potions[idx] * s >= success else 0
            ans.append(len(potions) - (idx + 1) + alpha)

        return ans
