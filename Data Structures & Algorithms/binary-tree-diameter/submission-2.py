# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def get_depth(node):
            if node == None:
                return 0
            l_depth = get_depth(node.left)
            r_depth = get_depth(node.right)
            self.max = max(l_depth + r_depth, self.max)
            return max(l_depth + 1, r_depth + 1)
        get_depth(root)
        return self.max
        