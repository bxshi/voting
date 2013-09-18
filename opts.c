//
//  opts.c
//  assign1
//
//  Created by Baoxu Shi on 13-8-30.
//  Copyright (c) 2013年 Baoxu Shi. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#include "constants.h"

int opts(int argc, char **argv, char **file_list, int *cores, int *block_size, int **thread)
{
    u_int32_t i;
    u_int16_t file_cnt;
    struct stat sb;
    short rtn;

    file_cnt = 0;
    rtn = 1;
    **thread = 1;

    if (argc <= 0)
    {
        rtn = 0;
    }
    else
    {
        for (i = 1; i < argc; i++)
        {
            //options
            if (argv[i][0] == '-')
            {
                if (!strcmp(argv[i],"-dupvote"))
                {
                    rtn = 2;
                }
                else if (!strcmp(argv[i],"-cores"))
                {
                    i += 1;
                    (*cores) = atoi(argv[i]);
                }
                else if (!strcmp(argv[i],"-blocksize"))
                {
                    i += 1;
                    (*block_size) = atoi(argv[i]);
                }
                else
                {
                    printf("[error] %s is not supported.\n", argv[i]);
                    rtn = 0;
                }
            }
            else
            {
                file_list[file_cnt++] = argv[i];
                if(stat(argv[i],&sb) == -1)
                {
                    rtn = 0;
                    printf("[error] %s is not a valid path\n", argv[i]);
                }
                else
                {
                    if(sb.st_size>=MAX_SIZE_PRE_FILE)
                    {
                        (**thread)++;
			printf("thread %d \n", **thread);
                    }
                }
            }
        }
    }
    return rtn;
}
