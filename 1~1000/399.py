class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        equations_map = defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            equations_map[a][a] = 1
            equations_map[b][b] = 1
            equations_map[a][b] = values[i]
            equations_map[b][a] = 1 / values[i]

        self.checked = defaultdict(dict)
        def dfs(a, b, val):
            self.checked[a][b] = True

            equations_map[a][b] = val
            equations_map[b][a] = 1 / val

            for i in range(len(equations)):
                if equations[i][0] == b:
                    nxt = equations[i][1]
                    nxt_val = equations_map[b][nxt]
                    if nxt not in self.checked[a]: dfs(a, nxt, val * nxt_val)
                    if nxt not in self.checked[b]: dfs(b, nxt, nxt_val)

        equations = equations + [list(reversed(item)) for item in equations]
        for i in range(len(equations)):
            a, b = equations[i]
            if b not in self.checked[a]:
                dfs(a, b, equations_map[a][b])

        answer = []
        for qa, qb in queries:
            result = equations_map[qa][qb] if qb in equations_map[qa] else float(-1)
            answer.append(result)
        return answer
