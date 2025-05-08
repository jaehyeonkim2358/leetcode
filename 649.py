class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senates = list(senate)
        counter = Counter(senates)
        baned_count = {'R':0, 'D':0}
        need_ban = {'R':0, 'D':0}
        while baned_count['R'] < counter['R'] and baned_count['D'] < counter['D']:
            for i in range(len(senates)):
                s = senates[i]
                if s.islower(): continue
                if baned_count['R'] == counter['R']: return 'Dire'
                if baned_count['D'] == counter['D']: return 'Radiant'

                if need_ban[s] > 0:
                    need_ban[s] -= 1
                    senates[i] = s.lower()
                else:
                  b = 'R' if s == 'D' else 'D'
                  baned_count[b] += 1
                  need_ban[b] += 1

        return 'Radiant' if baned_count['D'] == counter['D'] else 'Dire'
