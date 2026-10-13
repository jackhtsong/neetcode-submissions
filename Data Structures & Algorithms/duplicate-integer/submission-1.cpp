#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> seen;

        for (int n : nums) {
            if (seen.find(n) != seen.end()) {
                return true;
            }
            seen[n] = true;
        }
        return false;
    }
};
