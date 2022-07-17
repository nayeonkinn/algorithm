#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string result = "EABCD";
	for (int i = 0; i < 3; i++) {
		int a, cnt = 0;
		for (int j = 0; j < 4; j++) {
			cin >> a;
			if (a == 0) cnt++;
		}
		cout << result[cnt] << '\n';
	}
}