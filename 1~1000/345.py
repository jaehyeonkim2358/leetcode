class Solution(object):
    def reverseVowels(self, s):
        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels_of_string = []
        for ch in s:
            if ch in VOWELS:
                vowels_of_string.append(ch)

        answer = []
        for ch in s:
            appendable_char = ch if ch not in VOWELS else vowels_of_string.pop()
            answer.append(appendable_char)

        return ''.join(answer)
