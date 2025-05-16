class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        counter = [0] * 26
        for ch in s:
            counter[ord(ch) - ord('a')] += 1
        for _ in range(t):
            next_counter = [0] * 26
            next_counter[0] = counter[-1]
            next_counter[1] = (counter[0] + counter[-1]) % mod
            for i in range(len(counter)-1, 1, -1):
                next_counter[i] = counter[i-1]
            counter = next_counter
        return sum(counter) % mod
