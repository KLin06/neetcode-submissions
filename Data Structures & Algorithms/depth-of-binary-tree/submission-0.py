# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            depth += 1
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return depth

        