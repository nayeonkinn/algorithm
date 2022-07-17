#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, time, y = 0, m = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> time;
		y += ((time / 30) + 1) * 10;
		m += ((time / 60) + 1) * 15;
	}
	if (y < m) cout << "Y " << y;
	else if (y > m) cout << "M " << m;
	else cout << "Y M " << y;
}