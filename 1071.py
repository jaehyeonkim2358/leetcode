class Solution(object):
    def gcdOfStrings(self, str1, str2):
        max_len = len(str1) if len(str1) > len(str2) else len(str2)
        min_len = len(str1) if len(str1) < len(str2) else len(str2)
        answer_max_len = self.gcd(max_len, min_len)

        tmp = str1[:answer_max_len]

        while len(tmp) > 0:
          if len(str1) % len(tmp) != 0 or len(str2) % len(tmp) != 0:
            tmp = tmp[:-1]
            continue
          if self.check(tmp, str1) and self.check(tmp, str2):
              return ''.join(tmp)
          tmp = tmp[:-1]
        return ''

    def check(self, tmp, str):
        i, t = 0, 0
        while i < len(str):
            if tmp[t] != str[i]: return False
            t += 1
            i += 1
            if t == len(tmp): t = 0
        return True


    def gcd(self, max, min):
        while min != 0:
            tmp = max % min
            max = min
            min = tmp
        return max
