class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_map = dict()
        for n in nums:
            if n not in nums_map: nums_map[n] = 0
            nums_map[n] += 1

        answer = 0
        for n in nums:
            if n >= k: continue
            if k-n not in nums_map: continue
            if nums_map[n] > 0 and nums_map[k-n] > 0:
                nums_map[n] -= 1
                if nums_map[k-n] > 0:
                    nums_map[k-n] -= 1
                    answer += 1
        return answer
