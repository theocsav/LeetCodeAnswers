class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> lastSeen(128, -1);
        int maxLength = 0;
        int start = -1;

        for(int i = 0; i < s.length(); i++){
            start = max(start, lastSeen[s[i]]);
            maxLength = max(maxLength, i - start);
            lastSeen[s[i]] = i;
        }
    return maxLength;
    }
};