class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        used = [False for _ in range(len(digits))]
        answer = set()
        self.generateNums(digits, used, answer, 0, 0)
        return sorted(list(answer))

    def generateNums(self, digits, used, answer, result, depth):
        if depth == 3:
            answer.add(result)
            return
        for i in range(len(digits)):
            d = digits[i]
            if d == 0 and depth == 0: continue
            if d % 2 == 1 and depth == 2: continue
            if used[i]: continue

            used[i] = True
            old_result = result
            result = result * 10 + d
            self.generateNums(digits, used, answer, result, depth + 1)
            result = old_result
            used[i] = False
