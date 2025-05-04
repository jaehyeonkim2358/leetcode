class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        answer = 0
        data = defaultdict(int)
        for d in dominoes:
            d.sort()
            tup_d = tuple(d)
            data[tup_d] += 1
        for v in data.values():
            if v > 1: answer += (v * (v - 1)) // 2
        return answer
