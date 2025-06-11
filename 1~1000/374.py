# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s, e = 1, n
        while s < e:
            m = (s+e) // 2
            gm = guess(m)
            if gm == -1:
                e = m
            elif gm == 1:
                s = m + 1
            else:
                return m
        return e
