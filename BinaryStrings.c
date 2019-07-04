#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
/*
 1. Take inputs of string A and B (1 <= B <= A = 10^6)
 2. Compare every possible substring of string A of length string B (string C)
		to string B
 3. For each comparison, count the number of differences between the two strings
 4. Print the number of substrings with even number of differences
*/
int main(void)
{
	int i = 0, substringCounter = 0, j, sameCounter = 0, evenCounter = 0;
	char *stringA = calloc(1, sizeof(char) * pow(10.0, 6.0));
	char *stringB;
	char **stringC;
	scanf("%s", stringA);
	stringB = calloc(1, sizeof(char) * strlen(stringA));
	scanf("%s", stringB);
	for (i = 0; i + strlen(stringB) <= strlen(stringA); i++)
		substringCounter++;
	stringC = calloc(1, sizeof(char *) * substringCounter);
	for (i = 0; i < substringCounter; i++)
	{
		stringC[i] = calloc(1, sizeof(char) * strlen(stringB));
		strncpy(stringC[i], stringA+i, strlen(stringB));
		for (j = 0; j < strlen(stringB); j++)
			if (stringB[j] != stringC[i][j])
				sameCounter++;
		if (sameCounter % 2 == 0)
			evenCounter++;
		sameCounter = 0;
		free(stringC[i]);
	}
	printf("%d\n", evenCounter);
	return 0;
}
