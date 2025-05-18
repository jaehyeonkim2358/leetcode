class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        dp = [0] * N
        parent = [-1] * N
        max_index = 0
        for i in range(N):
            for j in range(i):
                if self.check(i, j, words, groups) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                if dp[i] > dp[max_index]:
                    max_index = i

        answer = []
        index = max_index
        while index >= 0:
            answer.append(words[index])
            index = parent[index]
        answer.reverse()
        return answer


    def check(self, i, j, words, groups):
        if groups[i] == groups[j]: return False
        if len(words[i]) != len(words[j]): return False
        gap = 0
        for p in range(len(words[i])):
            if words[i][p] != words[j][p]:
                gap += 1
        return gap == 1
