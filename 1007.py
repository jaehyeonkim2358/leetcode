class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        length = len(tops)
        num_count_map = [0] * 7
        for i in range(length):
            t, b = tops[i], bottoms[i]
            num_count_map[t] += 1
            if t != b: num_count_map[b] += 1

        tops_counter = Counter(tops)
        bottoms_counter = Counter(bottoms)
        answer = length
        for i in range(1, 7):
            if num_count_map[i] != length: continue
            t, b = tops_counter[i], bottoms_counter[i]
            rem = max(t+b-length, 0)
            answer = min(answer, t-rem, b-rem)

        return -1 if answer == length else answer
