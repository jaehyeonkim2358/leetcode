# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.p_path = None
        self.q_path = None
        self.dfs(root, [])

        while len(self.p_path) != len(self.q_path):
            self.p_path.pop() if len(self.p_path) > len(self.q_path) else self.q_path.pop()

        for i in range(len(self.p_path)-1, -1, -1):
            if self.p_path[i] == self.q_path[i]:
                return self.p_path[i]

    def dfs(self, node, path):
        if not node: return
        if self.p_path and self.q_path: return
        if node.val == self.p.val:
            self.p_path = [pp for pp in path]
            self.p_path.append(node)
        elif node.val == self.q.val:
            self.q_path = [qp for qp in path]
            self.q_path.append(node)

        path.append(node)
        self.dfs(node.right, path)
        self.dfs(node.left, path)
        path.pop()
