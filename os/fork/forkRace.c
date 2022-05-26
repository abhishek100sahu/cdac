#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int final_value = 0; // shared variable

int main(int argc, char *argv)
{
    pid_t pid;
    int count1, count2;
    pid = fork();

    if (pid == 0)
    {
        // Child Process Block
        for (int count1 = 0; count1 < 10000000; count1++)
        {
            printf("child count : %d\n", count1);
            final_value = final_value - 1;
        }
    }
    else if (pid > 0)
    {
        // Parent Process block
        for (int count2 = 0; count2 < 10000000; count2++)
        {
            printf("Parent count : %d\n", count1);
            final_value = final_value + 1;
        }
        
    }
    else
    {
        printf("failed to creat child process \n");
        exit(0);
    }

    printf("the final value is %d\n", final_value);

    return 0;
}