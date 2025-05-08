class Solution(object):
    def compress(self, chars):
        if len(chars) == 1: return 1
        cp_chars = [c for c in chars] + ['EOA']

        pre_ch = None
        index = -1
        count = 0
        for i in range(len(cp_chars)):
            ch = cp_chars[i]
            if pre_ch == None:
                pre_ch = ch
            elif pre_ch != ch or ch == 'EOA':
                index += 1
                chars[index] = pre_ch
                if count > 1:
                    for nch in str(count):
                        index += 1
                        chars[index] = nch
                pre_ch = ch
                count = 0
            count += 1

        return index + 1
