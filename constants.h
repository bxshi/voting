//
//  constants.h
//  assign1
//
//  Created by Baoxu Shi on 13-8-30.
//  Copyright (c) 2013年 Baoxu Shi. All rights reserved.
//

#ifndef assign1_constants_h
#define assign1_constants_h

#define MAX_FILE_NUM 4096
#define MAX_LINE_PRE_CHUNK 819200
#define MAX_LINE_LEN 23 //2^32 10digits
#define MAX_SIZE_PRE_FILE 17203200
#define TRUE 1
#define FALSE 0

#include "uthash.h"

struct vote_result
{
    u_int32_t uid;
    u_int32_t count;
    UT_hash_handle hh;
};

struct vote_history
{
    u_int32_t uid;
    u_int32_t vote;
    UT_hash_handle hh;
};

typedef struct file_struct
{
    char *filename;
    int dup_vote;
    long block_size;
} file_struct;

//global hashmap
typedef struct vote_info
{
    u_int32_t **uid;
    u_int32_t **vote;
    u_int16_t len;
} vote_info;

#endif
