class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s;
        vector<int> ret;

        for(int i : nums1){
            s.insert(i);
        }
        for(int i : nums2){
            if(s.find(i) != s.end()){
                s.erase(i);
                ret.push_back(i);
            }
        }
        return ret;
    }
};