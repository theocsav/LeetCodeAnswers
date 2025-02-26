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
    vector<int> preorder(Node* root) {
        vector<int> values;
        preorder(root, values);
        return values;
    }
    void preorder(Node* node, vector<int> &values){
        if(node == nullptr){
            return;
        }
        values.push_back(node->val);
        int children_number = node->children.size();
        for(int i = 0; i < children_number; i++){
            preorder(node->children[i], values);
        }
    }
};