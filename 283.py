class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

        l, r = 0, 0
        while r < len(nums):
            if l == r:
                r += 1
            elif nums[l] == 0 and nums[r] != 0:
                swap(nums, l, r)
            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            elif nums[l] != 0 and nums[r] != 0:
                l += 1
            elif l < r:
                l += 1
