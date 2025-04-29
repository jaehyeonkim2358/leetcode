class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        prefix_sum = 0
        prefix_sum_count = dict()
        answer = 0
        for i in range(len(nums)):
            n = nums[i]
            if n == max_num:
                prefix_sum_count[prefix_sum] = i # 새로운 최대값 전까지의 개수
                prefix_sum += 1

            if prefix_sum >= k:
                answer += prefix_sum_count.get(prefix_sum - k, 0) + 1

        return answer
