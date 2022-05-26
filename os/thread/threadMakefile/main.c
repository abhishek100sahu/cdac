#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<pthread.h>
#include "routine1.h"
#include "routine2.h"


int main(int argc, char* argv[]){
    //thread routine -->function
    
    pthread_t t1;
    pthread_t t2;
    //creat a thread
    printf("pid : %d\n", getpid());
    sleep(10);
    pthread_create(&t1,NULL,routine1,NULL);
    pthread_join(t1,NULL);
    // system("ps")
    
    sleep(30);
    pthread_create(&t2,NULL,routine2,NULL);
    pthread_join(t2,NULL);
    sleep(30);
    

    // pthread_create(&t1, NULL,routine2, NULL);
    // pthread_join(t1, NULL);
}