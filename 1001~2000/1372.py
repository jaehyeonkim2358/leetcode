# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root, 0, 0), self.dfs(root, 1, 0))

    def dfs(self, node, next_direction, length):
        # next_direction: 0=right, 1=left
        if not node: return length - 1

        reval = 0
        if next_direction == 0:
            reval = max(self.dfs(node.right, 1, length + 1), self.dfs(node.left, 0, 1))
        else:
            reval = max(self.dfs(node.left, 0, length + 1), self.dfs(node.right, 1, 1))

        return reval
