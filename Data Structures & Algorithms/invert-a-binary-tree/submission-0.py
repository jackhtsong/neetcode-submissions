# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        current = root
        temp = current.left
        current.left = current.right
        current.right = temp

        if current.left != None:
            self.invertTree(current.left)
        if current.right != None:
            self.invertTree(current.right)
        
        return current