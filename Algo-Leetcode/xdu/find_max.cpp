#include<iostream>
using namespace std;
#include<vector>

vector<int> build_vec(int n){
	vector<int> nums;
	for(int i = 0; i < n; i++){
		int num;
		cin >> num;
		nums.push_back(num);
	}
	return nums;
}

void print_vec(vector<int> vec){
	for(int i = 0; i < vec.size(); i++){
		cout << vec[i] << " ";
	}
	cout << endl;
}

int find_max(vector<int> nums, int i, int j){
	if(i > j){
		return -1;
	}
	if(i == j){
		return nums[i];
	}
	int mid = (i+j)/2;
	int l = find_max(nums, i, mid);
	int r = find_max(nums, mid+1, j);
	return max(l, r);
}

int main(){
	int n = 7;
	vector<int> nums = build_vec(n);
	print_vec(nums);
	cout << find_max(nums, 0, n-1);
	return 0;
} 


