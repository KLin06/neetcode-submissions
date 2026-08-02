# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse_dfs(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp

            reverse_dfs(node.right)
            reverse_dfs(node.left)
        
        reverse_dfs(root)
        return root
        