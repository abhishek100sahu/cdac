#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(int argc, char* argv[]){
    pid_t ret;
     
    ret = fork();
     ret = fork();
      ret = fork();
       //ret = fork();

    printf("statement before fork --> \n");
}
