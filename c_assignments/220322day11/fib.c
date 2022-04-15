#include<stdio.h>

//8.Write a program to print n fibonnaci numbers(Take n from user)

int main()
{
	int i, n;

	// Initialize 1st and 2nd term
	int t1 = 0, t2 = 1;

	// Initializing the next term (3rd term)
	int nextTerm = t1 + t2;

	// Get no. of terms from user
	printf("Enter the number of terms : ");
	scanf("%d", &n);

	printf("Fibonacci series : %d, %d, ", t1, t2);

	// print 3rd to nth terms
	for(i=3; i<=n; ++i)
	{
		printf("%d, ", nextTerm);
		t1 = t2;
		t2 = nextTerm;
		nextTerm = t1 + t2;
	}

	return 0;
}
