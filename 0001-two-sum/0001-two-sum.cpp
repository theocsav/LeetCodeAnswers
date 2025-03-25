class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for(int i = 0; i < nums.size(); i++){
            int difference = target - nums.at(i);
            if(mp.find(difference) != mp.end()){
                return {mp[difference], i};
            }
            else {
                mp[nums.at(i)] = i;
            }
        }
        return {};
    }
};