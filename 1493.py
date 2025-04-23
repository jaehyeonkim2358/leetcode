class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_index_arr = [i for i in range(len(nums)) if nums[i] == 0]
        if len(zero_index_arr) == 0: return len(nums) - 1

        zero_index_arr = [-1] + zero_index_arr + [len(nums)]
        answer = 0
        for i in range(1, len(zero_index_arr)-1):
            # 두 index a, b 사이의 간격은 a - b - 1
            # 여기서는 i번째 숫자(0)를 삭제한 길이를 구하는것이라 a - b - 1 - 1 = a - b - 2
            length = zero_index_arr[i+1] - zero_index_arr[i-1] - 2
            answer = max(answer, length)
        return answer
