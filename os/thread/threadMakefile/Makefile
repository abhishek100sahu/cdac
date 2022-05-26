output: main.o routine1.o routine2.o
	gcc main.o routine1.o routine2.o -lpthread -o abhi
main.o: main.c routine1.h routine2.h
	gcc main.c -c
routine1.o: routine1.c
	gcc routine1.c -c
routine2.o: routine2.c
	gcc routine2.c -c
clean:
	rm *.o abhi
run:
	./abhi
