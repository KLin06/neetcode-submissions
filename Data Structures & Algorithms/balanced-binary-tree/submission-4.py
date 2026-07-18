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
            if r_depth == -1 or l_depth == -1:
                return -1
            if abs(r_depth - l_depth) > 1:
                return -1
            return max(r_depth, l_depth) + 1

        return subtree_depth(root) != -1

