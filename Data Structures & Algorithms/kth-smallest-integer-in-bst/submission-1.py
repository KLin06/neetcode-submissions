# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def inorder_search(node):
            if not node:
                return
            nonlocal cnt
            left = inorder_search(node.left)
            if left:
                return left
            cnt += 1
            if cnt == k:
                return node.val
            return inorder_search(node.right)

        return inorder_search(root)
                