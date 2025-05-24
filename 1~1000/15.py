class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.counter = Counter(nums)
        self.answer = []
        nums.sort()
        index = 0
        while index < len(nums):
            self.biSearch(nums, index)
            index += self.counter[nums[index]]
        return self.answer

    def biSearch(self, nums, n_index):
        offset = lambda a, b: self.counter[nums[a]] - (nums[b] == nums[a])

        s, e = n_index + 1, len(nums) - 1
        while s < e:
            result = nums[s] + nums[e] + nums[n_index]
            if result == 0:
                self.answer.append([nums[n_index], nums[s], nums[e]])
                e -= offset(e, n_index)
                s += offset(s, n_index)
            else:
                if result > 0:
                    e -= offset(e, n_index)
                else:
                    s += offset(s, n_index)
