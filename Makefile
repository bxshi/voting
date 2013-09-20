CC = gcc
CFLAG =  -lpthread
EXECS = vote_count

all: clean main

clean:
	rm -rf *.o ${EXECS}

count.o:
	${CC} -c count.c ${CFLAG}

vote_counter.o:
	${CC} -c vote_counter.c ${CFLAG}

opts.o:
	${CC} -c opts.c ${CFLAG}

file_reader.o:
	${CC} -c file_reader.c ${CFLAG}

threadpool.o:
	${CC} -c threadpool.c ${CFLAG}

main.o:
	${CC} -c main.c ${CFLAG}

main: main.o file_reader.o opts.o vote_counter.o threadpool.o count.o
	${CC} -o ${EXECS} ${CFLAG} main.o file_reader.o opts.o vote_counter.o threadpool.o count.o
