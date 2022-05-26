#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

#define Max_MSG_SIZE 100

char *msg1 = "Pipes are used for one way communication";
char *msg2 = "First need to write data in buffer";
char *msg3 = "than read data from buffer";

int main(){
    char buffer[Max_MSG_SIZE];
    int p[2], nbytes;
    pid_t pid;
    int ret = pipe(p);

    if(ret == -1){
        perror("Pipe not created\n");
        exit(1);
    }
    pid = fork();
    if(pid < 0){
        perror("Child process not created\n");
    }else if(pid > 0){
        close(p[0]);
        write(p[1], msg1,Max_MSG_SIZE);
        write(p[1], msg2, Max_MSG_SIZE);
        write(p[1], msg3, Max_MSG_SIZE);
        close(p[1]);
        wait(NULL);
    }else{
        close(p[1]);
        while ((nbytes = read(p[0], buffer, Max_MSG_SIZE)) > 0){
            printf("%s\n", buffer);
            close(p[0]);
        }
        
    }
    printf("Finished reading\n");
    //printf("%d",n);
    return 0;
}