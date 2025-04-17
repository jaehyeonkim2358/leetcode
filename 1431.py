class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        answer = [False for _ in range(len(candies))]
        maxValue = max(candies)
        for i in range(len(candies)):
            curKidCandy = candies[i] + extraCandies
            if maxValue <= curKidCandy:
                answer[i] = True
        return answer
