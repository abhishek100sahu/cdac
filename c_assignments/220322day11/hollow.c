#include<stdio.h>

int main()
{
	int n = 6;
	
	for(int i=1; i<=n; i++) {
		for(int j=i; j<=n; j++) {
			if(i==2 && j==n-1 || i==2 && j==n-2 || i==2 && j==n-3 || i==3 && j==n-1 || i==3 && j==n-2 || i==4 && j==n-1) {
				printf(" ");
			}
			else
				printf("*");
		}
		printf("\n");
	}
		
	return 0;
}
