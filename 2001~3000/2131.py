class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        WORDS = set(words)
        double_counter = defaultdict(int)
        counter = defaultdict(int)
        reversed_words = {}
        for w in words:
            reversed_w = w[::-1]
            reversed_words[w] = reversed_w
            if reversed_w == w:
                double_counter[w] += 1
            elif reversed_w in WORDS:
                counter[w] += 1

        # 앞뒤가 다른 문자('el', 'fc')
        answer = 0
        for w, cnt in counter.items():
            reversed_w = reversed_words[w]
            answer += min(counter[w], counter[reversed_w]) * 2

        # 앞뒤가 같은 문자('gg', 'mm')
        additional_length = 0
        for dw, cnt in double_counter.items():
            if cnt >= 2:
                usable_count = (cnt // 2) * 2
                answer += usable_count * 2
                double_counter[dw] -= usable_count
            if double_counter[dw] > 0:
                additional_length = 2

        return answer + additional_length
