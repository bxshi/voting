#include <stdio.h>
#include <pthread.h>
#include "threadpool.h"

int main(int argc, char **argv) {

threadpool_t *pool;

	if((pool = threadpool_create(22, 8912, 0)) == NULL)
	{
		printf("[error] can not init\n");
	}
}
