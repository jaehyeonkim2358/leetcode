class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]

        s, e = 1, len(nums)-2
        while s < e:
            m = (s+e)//2
            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m-1
            elif nums[m-1] > nums[m]:
                e = m-1
            else:
                s = m+1
        return e-1
