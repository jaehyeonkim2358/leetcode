class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        def backtrack(result, s, depth, total):
            if depth == k:
                if total == n: self.ans.append(result[:])
                return
            for i in range(s,10):
                result.append(i)
                backtrack(result, i+1, depth+1, total+i)
                result.pop()

        backtrack([], 1, 0, 0)
        return self.ans
