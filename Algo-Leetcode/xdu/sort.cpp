#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

// Merge Sort Implementation
void merge(vector<int>& nums, int left, int right) {
	if(left >= right){
		return;
	}
	int mid = (left+right) / 2;
	merge(nums, left, mid);
	merge(nums, mid+1, right);
	
    vector<int> temp(right - left + 1);
    int i = left, j = mid+1, count = 0;
    
    while(i<=mid && j<=right){
        if(nums[i]<nums[j]){
            temp[count++] = nums[i++];
        }else{
            temp[count++] = nums[j++];
        }
    }
    while(i<=mid){ temp[count++] = nums[i++]; }
    while(j<=right){ temp[count++] = nums[j++]; }
    for(int k = 0; k <= right-left; k++){
        nums[k+left] = temp[k];
    }
}

void mergeSort(vector<int>& arr) {
    merge(arr, 0, arr.size()-1);
}



// Quick Sort Implementation
void partition(vector<int>& arr, int left, int right) {
	if(left >= right){ return; }
	swap(arr[right], arr[(left+right)/2]);
    int pivot = arr[right];
    int p = left;

    for (int i = left; i < right; i++) {
        if (arr[i] < pivot) {
            swap(arr[i], arr[p++]);
        }
    }
    swap(arr[p], arr[right]);
    partition(arr, left, p-1);
    partition(arr, p+1, right);
}

void quickSort(vector<int>& arr) {
    partition(arr, 0, arr.size()-1);
}

// Generate Random Data
vector<int> generateData(size_t size, int lower_bound = 0, int upper_bound = 10000) {
    vector<int> data(size);
    for (size_t i = 0; i < size; ++i) {
        data[i] = lower_bound + rand() % (upper_bound - lower_bound + 1);
    }
    return data;
}

// Time Comparison
void compareAlgorithms() {
    vector<size_t> sizes = {10000, 100000, 500000};

    for (size_t size : sizes) {
        vector<int> data = generateData(size);

        vector<int> data_copy = data;
        clock_t start = clock();
        mergeSort(data);
        double mergeTime = double(clock() - start) / CLOCKS_PER_SEC;

        data = data_copy;
        start = clock();
        quickSort(data);
        double quickTime = double(clock() - start) / CLOCKS_PER_SEC;

        cout << "Data Size: " << size << endl;
        cout << "Merge Sort Time: " << mergeTime << " seconds" << endl;
        cout << "Quick Sort Time: " << quickTime << " seconds" << endl;
        cout << string(40, '-') << endl;
    }
}

int main() {
    srand(time(0));
    compareAlgorithms();
    return 0;
}

