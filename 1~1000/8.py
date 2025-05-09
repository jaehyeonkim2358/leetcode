class Solution:
    def myAtoi(self, s: str) -> int:
        reval = 0

        atoi_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        read_start = False
        negative = False
        for ch in s:
            if ch == ' ':
                if read_start: break
            elif not read_start and (ch == '-' or ch == '+'):
                read_start = True
                negative = True if ch == '-' else False
            elif '0' <= ch <= '9':
                read_start = True
                reval *= 10
                reval += atoi_map[ch]
            else:
                break

        reval = -reval if negative else reval
        if reval < -2**31: reval = -2**31
        elif reval > 2**31-1: reval = 2**31-1

        return reval
