class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        total_rows_count = 3**m
        mod = 10**9 + 7

        # init rows
        rows = dict()
        for i in range(total_rows_count):
            tmp = i
            row = []
            valid = True
            for _ in range(m):
                # 하나의 row에서 인접한 두 color가 동일하면 invalid row로 판단
                if row and row[-1] == (tmp % 3):
                    valid = False
                    break
                row.append(tmp % 3)
                tmp //= 3
            if valid:
                # valid row만 rows에 저장
                rows[i] = row

        # init row_valid
        # row_valid[i][j] = 두 row rows[i], rows[j]가 인접할 수 있는지 여부를 Boolean으로 저장
        row_valid = [[False] * total_rows_count for _ in range(total_rows_count)]
        for i, row_1 in rows.items():
            for j, row_2 in rows.items():
                row_valid[i][j] = True
                for k in range(m):
                    if row_1[k] == row_2[k]:
                        row_valid[i][j] = False

        # dp[col][j] = 1~col 사이의 rows를 이용해 rows[j]로 끝나는 grid를 만들때의 경우의 수
        dp = [[0] * total_rows_count for _ in range(n+1)]

        # 각 row는 자신을 포함한 1행짜리 grid를 1개씩 만들 수 있음
        for i in rows.keys():
            dp[1][i] = 1

        # 2개부터 n개까지의 col을 이용해 grid를 만드는 경우의 수 계산
        for col in range(2, n+1):
            for i in rows.keys():
                total_ways = 0
                for j in rows.keys():
                    # rows[i], rows[j]가 인접할 수 있다면,
                    if row_valid[i][j]:
                        # rows[j]가 마지막 행인 grid 뒤에 rows[i]를 붙일 수 있음
                        total_ways += dp[col-1][j]
                dp[col][i] = total_ways % mod

        return sum(dp[n]) % mod
