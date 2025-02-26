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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> values;
        postorder(root, values);
        return values;
    }

    void postorder(TreeNode* node, vector<int> &values){
        if(node == nullptr){
            return;
        }

        postorder(node->left, values);
        postorder(node->right, values);
        values.push_back(node->val);
    }
};