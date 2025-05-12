# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.countGoodNodes(root, -(10**4) - 1)
        return self.count

    def countGoodNodes(self, node, max_val):
        if node.val >= max_val:
            self.count += 1
        if node.left == None and node.right == None:
            return
        max_val = max(node.val, max_val)
        if node.left: self.countGoodNodes(node.left, max_val)
        if node.right: self.countGoodNodes(node.right, max_val)
