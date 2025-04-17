class Solution(object):
    def productExceptSelf(self, nums):
        zero_count = 0
        total_product = 1
        total_product_without_zero = 1
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                total_product_without_zero *= n
            total_product *= n

        answer = [0 for _ in range(len(nums))]
        if zero_count <= 1:
            for i in range(len(nums)):
                n = nums[i]
                answer_num = total_product_without_zero if n == 0 else total_product // n
                answer[i] = answer_num

        return answer
