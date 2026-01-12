# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if lists are empty, return none
        if not preorder or not inorder:
            return None
            
        # first element in preorder is alwasy the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # find index of root in inorder list to split left/right
        mid = inorder.index(root_val)
        
        # recursive calls for childs
        # slice preorder based on length of left subtree (mid)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root