#include <stdio.h>

int is_last(char *str)
{
	for (int i = 0; str[i]; i++)
	{
		if (str[i] == '-')
			return (1);
	}
	return (0);
}

void count_and_print(char *str)
{
	int cnt = 0;
	int stack = 0;

	for (int i = 0; str[i]; i++)
	{
		if (str[i] == '{')
			stack++;
		else if (stack == 0 && str[i] == '}')
		{
			cnt++;
			stack++;
		}
		else if (stack != 0 && str[i] == '}')
			stack--;
	}
	printf("%d\n", stack / 2 + cnt);
}

int main(void)
{
	int line = 1;

	while (1)
	{
		char str[2000];
		scanf("%s", str);
		if (is_last(str) == 1)
			return (0);
		else
			printf("%d. ", line);
		count_and_print(str);
		line++;
	}
}