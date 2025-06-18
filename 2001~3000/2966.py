class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(0, len(nums)-2, 3):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if c-a <= k:
                ans.append([a, b, c])
            else:
                return []
        return ans
