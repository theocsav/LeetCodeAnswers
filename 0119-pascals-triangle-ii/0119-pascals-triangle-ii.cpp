class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result;
        
        long long c = 1;
        for(int j = 0; j <= rowIndex; j++){
            result.push_back(c);
            c = c * (rowIndex - j) / (j + 1);
        }
    
        return result;
    }
};