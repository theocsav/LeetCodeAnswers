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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> values;
        preorder(root, values);
        return values;
    }

    void preorder(TreeNode* node, vector<int> &values){
        if(node == nullptr){
            return;
        }
        values.push_back(node->val);
        preorder(node->left, values);
        preorder(node->right, values);
    }
};