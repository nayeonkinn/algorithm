#include <stdio.h>

int calculate(int *price, int N, int start, int *total)
{
	int max_i, max = 0;

	for (int i = start; i < N; i++)
	{
		if (max < price[i])
		{	
			max_i = i;
			max = price[i];
		}
	}
	for (int j = start; j <= max_i; j++)
	{
		if (j < max_i)
			*total -= price[j];
		else
			*total += price[j] * (max_i - start);
	}
	return (max_i + 1);
}

int main(void)
{
	int N, total = 0, j = 0;

	scanf("%d", &N);
	int price[N];
	for (int i = 0; i < N; i++)
		scanf("%d", &price[i]);
	while (j < N)
		j = calculate(price, N, j, &total);
	printf("%d\n", total);
}