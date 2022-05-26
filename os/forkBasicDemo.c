#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(int argc, char* argv[]){
    pid_t ret;
    printf("statement before fork --> \n");
    ret = fork();
    printf("statement after fork --> \n");
}