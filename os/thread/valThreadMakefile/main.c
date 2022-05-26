#include<pthread.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include"routine1.h"
#include"routine2.h"

extern int val;

int main(int agrc, char* argv[]){
    
    pthread_t t1;
    pthread_t t2;

    printf("Pid : %d\n", getpid());
    sleep(10);

    pthread_create(&t1, NULL, routine1, NULL);
    pthread_join(t1, NULL);

    sleep(10);

    pthread_create(&t2, NULL, routine2, NULL);
    pthread_join(t2, NULL);

    printf("main_val : %d\n",val);

    sleep(10);

    return 0;
}