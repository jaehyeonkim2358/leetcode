class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senates = deque(list(senate))
        R_count, D_count = 0, 0
        while True:
            cur = senates.popleft()
            if cur == 'R':
                if D_count > 0:
                    D_count -= 1
                else:
                    R_count += 1
                    senates.append(cur)
            else:
                if R_count > 0:
                    R_count -= 1
                else:
                    D_count += 1
                    senates.append(cur)

            radiant_win = len(senates) == R_count
            dire_win = len(senates) == D_count
            if radiant_win or dire_win:
                return 'Radiant' if radiant_win else 'Dire'
