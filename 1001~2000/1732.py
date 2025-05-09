class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = 0
        gain = [0] + gain
        for i in range(1, len(gain)):
            gain[i] += gain[i-1]
            answer = max(answer, gain[i])
        return answer
