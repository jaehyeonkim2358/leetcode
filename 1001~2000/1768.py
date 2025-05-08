class Solution(object):
    def mergeAlternately(self, word1, word2):
        str_list = []
        word1_len = len(word1)
        word2_len = len(word2)
        min_length = word1_len if word1_len < word2_len else word2_len
        for i in range(min_length):
            if word1_len > i:
              str_list.append(word1[i])
            if word2_len > i:
              str_list.append(word2[i])
        result = ''.join(str_list)
        result += word1[min_length:]
        result += word2[min_length:]

        return result
