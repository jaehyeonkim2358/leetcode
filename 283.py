class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_nums = []
        for n in nums:
            if n != 0: non_zero_nums.append(n)

        for i in range(len(nums)):
            if i < len(non_zero_nums):
                nums[i] = non_zero_nums[i]
            else:
                nums[i] = 0
