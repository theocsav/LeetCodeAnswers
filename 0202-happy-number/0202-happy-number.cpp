#import <unordered_set>

int getSumOfSquares(int n){
    int sum = 0;
    while(n > 0){
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }
    return sum;
}

class Solution {
public:
    bool isHappy(int n) {
       std::unordered_set<int> seenNumbers; 
        
        while(n != 1){
            if(seenNumbers.find(n) != seenNumbers.end()){
                return false;
            }
            seenNumbers.insert(n);

            n = getSumOfSquares(n);
        }
        return true;
    }
};