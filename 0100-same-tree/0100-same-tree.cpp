/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        std::vector<int> tree1, tree2;

        preorder(p, tree1);
        preorder(q, tree2);

        return tree1 == tree2;
        
    }

    void preorder(TreeNode* node, std::vector<int>& result){
        if(!node){
            result.push_back(-999);
            return;
        }
        result.push_back(node->val);
        preorder(node->left, result);
        preorder(node->right, result);
    }  
};