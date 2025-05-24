class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        p, n, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        if len(z) >= 3:
            ans.add((0, 0, 0))

        P, N = set(p), set(n)
        if z:
            for num in P:
                if -num in N:
                    ans.add((-num, 0, num))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if -(n[i]+n[j]) in P:
                    a, c = min(n[i], n[j], -(n[i]+n[j])), max(n[i], n[j], -(n[i]+n[j]))
                    b = -(a+c)
                    ans.add((a, b, c))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if -(p[i]+p[j]) in N:
                    a, c = min(p[i], p[j], -(p[i]+p[j])), max(p[i], p[j], -(p[i]+p[j]))
                    b = -(a+c)
                    ans.add((a, b, c))

        return [list(item) for item in ans]
