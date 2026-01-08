# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, low, high):
            # base case, if node is empty its valid
            if not node:
                return True
            
            # check constraints. val must be strictly inside bounds
            if node.val <= low or node.val >= high:
                return False
            
            # recusive step
            # left child must be less than curr, right child must be greater
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
            
        return helper(root, float('-inf'), float('inf'))
        