# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # base case:
        if not root:
            return 0
        
        # max (left, right) + 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))