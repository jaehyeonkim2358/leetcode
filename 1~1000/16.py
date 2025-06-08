class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_gap = float('inf')
        ans = 0
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+2, len(nums)):
                val = nums[i] + nums[j]
                new_sum = self.bi_search(nums, target, val, min_gap, i, j)
                new_gap = abs(target - new_sum)
                if new_gap < min_gap:
                    min_gap = new_gap
                    ans = new_sum
        return ans

    def bi_search(self, nums, target, val, min_gap, i, j):
        s = i+1
        e = j-1
        m = (s + e) // 2
        while s < e:
            m = (s + e) // 2
            if nums[m] + val >= target:
                e = m
            else:
                s = m + 1
        v1 = nums[s] + val
        v2 = nums[m] + val
        v3 = nums[e] + val
        min_gap = min(abs(target-v1), abs(target-v2), abs(target-v3))
        if min_gap == abs(target-v1):
            return v1
        elif min_gap == abs(target-v2):
            return v2
        else:
            return v3
