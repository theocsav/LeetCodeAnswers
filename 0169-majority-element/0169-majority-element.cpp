class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]]++;
        }
        for(auto iter = mp.begin(); iter != mp.end(); iter++){
            if(iter->second > nums.size() / 2){
                return iter->first;
            }
        }
        return 0;
    }
};