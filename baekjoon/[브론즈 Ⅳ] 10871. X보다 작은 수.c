#include <stdio.h>

int main(void) {
	int N, X, num;
	scanf("%d %d", &N, &X);
	for (int i = 0; i < N; i++) {
		scanf("%d", &num);
		if (num < X) printf("%d ", num);
	}
}

/*baaarkingdog
#include <bits/stdc++.h>
using namespace std;
int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, x, t;
	cin >> n >> x;
	while (n--) {
		cin >> t;
		if (t < x) cout << t << ' ';
	}
}