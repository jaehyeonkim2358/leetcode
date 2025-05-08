class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes_list = list(dominoes)
        pre_domino = 'L'
        stack = []
        for i in range(len(dominoes_list)):
            d = dominoes_list[i]
            if d == '.':
                stack.append(i)
            else:
                if pre_domino == d:
                    self.change(dominoes_list, stack, d)
                elif d == 'L': # R -> L
                    length = len(stack)
                    if length > 1:
                        self.change(dominoes_list, stack[:length//2], 'R')
                        self.change(dominoes_list, stack[length//2 + length % 2:], 'L')

                stack = []
                pre_domino = d

        if pre_domino == 'R':
            self.change(dominoes_list, stack, 'R')

        return ''.join(dominoes_list)

    def change(self, arr, index_arr, char):
        for i in index_arr: arr[i] = char
