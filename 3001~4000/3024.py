class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a == b == c: return 'equilateral'
        if c >= a + b: return 'none'
        if a == b or b == c: return 'isosceles'
        return 'scalene'
