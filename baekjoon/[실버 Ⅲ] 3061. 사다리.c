#include <stdio.h>

int main(void)
{
	int T, N, cnt, temp;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &N);
		int ladder[N];
		cnt = 0;
		for (int j = 0; j < N; j++)
			scanf("%d", &ladder[j]);
		for (int m = 0; m < N - 1; m++)
		{
			for (int n = m + 1; n < N; n++)
			{
				if (ladder[m] > ladder[n])
				{
					temp = ladder[m];
					ladder[m] = ladder[n];
					ladder[n] = temp;
					cnt++;
				}
			}
		}
		printf("%d\n", cnt);
	}
}