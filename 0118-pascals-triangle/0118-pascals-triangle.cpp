class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        for(int i = 0; i < numRows; i++){
            vector<int> row;
            int c = 1;
            for(int j = 0; j <= i; j++){
                row.push_back(c);
                c = c * (i - j) / (j + 1);
            }
            result.push_back(row);
        }
        return result;
    }
};