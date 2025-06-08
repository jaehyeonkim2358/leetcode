class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        min_gap = float('inf')
        for i in range(N-2):
            left, right = i+1, N-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > target:
                    right -= 1
                else:
                    left += 1
                new_gap = abs(s - target)
                if new_gap < min_gap:
                    min_gap = new_gap
                    ans = s

        return ans
