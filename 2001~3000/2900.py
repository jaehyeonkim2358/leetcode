class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        start_0 = []
        start_1 = []
        for i in range(len(groups)):
            if not start_0:
                if groups[i] == 0: start_0.append(i)
            elif groups[i] != groups[start_0[-1]]:
                start_0.append(i)

            if not start_1:
                if groups[i] == 1: start_1.append(i)
            elif groups[i] != groups[start_1[-1]]:
                start_1.append(i)

        answer = []
        select_groups = start_0 if len(start_0) > len(start_1) else start_1
        for index in select_groups:
            answer.append(words[index])

        return answer
