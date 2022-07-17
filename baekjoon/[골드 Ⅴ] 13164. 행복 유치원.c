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

int main(void)
{
	int N, K, total = 0;

	scanf("%d %d", &N, &K);
	int height[N];
	int cost[N - 1];
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &height[i]);
		if (i > 0)
			cost[i - 1] = height[i] - height[i - 1];
	}
	qsort(cost, N - 1, sizeof(int), compare);
	for (int j = 0; j < N - K; j++)
		total += cost[j];
	printf("%d", total);
}