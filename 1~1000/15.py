class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.counter = Counter(nums)
        self.answer = []
        nums.sort()
        index = 0
        while index < len(nums):
            self.search(nums, index)
            index += self.counter[nums[index]]
        return self.answer

    def search(self, nums, n_index):
        # nums[n_index]와 nums[s] 또는 nums[e]가 같은 경우 '숫자개수 - 1' 만큼 이동해야한다.
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
