class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        m, n = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(count):
            p = pills
            tmpWorkers = workers[n - count:]
            for i in range(count - 1, -1, -1):
                if tmpWorkers[-1] >= tasks[i]:
                    tmpWorkers.pop()
                else:
                    if p == 0: return False
                    task_index = self.bisectLeft(tmpWorkers, tasks[i] - strength)
                    if task_index == len(tmpWorkers): return False

                    p -= 1
                    tmpWorkers.pop(task_index)
            return True

        # 해결 가능한 최대 task 수를 이분탐색한다.
        s, e = 0, min(n, m) + 1
        while s < e:
            m = (s + e) // 2
            if check(m):
                s = m + 1
            else:
                e = m
        return s - 1 # s는 항상 처음으로 실패한 값(실패한 값 중 가장 작은 값)

    def bisectLeft(self, arr, target):
        s, e = 0, len(arr)
        while s < e:
            m = (s + e) // 2
            if arr[m] < target:
                s = m + 1
            else:
                e = m
        return s
