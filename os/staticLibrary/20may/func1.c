#include<stdio.h>

void days(int x){
    switch (x)
    {
    case 1:
        printf("Monday\n");
        break;

    case 2:
        printf("Tuesday\n");
        break;
    
    default:
        printf("Invalid\n");
        break;
    }
}