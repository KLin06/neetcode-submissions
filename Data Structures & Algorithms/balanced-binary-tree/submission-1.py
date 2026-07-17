# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def subtree_depth(node) -> int:
            if not node:
                return 0
            r_depth = subtree_depth(node.right)
            l_depth = subtree_depth(node.left)
            if abs(r_depth - l_depth) > 1:
                self.is_balanced = False
            return max(r_depth, l_depth) + 1

        subtree_depth(root)

        return self.is_balanced
