class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_index_arr = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index_arr.append(i)

        if k >= len(zero_index_arr): return len(nums)

        max_count = cur_count = zero_index_arr[k]
        zero_index_arr = [-1] + zero_index_arr + [len(nums)]
        for i in range(len(zero_index_arr) - k - 1):
            cur_count = zero_index_arr[i+k+1] - zero_index_arr[i] - 1
            max_count = max(max_count, cur_count)

        return max_count
