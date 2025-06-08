class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = dict()
        s, e = 0, 3
        for i in range(2,10):
            phone[i] = [chr(i+ord('a')) for i in range(s,e)]
            s = e
            e += 3 if i != 8 and i != 6 else 4
        digits = [int(d) for d in digits]

        self.ans = []
        def backtrack(result, depth):
            if depth == len(digits):
                self.ans.append(''.join(result))
                return
            for alph in phone[digits[depth]]:
                result.append(alph)
                backtrack(result, depth + 1)
                result.pop()

        backtrack([], 0)
        return self.ans
