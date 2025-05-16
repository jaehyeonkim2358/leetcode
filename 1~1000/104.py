# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        self.answer = 1
        def dfs(node, depth):
            self.answer = max(self.answer, depth)
            if node.right: dfs(node.right, depth + 1)
            if node.left: dfs(node.left, depth + 1)
        dfs(root, 1)
        return self.answer
