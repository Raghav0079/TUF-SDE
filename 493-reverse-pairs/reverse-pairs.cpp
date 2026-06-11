class Solution {
private:
    // Helper function to count the reverse pairs
    int countPairs(vector<int> &arr, int low, int mid, int high) {
        int right = mid + 1;
        int cnt = 0;
        for (int i = low; i <= mid; i++) {
            // CAST TO long long TO PREVENT INTEGER OVERFLOW
            while (right <= high && arr[i] > 2LL * arr[right]) {
                right++;
            }
            cnt += (right - (mid + 1));
        }
        return cnt;
    }

    // Helper function to merge two sorted halves
    void merge(vector<int> &arr, int low, int mid, int high) {
        vector<int> temp; 
        int left = low;    
        int right = mid + 1; 

        while (left <= mid && right <= high) {
            if (arr[left] <= arr[right]) {
                temp.push_back(arr[left]);
                left++;
            } else {
                temp.push_back(arr[right]);
                right++;
            }
        }

        while (left <= mid) {
            temp.push_back(arr[left]);
            left++;
        }

        while (right <= high) {
            temp.push_back(arr[right]);
            right++;
        }

        for (int i = low; i <= high; i++) {
            arr[i] = temp[i - low];
        }
    }

    // Classic Merge Sort structure tracking the counts
    int mergeSort(vector<int> &arr, int low, int high) {
        int cnt = 0;
        if (low >= high) return cnt;
        
        int mid = low + (high - low) / 2; // Prevents potential overflow of mid calculation
        
        cnt += mergeSort(arr, low, mid);       // Left half
        cnt += mergeSort(arr, mid + 1, high);  // Right half
        cnt += countPairs(arr, low, mid, high); // Count pairs before merging
        merge(arr, low, mid, high);            // Merge sorted halves
        
        return cnt;
    }

public:
    int reversePairs(vector<int>& nums) {
        if (nums.empty()) return 0;
        return mergeSort(nums, 0, nums.size() - 1);
    }
};