class Solution:
    def reverse(self, x: int) -> int:
        minus = True if x < 0 else False
        x = abs(x)
        result = 0
        while x > 0:
            result *= 10
            result += x % 10
            x //= 10

        result = -result if minus else result
        return result if -2**31 <= result <= 2**31 else 0
