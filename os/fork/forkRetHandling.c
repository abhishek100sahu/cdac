#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include<stdlib.h>

int sum(int, int);
int sub(int, int);
int num1, num2;

int main(int argc, char *argv)
{
    pid_t ret;

    printf("Enter num1 : ");
    scanf("%d", &num1);
    printf("Enter num2 : ");
    scanf("%d", &num2);

    ret = fork();

    if (ret == 0)
    {
        // Child Process Block
        printf("cpid : %d\n", getpid());
        printf("cppid : %d\n", getppid());
        int result = sum(num1, num2);
        printf("%d + %d = %d\n", num1, num2, result);
    }
    else if(ret > 0)
    {
        // Parent Process block
        printf("ppid = %d\n",getpid());
        printf("pppid = %d\n",getppid());
        int result = sub(num1,num2);
        printf("%d - %d = %d \n",num1,num2,result);

    }
    else{
        printf("failed to creat child process \n");
        exit(0);
    }
    printf("Hola\n");
    printf("fork ret val : %d", ret);
    sleep(70);

    return 0;
}

int sum(int num1, int num2)
{
    int result = num1 + num2;
    return result;
}

int sub(int num1, int num2)
{
    int result = num1 - num2;
    return result;
}