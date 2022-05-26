#include<stdio.h>
#include"mul.h"
#include"sum.h"

int main(){
    int num1 , num2;
    printf("Enter first number : ");
    scanf("%d", &num1);
    printf("Enter second number : ");
    scanf("%d", &num2);

    int res1 = sum(num1, num2);
    int res2 = mul(num1, num2);
    printf("%d + %d = %d\n", num1, num2, res1);
    printf("%d * %d = %d\n", num1, num2, res2);

    return 0;
}