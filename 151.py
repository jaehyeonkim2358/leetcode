class Solution(object):
    def reverseWords(self, s):
        array = s.split(" ")
        compact_array = [x for x in array if x != '']
        compact_array.reverse()

        return ' '.join(compact_array)
