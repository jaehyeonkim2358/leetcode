class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        answer = prefix_sum = 0
        prefix_sum_prefix_count = [0 for n in nums if n == max_num]
        for i in range(len(nums)):
            if nums[i] == max_num:
                prefix_sum_prefix_count[prefix_sum] = i + 1
                prefix_sum += 1

            if prefix_sum < k: continue

            answer += prefix_sum_prefix_count[prefix_sum - k]

        return answer
