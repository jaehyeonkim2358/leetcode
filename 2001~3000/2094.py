class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        answer = []
        counter = [0] * 10
        for d in digits:
            counter[d] += 1

        for num in range(100, 1000, 2):
            flag = True

            tmp = num
            while tmp > 0:
                n = tmp % 10
                if counter[n] <= 0: flag = False
                counter[n] -= 1
                tmp //= 10

            tmp = num
            while tmp > 0:
                n = tmp % 10
                counter[n] += 1
                tmp //= 10

            if flag: answer.append(num)

        return answer
