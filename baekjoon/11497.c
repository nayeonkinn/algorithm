#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
	if (*(int *)a > *(int *)b)
		return 1;
	else if (*(int *)a < *(int *)b)
		return -1;
	else
		return 0;
}

void count(int *L, int N)
{
	int map[N];
	int j = N / 2, k = 0, max = 0;

	for (int i = 0; i < N; i++)
	{
		j += k;
		map[j] = L[i];
		if (i % 2 == 1)
			k = i + 1;
		else
			k = (i + 1) * -1;
	}
	for (int k = 1; k < N; k++)
	{
		if (abs(map[k] - map[k - 1]) > max)
			max = abs(map[k] - map[k - 1]);
	}
	printf("%d\n", max);
}

int main(void)
{
	int T, N;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &N);
		int L[N];
		for (int j = 0; j < N; j++)
			scanf("%d", &L[j]);
		qsort(L, N, sizeof(int), compare);
		count(L, N);
	}
}