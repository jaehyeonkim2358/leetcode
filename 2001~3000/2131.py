class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        answer = 0
        additional_count = 0
        for w, cnt in counter.items():
            reversed_w = w[::-1]
            if w == reversed_w:             # 앞뒤가 같은 문자('gg', 'mm')
                if cnt >= 2:
                    usable_count = (cnt // 2) * 2
                    answer += usable_count * 2
                    counter[w] -= usable_count
                if counter[w] > 0:
                    additional_count = 1
            elif counter[reversed_w] > 0:   # 앞뒤가 다른 문자('el', 'fc')
                answer += min(counter[w], counter[reversed_w]) * 2

        return answer + additional_count * 2
