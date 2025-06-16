class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        latest_max = 0
        ans = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= latest_max:
                latest_max = nums[i]
            else:
                ans = max(ans, latest_max - nums[i])
        return ans
