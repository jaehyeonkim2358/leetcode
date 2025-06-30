from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        prev = -float('inf')
        ans = 0
        for n in sorted(counter.keys()):
            if n - prev == 1:
                ans = max(counter[prev] + counter[n], ans)
            prev = n
        return ans
