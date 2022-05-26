#include <stdio.h>
#include<unistd.h>
int main(int agrc, char* argv[])
{
    for(int count =0; count<10; count++)
    {
        printf("Basic Process Creation in c\n");
        sleep(5);
    }
    return 0;
}