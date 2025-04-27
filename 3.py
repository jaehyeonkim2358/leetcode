class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        char_to_index_map = dict()
        for right in range(len(s)):
            right_ch = s[right]
            if right_ch in char_to_index_map and char_to_index_map[right_ch] >= left:
                left = char_to_index_map[right_ch] + 1
            char_to_index_map[right_ch] = right

            length = right - left + 1
            answer = max(answer, length)

        return answer
