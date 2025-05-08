class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sums = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            prefix_sums[i] += prefix_sums[i-1] + nums[i]
        prefix_sums = [0] + prefix_sums

        answer = 0
        for i in range(1, len(prefix_sums)):
            answer += self.biSearch(prefix_sums, i, k)

        return answer


    def biSearch(self, sums, index, k):
        s, e = 0, index
        while s < e:
            mid = (s + e) // 2
            if (sums[index] - sums[mid]) * (index - mid) < k:
                e = mid
            else:
                s = mid + 1
        return index - e
