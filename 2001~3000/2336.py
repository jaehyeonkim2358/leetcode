class SmallestInfiniteSet:

    def __init__(self):
        self.count = 1
        self.heap = []
        self.removed = set()

    def popSmallest(self) -> int:
        reval = 0
        if self.heap and self.count >= self.heap[0]:
            reval = heappop(self.heap)
        else:
            reval = self.count
            self.count += 1

        self.removed.add(reval)
        return reval

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
