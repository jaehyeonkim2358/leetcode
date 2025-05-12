# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def blackBox(node, p, q):
            if not node: return
            if node == p or node == q:
                return node

            left = blackBox(node.left, p, q)
            right = blackBox(node.right, p, q)

            if left and right: return node

            if left: return left
            else: return right

        return blackBox(root, p, q)
