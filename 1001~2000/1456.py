class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cur_count = max_count = sum(1 for ch in s[:k] if ch in vowels)
        for i in range(1, len(s) - k + 1):
            if s[i-1] in vowels: cur_count -= 1
            if s[i+k-1] in vowels: cur_count += 1
            max_count = max(max_count, cur_count)

        return max_count
