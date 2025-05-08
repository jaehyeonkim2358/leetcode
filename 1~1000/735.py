from collections import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            unbroken = True
            while a < 0 and len(stack) > 0 and stack[-1] > 0:
                crash_result = stack[-1] + a
                if crash_result > 0:    # 음수 부서짐
                    unbroken = False
                    break
                elif crash_result == 0: # 둘 다 부서짐
                    stack.pop()
                    unbroken = False
                    break
                else:                   # 양수 부서짐
                    stack.pop()

            if unbroken:
                stack.append(a)

        return stack

# 소행성이 충돌하는 경우는 양수 바로 뒤에 음수가 올 때 뿐이다.
