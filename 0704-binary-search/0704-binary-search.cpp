class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size() - 1, target);
    }

    int binarySearch(vector<int> nums, int low, int high, int x){
        if(high >= low){
            int mid = low + (high - low) / 2;
            if(nums.at(mid) == x){
                return mid;
            }
            if(nums.at(mid) > x){
                return binarySearch(nums, low, mid - 1, x);
            }
            return binarySearch(nums, mid + 1, high, x);
        }
        return -1;
    }
};