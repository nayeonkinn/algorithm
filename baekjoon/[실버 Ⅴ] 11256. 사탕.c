#include <stdio.h>

void sort(int *info, int N)
{
	int temp;

	for (int i = 0; i < N - 1; i++)
	{
		for (int j = i + 1; j < N; j++)
		{
			if (info[i] < info[j])
			{
				temp = info[i];
				info[i] = info[j];
				info[j] = temp;
			}
		}
	}
}

int main(void)
{
	int T, J, N, row, col, box, capa;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d %d", &J, &N);
		int info[1000] = {0};
		for (int j = 0; j < N; j++)
		{
			scanf("%d %d", &row, &col);
			info[j] = row * col;
		}
		sort(info, N);
		box = 0;
		capa = 0;
		for (int k = 0; k < N; k++)
		{
			if (capa < J)
				box++;
			else
				break;
			capa += info[k];
		}
		printf("%d\n", box);
	}
}