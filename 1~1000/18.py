class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        self.ksum(0, len(nums)-1, 4, target, [], ans, nums)
        return ans

    def ksum(self, l, r, k, target, path, out, nums):
        def skipSameNum(idx, nums):
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]: idx += 1
            return idx+1

        if k == 2:
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    out.append(path + [nums[l], nums[r]])
                    l = skipSameNum(l, nums)
                    r -= 1
            return

        while l < r:
            path.append(nums[l])
            self.ksum(l+1, r, k-1, target - nums[l], path, out, nums)
            path.pop()
            l = skipSameNum(l, nums)
