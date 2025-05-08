class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            if self.digitsCount(n) % 2 == 0: answer += 1

        return answer


    def digitsCount(self, num: int) -> int:
        count = 0
        while num > 0:
            num //= 10
            count += 1
        return count
