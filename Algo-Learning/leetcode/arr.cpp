#include <iostream>
using namespace std;


int len(int arr[]) {
	int len = 0;
	while (arr[len] != '\0') {
		cout << arr[len] << endl;
		len++;
	}
	return len;
}

int main() {
	int arr[4];
	for (int i = 0; i < 4; i++) {
		arr[i] = i + 1;
	}
	cout << len(arr);
}

