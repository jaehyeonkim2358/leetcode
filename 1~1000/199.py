# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        result = []
        queue = [(root, 0)]
        while queue:
            node, cur_depth = queue.pop(0)

            if cur_depth >= len(result):
                result.append(node.val)

            if node.right: queue.append((node.right, cur_depth + 1))
            if node.left: queue.append((node.left, cur_depth + 1))

        return result
