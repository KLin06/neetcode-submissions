# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:        
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = [None if x == 'N' or not x else int(x) for x in data.split(',')]
        print(tree)

        i = 0
        def build_tree():
            nonlocal i
            if tree[i] == None:
                return None
            node = TreeNode(tree[i])
            i += 1
            node.left = build_tree()
            i += 1
            node.right = build_tree()
            return node
        
        root = build_tree()
        return root
