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
    bool isSymmetric(TreeNode* root) {
        string left = "";
        string right = "";
        inorder_left(root, root->val, left);
        cout << left << endl;
        cout << right << endl;
        inorder_right(root, root->val, right);
        return left == right;
    }

    void inorder_left(TreeNode* node, int head_value, string &left){
        if(node == nullptr){
            left.append("#")
            return;
        }
        inorder_left(node->left, head_value, left);
        left.append(to_string(node->val));
        inorder_left(node->right, head_value, left);
    }
    void inorder_right(TreeNode* node, int head_value, string &right){
        if(node == nullptr){
            right.append("#")
            return;
        }
        inorder_right(node->right, head_value, right);
        right.append(to_string(node->val));
        inorder_right(node->left, head_value, right);
    }
};