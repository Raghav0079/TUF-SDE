#include <vector>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    std::vector<int> arrayRankTransform(std::vector<int>& arr) {
        // Step 1: Create a sorted copy of the unique elements
        std::vector<int> sortedArr = arr;
        std::sort(sortedArr.begin(), sortedArr.end());
        
        // Step 2: Map each unique element to its rank
        std::unordered_map<int, int> rankMap;
        int rank = 1;
        
        for (int num : sortedArr) {
            // Only assign a rank if the number hasn't been ranked yet
            if (rankMap.find(num) == rankMap.end()) {
                rankMap[num] = rank;
                rank++;
            }
        }
        
        // Step 3: Transform the original array to its ranks
        std::vector<int> result;
        result.reserve(arr.size()); // Optimize memory allocation
        for (int num : arr) {
            result.push_back(rankMap[num]);
        }
        
        return result;
    }
};