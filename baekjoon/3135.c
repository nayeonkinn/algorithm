#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int from, to, N, button;
	int preset[5];

	scanf("%d %d %d", &from, &to, &N);
	button = abs(from - to);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &preset[i]);
		if (abs(preset[i] - to) < button)
			button = abs(preset[i] - to) + 1;
	}
	printf("%d", button);
}