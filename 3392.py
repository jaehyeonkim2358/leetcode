class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        answer  = 0
        window = 3
        for i in range(len(nums) - window + 1):
            if nums[i+1] == (nums[i] + nums[i+2]) * 2:
                answer += 1
        return answer
