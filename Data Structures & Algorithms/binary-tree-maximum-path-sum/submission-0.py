# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float('inf')
        def pathSum(node):
            nonlocal maxSum
            if not node: return 0
            left = pathSum(node.left)
            right = pathSum(node.right)
            maxSum = max(maxSum, node.val + max(left + right, left, right, 0))
            return node.val + max(left, right, 0)
        pathSum(root)
        return maxSum