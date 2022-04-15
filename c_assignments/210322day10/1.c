#include<stdio.h>

/*Q1. Given int a[5] = {10, 20, 30, 40, 50 };
int *p=a, *q=*(&a+1) - 1;
evaluate following expressions
*p++, *++p, (*p)++, ++(*p), ++*p, *(p++), *(++p)
*q--, *--q, --(*q), --*q,
(*q)--, *(q--), *(--q)*/

int main()
{
	int a[5] = {10, 20, 30, 40, 50};
	int *p = a, *q = *(&a+1)-1;

//	printf("*p : %d\n", *p);// 1000
//	printf("*q : %d\n", *q);// 1016
//	printf("p : %d\n", p);	
//	printf("q : %d\n", q);
//	printf("*p++ : %d\n", *p++);
//	printf("%d\n", *p);
	printf("*++p : %d\n", *++p);
//	printf("(*p)++ : %d\n", (*p)++);
//	printf("++(*p) : %d\n", ++(*p));
//	printf("++*p : %d\n", ++*p);
//	printf("*(p++) : %d\n", *(p++));
//	printf("*(++p) : %d\n", *(++p));
//	printf("*q-- : %d\n", *q--);
//	printf("*--q : %d\n", *--q);
//	printf("--(*q) : %d\n", --(*q));
//	printf("--*q : %d\n", --*q);
//	printf("(*q)-- : %d\n", (*q)--);
//	printf("*(q--) : %d\n", *(q--));
//	printf("*(--q) : %d\n", *(--q));

	return 0;
}
