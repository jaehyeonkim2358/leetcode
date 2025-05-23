class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True

        i = 0
        for ch in t:
            if ch == s[i]:
                i += 1
            if i == len(s):
                return True
        return False
