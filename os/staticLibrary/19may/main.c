#include<stdio.h>
#include"header.h"

int main(int argc, char * argv[]){
    int num1 = 20;
    int num2 = 10;

    printf("%d + %d = %d\n",num1 ,num2, addTwoNumber(num1,num2));
    printf("%d - %d = %d\n",num1 ,num2, subTwoNumber(num1,num2));

    return 0;
}