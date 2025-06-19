class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        split_count = 0
        m = -1
        for i in range(len(nums)):
            if m == -1:
                m = nums[i]
            if nums[i] - m > k:
                split_count += 1
                m = nums[i]
        return split_count + 1
