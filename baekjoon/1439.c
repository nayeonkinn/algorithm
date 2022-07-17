#include <stdio.h>

int main(void)
{
	char str[1000000];
	char c;
	int cnt;

	scanf("%s", str);
	c = str[0];
	cnt = 0;
	for (int i = 0; str[i]; i++)
	{
		if (str[i] != c)
			cnt++;
		c = str[i];
	}
	if (cnt % 2 == 1)
		printf("%d", cnt / 2 + 1);
	else
		printf("%d", cnt / 2);
}