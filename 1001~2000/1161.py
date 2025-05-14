from queue import PriorityQueue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        counter = itertools.count()
        queue = [(1, next(counter), root)]
        pre_depth = 1
        max_sum = float('-inf')
        answer = 1
        depth_sum = root.val
        while queue:
            depth, _, node = heappop(queue)
            if depth > pre_depth:
                if depth_sum > max_sum:
                    max_sum = depth_sum
                    answer = pre_depth
                pre_depth = depth
                depth_sum = 0
            depth_sum += node.val
            if node.right:
                heappush(queue, (depth + 1, next(counter), node.right))
            if node.left:
                heappush(queue, (depth + 1, next(counter), node.left))

        return pre_depth if depth_sum > max_sum else answer
