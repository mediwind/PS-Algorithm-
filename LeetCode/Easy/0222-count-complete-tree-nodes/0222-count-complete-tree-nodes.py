# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def DFS(root):
            if not root:
                return 0
            
            left = DFS(root.left)
            right = DFS(root.right)
            return 1 + left + right
        
        return DFS(root)