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
    bool isBalanced(TreeNode* root) {
        bool balanced = height(root) != -1;
        return balanced;
    }

    int height(TreeNode* node){
        if(node == nullptr){
            return 0;
        }
        int left = height(node->left);
        if(left == -1){
            return -1;
        }
        int right = height(node->right);
        if(right == -1){
            return -1;;
        }
        if(abs(left - right) > 1){
            return -1;
        }
        return max(left, right) + 1;
    }
};