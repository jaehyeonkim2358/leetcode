class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.DEFAULT_VALUE = 27
        self.parent = [self.DEFAULT_VALUE for _ in range(26)]
        N = len(s1)
        ord_a = ord('a')
        for i in range(N):
            if s1[i] == s2[i]: continue
            self.union(ord(s1[i]) - ord_a, ord(s2[i]) - ord_a)

        for i in range(26):
            self.find(i)

        ans = []
        for ch in baseStr:
            new_ch = ch
            num = ord(ch) - ord_a
            if self.parent[num] != self.DEFAULT_VALUE:
                new_ch = chr(self.parent[num] + ord_a)
            ans.append(new_ch)

        return ''.join(ans)


    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a < b:
            if self.parent[b] > a:
                self.parent[b] = a
        elif b < a:
            if self.parent[a] > b:
                self.parent[a] = b

    def find(self, x):
        if self.parent[x] == self.DEFAULT_VALUE:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
