class RecentCounter:
    def __init__(self):
        self.count_queue = deque()

    def ping(self, t: int) -> int:
        self.count_queue.append(t)
        while self.count_queue and t - self.count_queue[0] > 3000:
            self.count_queue.popleft()
        return len(self.count_queue)
