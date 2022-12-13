#include <stdio.h>

int main(void)
{
	int N, cnt = 0;
	scanf("%d", &N);

	int note[N];
	int button[N];
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &note[i]);
		button[i] = 0;
	}
	for (int j = 0; j < N; j++)
	{
		if (note[j] != button[j])
		{
			for (int k = 0; k < 3 && j + k < N; k++)
				button[j + k] = 1 - button[j + k];
			cnt++;
		}
	}
	printf("%d", cnt);
}