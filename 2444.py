class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        i, minP, maxP, wp = 0, -1, -1, -1
        while i < len(nums):
            n = nums[i]
            if n == minK:
                minP = i
            if n == maxK:
                maxP = i

            if minK <= n <= maxK:
                if minP >= 0 and maxP >= 0:
                    answer += min(minP, maxP) - wp
            else:
                minP, maxP = -1, -1
                wp = i
            i += 1

        return answer
