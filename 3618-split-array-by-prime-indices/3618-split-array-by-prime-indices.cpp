#include <vector>
#include <numeric>
#include <cmath>
#include <cstdlib>

using namespace std; 

class Solution {
public:
    long long splitArray(vector<int>& nums) {
        int n = nums.size();
        if(n == 0){
            return 0;
        }

        vector<bool> isPrime(n, true); 

        if (n > 0) isPrime[0] = false; // Index 0 is not prime
        if (n > 1) isPrime[1] = false; // Index 1 is not prime


        for (int p = 2; p * p < n; p++){
            if(isPrime[p]){
                for(int i = p * p; i < n; i += p){
                    isPrime[i] = false;
                }
            }
        }

        long long sumA = 0;
        long long sumB = 0;

        for (int i = 0; i < n; i++){
            if(isPrime[i]){
                sumA += nums[i];
            } else {
                sumB += nums[i];
            }
        }
        return abs(sumA - sumB);
    }
};