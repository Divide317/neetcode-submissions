#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        // 1. Get the size 'n' directly from the input vector
        int n = nums.size();
        
        // 2. Create the new vector 'arr1' with a size of 2 * n
        vector<int> arr1(2 * n);
        
        // 3. Your exact loop logic
        for (int j = 0; j < n; j++) {
            arr1[j] = nums[j];
            arr1[j + n] = nums[j];
        }
        
        // 4. Return the result instead of printing it
        return arr1;
    }
};