# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowest_ancestor = None

        def findLCA(node): 
            nonlocal lowest_ancestor
            
            if lowest_ancestor:
                return (True, True)

            if node == None:
                return (False, False) # p, q

            l_p, l_q = findLCA(node.left)
            r_p, r_q = findLCA(node.right)
            has_p = l_p or r_p or node == p
            has_q = l_q or r_q or node == q

            if not lowest_ancestor and has_p and has_q:
                lowest_ancestor = node

            return (has_p, has_q) 

        findLCA(root)

        return lowest_ancestor
            
        