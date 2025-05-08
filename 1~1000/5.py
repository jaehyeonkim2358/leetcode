class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, 0
        for i in range(len(s)):
            tl, tr = self.palindromeRange(s, i)
            if r - l < tr - tl:
                l, r = tl, tr

        return s[l:r+1]

    def palindromeRange(self, s: str, i: int) -> tuple:
        def odd_palindrome(s, i):
            l, r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l+1, r-1)

        def even_palindrome(s, i):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l+1, r-1)

        odd = odd_palindrome(s, i)
        even = even_palindrome(s, i)
        odd_len = odd[1]-odd[0]
        even_len = even[1]-even[0]

        return odd if odd_len > even_len else even
