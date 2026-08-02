# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        sol = -1
        def inorder_search(node):
            if not node:
                return
            nonlocal cnt
            nonlocal sol
            inorder_search(node.left)
            cnt += 1
            if cnt == k:
                sol = node.val
            inorder_search(node.right)
        inorder_search(root)
        return sol
        