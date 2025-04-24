class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        min_size = len(set(nums))

        answer = 1
        for size in range(min_size, len(nums)):
            num_count_map = {}
            for i in range(size):
                n = nums[i]
                num_count_map[n] = num_count_map.get(n, 0) + 1
            if len(num_count_map.keys()) >= min_size:
                answer += 1

            for i in range(1, len(nums) - size + 1):
                left_n = nums[i-1]
                num_count_map[left_n] = num_count_map.get(left_n, 0) - 1
                if num_count_map[left_n] <= 0:
                    del(num_count_map[left_n])

                right_n = nums[i+size-1]
                num_count_map[right_n] = num_count_map.get(right_n, 0) + 1

                if len(num_count_map.keys()) >= min_size:
                    answer += 1

        return answer
