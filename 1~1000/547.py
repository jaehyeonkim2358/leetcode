class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        answer = 0
        visited = [False for _ in range(len(isConnected))]
        for i in range(len(visited)):
            if visited[i]: continue
            self.find_provinces(i, visited, isConnected)
            answer += 1
        return answer

    def find_provinces(self, num, visited, isConnected):
        if visited[num]: return

        visited[num] = True

        for i in range(len(isConnected)):
            if isConnected[num][i] == 1:
                self.find_provinces(i, visited, isConnected)
