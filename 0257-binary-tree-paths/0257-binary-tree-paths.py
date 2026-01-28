# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def dfs(node, current_path):
            if not node:
                return
            
            # add current node val to the path string
            current_path += str(node.val)
            
            # check if leaf
            if not node.left and not node.right:
                paths.append(current_path)
            else:
                dfs(node.left, current_path + "->")
                dfs(node.right, current_path + "->")
        
        dfs(root, "")
        return paths