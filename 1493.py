class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_index_arr = [i for i in range(len(nums)) if nums[i] == 0]
        if len(zero_index_arr) == 0: return len(nums) - 1

        zero_index_arr = [-1] + zero_index_arr + [len(nums)]
        answer = 0
        for i in range(1, len(zero_index_arr)-1):
            length = zero_index_arr[i+1] - zero_index_arr[i-1] - 2
            answer = max(answer, length)
        return answer
