targetOut: main.o libAddSub.so
	gcc main.o -L . libAddSub.so -o targetOut 

copyheader: header.h
	sudo cp header/h /usr/include

copylib: libAddSub.so
	sudo cp libAddSub.so /usr/lib

runldconfig:
	sudo ldconfig

libAddSub.so: addTwoNumber.o subTwoNumber.o
	gcc -shared addTwoNumber.o subTwoNumber.o -o libAddSub.so

main.o: main.c header.h
	gcc main.c -c

addTwoNumber.o: addTwoNumber.c
	gcc -fPIC addTwoNumber.c -c

subTwoNumber.o: subTwoNumber.c
	gcc -fPIC subTwoNumber.c -c

clean:
	rm *.o targetOut

run:
	./targetOut