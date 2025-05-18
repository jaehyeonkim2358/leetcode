class Solution:
    def intToRoman(self, num: int) -> str:
        integer_to_roman_map = {
            0: '',
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        def to_roman(d, n):
            if n == 0: return
            if n == 4: return integer_to_roman_map[(10**d)] + integer_to_roman_map[(10**d) * 5]
            if n == 9: return integer_to_roman_map[(10**d)] + integer_to_roman_map[(10**d) * 10]
            if n < 5: return integer_to_roman_map[10**d] * n
            return integer_to_roman_map[(10**d) * 5] + (integer_to_roman_map[10**d] * (n - 5))

        answer = deque()
        for i in range(len(digits)):
            roman = to_roman(i, num % 10)
            if roman: answer.appendleft(roman)
            num //= 10
        return ''.join(answer)
