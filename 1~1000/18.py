from collections import Counter

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        counter = Counter(nums)
        ans = set()
        N = len(nums)
        for i in range(N-3):
            for j in range(i+3, N):
                left, right = i+1, j-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += counter[nums[left]]
                    elif s > target:
                        right -= counter[nums[right]]
                    else:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += counter[nums[left]]
                        right -= counter[nums[right]]

        return list(ans)
