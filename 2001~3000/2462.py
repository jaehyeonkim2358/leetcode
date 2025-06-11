from heapq import heappush, heappop
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap1, heap2 = [], []
        left, right = 0, 0
        for i in range(min(candidates, len(costs))):
            heappush(heap1, costs[i])
            left = i
        for i in range(len(costs)-1,  max(len(costs)-candidates-1, len(heap1)-1), -1):
            heappush(heap2, costs[i])
            right = i

        left += 1
        right -= 1
        ans = 0
        while k > 0:
            # push
            if len(heap1) < candidates and (left < right or left == right):
                heappush(heap1, costs[left])
                left += 1
            elif len(heap2) < candidates and (left < right or left == right):
                heappush(heap2, costs[right])
                right -= 1

            # pop
            if heap1 and heap2:
                ans += heappop(heap2) if heap1[0] > heap2[0] else heappop(heap1)
            elif heap1:
                ans += heappop(heap1)
            elif heap2:
                ans += heappop(heap2)

            k -= 1

        return ans
