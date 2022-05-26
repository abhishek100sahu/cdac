#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

//#define Max_MSG_SIZE 100

// char *msg1 = "Pipes are used for one way communication";
// char *msg2 = "First need to write data in buffer";
// char *msg3 = "than read data from buffer";
int sharedVal = 4;

int main(){
    int buffer;
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
    }
    else if(pid == 0){
        close(p[0]);
        int wbytes = write(p[1], &sharedVal, sizeof(sharedVal));
        printf("number of bytes written : %d\n", wbytes);
        close(p[1]);
    }
    else{
        wait(NULL);
        close(p[1]);
        while ((nbytes = read(p[0], &buffer, sizeof(buffer))) > 0){
            printf("value passed by process p1 : %d\n", nbytes);
            close(p[0]);
        }
        buffer += 2;
        sharedVal = buffer;
        printf("modified value : %d\n", sharedVal);
        
    }
    printf("sharedValue : %d\n", sharedVal);
    printf("Finished reading\n");
    //printf("%d",n);
    return 0;
}