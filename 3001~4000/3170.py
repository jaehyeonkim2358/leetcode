from heapq import heappush, heappop

class Solution:
    def clearStars(self, s: str) -> str:
        if '*' not in s: return s

        ord_a = ord('a')
        N = len(s)
        alph_queue = []
        stack = [[] for _ in range(26)]
        remove = set()
        for i in range(N):
            ch = s[i]
            if ch == '*':
                remove.add(i)
                if alph_queue:
                    alph_num = heappop(alph_queue)
                    index = stack[alph_num].pop()
                    remove.add(index)
            else:
                alph_num = ord(ch) - ord_a
                heappush(alph_queue, alph_num)
                stack[alph_num].append(i)

        return ''.join([s[i] for i in range(N) if i not in remove])
