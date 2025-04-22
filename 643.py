class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = max_sum = sum(nums[0:k])
        l, r = 0, k-1
        while r < len(nums):
            if l > 0: cur_sum = cur_sum - nums[l-1] + nums[r]
            max_sum = max(max_sum, cur_sum)
            l += 1
            r += 1

        return max_sum / k
