#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int height[9], sum = 0;
	for (int i = 0; i < 9; i++) {
		cin >> height[i];
		sum += height[i];
	}
	sort(height, height + 9);
	for (int j = 0; j < 8; j++) {
		for (int k = 0; k < 9; k++) {
			if (sum - height[j] - height[k] == 100) {
				for (int l = 0; l < 9; l++) if (l != j && l != k) cout << height[l] << '\n';
				return 0;
			} 
		}
	}
}