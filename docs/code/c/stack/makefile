demo: demo.c stack.h stack.o
	gcc -o demo demo.c stack.o

stack.o: stack.c stack.h
	gcc -c stack.c -o $@

clean:
	rm -f *.o demo