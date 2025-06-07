from heapq import heappush, heappop

class Solution:
    def clearStars(self, s: str) -> str:
        if '*' not in s: return s

        N = len(s)
        queue = []
        remove = set()
        for i in range(N):
            ch = s[i]
            if ch == '*':
                remove.add(i)
                if queue:
                    _, index = heappop(queue)
                    remove.add(-index)
            else:
                heappush(queue, (ch, -i))

        return ''.join([s[i] for i in range(N) if i not in remove])
