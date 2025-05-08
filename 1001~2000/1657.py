from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        if set(word1) != set(word2): return False

        # word1에는 개수가 5개인 문자가 2개, word2에는 개수가 5개인 문자가 1개 있다면
        # 연산을 몇 번 해도 같아질 수 없다.
        cc1 = Counter(Counter(word1).values())
        cc2 = Counter(Counter(word2).values())
        if cc1 != cc2: return False

        return True
