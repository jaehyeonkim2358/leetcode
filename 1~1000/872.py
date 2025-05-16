# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, seq):
            if not node.right and not node.left:
                seq.append(node.val)
                return
            if node.left: dfs(node.left, seq)
            if node.right: dfs(node.right, seq)

        seq1, seq2 = [], []
        dfs(root1, seq1)
        dfs(root2, seq2)
        return seq1 == seq2
