#include <stdio.h>

int findSum(int a)
{
	if (a < 10)
		return a;
	return (a % 10) + findSum(a / 10);
}

int main(void)
{
	int a, sum;
	scanf("%d", &a);
	while (1)
	{
		sum = findSum(a);
		if (sum % 4 == 0)
		{
			printf("%d\n", a);
			break;
		}
		a++;
	}
	return 0;
}
