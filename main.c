/*
 * =====================================================================================
 *
 *       Filename:  main.c
 *
 *    Description:  Main logic of votes
 *
 *        Version:  1.0
 *        Created:  2013/08/29 22时26分17秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Baoxu Shi (http://github.com/bxshi), bshi@nd.edu
 *   Organization:  University of Notre Dame
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

#include "opts.h"
#include "constants.h"
#include "file_reader.h"
#include "vote_counter.h"
#include "threadpool.h"

int main(int argc, char **argv)
{
    int i, dup_vote;
    int cores, block_size;
    cores = 16;
    block_size = 1024*1024;
    int *thread;
    file_struct *fs;
    threadpool_t *pool;

    thread = malloc(sizeof(int));

    if(argc<2)
    {
        printf("[usage] vote_counter [-dupvote] [-cores C] [-blocksize B] [filename1] ... [filenameN]\n");
        exit(-1);
    }

    char **file_list = malloc(sizeof(char *) * MAX_FILE_NUM);
    memset(file_list, 0, (sizeof(char*))*MAX_FILE_NUM);

    //analyze input arguments
    if(!(dup_vote = opts(argc, argv, file_list, &cores, &block_size, &thread)))
    {
        exit(-1);
    }
    
    printf("thread number %d\n", *thread);
    //printf("cores %d; block_size %d\n", cores, block_size);
    
    //create pool according to total file size & number
    if((pool = threadpool_create(cores, 8192, 0)) == NULL)
    {
        printf("[error] can not initalize thread\n");
        exit(-1);
    }

    init_mutex();

    dup_vote = dup_vote == 2 ? TRUE : FALSE;

    for (i=0; file_list[i]!=NULL; i++)
    {
        fs = malloc(sizeof(file_struct));
        fs->filename = file_list[i];
        fs->dup_vote = dup_vote;
        fs->block_size = block_size;

        //send read task to thread pool
        threadpool_add(pool, &readfile, fs, 0);

    }

    //wait until all thread finish their job
    threadpool_destroy(pool, 1);

    get_vote_result(3);

    return 0;
}

