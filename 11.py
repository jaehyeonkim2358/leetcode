class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        answer = 0
        while l < r:
            cur_amount = min(height[l], height[r]) * (r - l)
            answer = max(answer, cur_amount)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return answer
