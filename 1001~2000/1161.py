# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(1, root)])
        pre_depth = 1
        max_sum = float('-inf')
        answer = 1
        depth_sum = root.val
        while queue:
            depth, node = queue.popleft()
            if depth > pre_depth:
                if depth_sum > max_sum:
                    max_sum = depth_sum
                    answer = pre_depth
                pre_depth = depth
                depth_sum = 0
            depth_sum += node.val
            if node.right:
                queue.append((depth + 1, node.right))
            if node.left:
                queue.append((depth + 1, node.left))

        return pre_depth if depth_sum > max_sum else answer
