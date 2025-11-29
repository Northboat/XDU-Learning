#include <iostream>
using namespace std;

void swap(int *arr, int i, int j) {

	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

void perm(int *arr, int k, int m) {
	if (k == m) {
		for (int i = 0; i <= m; i++) {
			cout << arr[i];
		}
		cout << endl;
		return;
	}
	int i = k;
	while (i <= m) {
		swap(arr, k, i);
		perm(arr, k + 1, m);
		swap(arr, k, i);
		i++;
	}
}

int main() {
	int arr[] = {1, 2, 3, 4};
	perm(arr, 0, 3);
	return 0;
}
