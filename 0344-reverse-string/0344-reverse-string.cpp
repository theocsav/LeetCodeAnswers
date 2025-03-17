class Solution {
public:
    void reverseString(vector<char>& s) {
        for(int i = 0; i < s.size() / 2; i++){
            swap(s.at(i), s.at(s.size() - i - 1));
        }
    }
};