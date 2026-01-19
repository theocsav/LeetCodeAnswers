# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def build(start, end):
            # base: bounds crossed means empty tree (none)
            if start > end:
                return [None]
            
            trees = []
            # try ever number as the root
            for i in range(start, end + 1):
                # get all possible left subtrees (smaller vals)
                left_subtrees = build(start, i - 1)
                # get all possible right subtrees (larger vals)
                right_subtrees = build(i + 1, end)
                
                # combine every left with every right
                for l in left_subtrees:
                    for r in right_subtrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            
            return trees

        return build(1, n)