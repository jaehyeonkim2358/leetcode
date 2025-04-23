class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            # i == 0 일 때, prefix_sum[-1]은 0이다.
            prefix_sum[i] = nums[i] + prefix_sum[i-1]

        for i in range(len(nums)):
            left_val = 0 if i == 0 else prefix_sum[i-1]
            right_val = 0 if i == len(nums) - 1 else prefix_sum[-1] - prefix_sum[i]
            if left_val == right_val: return i
        return -1
