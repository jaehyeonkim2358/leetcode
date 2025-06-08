class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.DEFAULT_VALUE = 27
        self.parent = [self.DEFAULT_VALUE for _ in range(26)]
        ord_a = ord('a')
        for i in range(len(s1)):
            if s1[i] == s2[i]: continue
            self.union(ord(s1[i]) - ord_a, ord(s2[i]) - ord_a)

        ans = []
        for ch in baseStr:
            num = ord(ch) - ord_a
            ans.append(self.find(num))

        return ''.join([chr(n + ord_a) for n in ans])


    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return

        if a < b:
            if self.parent[b] > a:
                self.parent[b] = a
        else:
            if self.parent[a] > b:
                self.parent[a] = b

    def find(self, x):
        if self.parent[x] == self.DEFAULT_VALUE:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
