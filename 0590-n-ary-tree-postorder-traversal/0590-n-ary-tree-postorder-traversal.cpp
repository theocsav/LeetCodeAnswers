/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> values;
        postorder_helper(root, values);
        return values;
    }
    void postorder_helper(Node* node, vector<int> &values){
        if(node == nullptr){
            return;
        }
        int children_number = node->children.size();
        for(int i = 0; i < children_number; i++){
            postorder_helper(node->children[i], values);
        }
        values.push_back(node->val);
    }
};