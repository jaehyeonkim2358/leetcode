# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # 노드 찾음
            # 자식 0
            if not root.left and not root.right:
                return None

            # 자식 1
            if not root.left or not root.right:
                return root.left if root.left else root.right

            # 자식 2
            temp = root.left
            while temp.right:
                temp = temp.right
            root.val = temp.val
            root.left = self.deleteNode(root.left, temp.val)

        return root
