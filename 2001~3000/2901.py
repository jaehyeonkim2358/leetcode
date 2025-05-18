class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        dp = [0] * N
        parent = [-1] * N # parent[i]에 subsequence를 구성하는 words[i] 이전 요소의 index를 저장
        max_index = 0
        for i in range(N):
            for j in range(i):
                if self.check(i, j, words, groups) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1

                    # words[i]가 현재 까지 만들어진 subsequence의 마지막 요소일 때,
                    # subsequence의 words[i] 이전 값은 words[j]
                    parent[i] = j
                if dp[i] > dp[max_index]:
                    max_index = i

        # 마지막 요소(words[max_index])부터 시작해서 parent[i]에 저장된 index를 따라 이전 요소를 찾아가면서 전체 subsequence를 구성
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
