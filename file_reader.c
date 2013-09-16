//
//  file_reader.c
//  assign1
//
//  Created by Baoxu Shi on 13-8-30.
//  Copyright (c) 2013 Baoxu Shi. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "file_reader.h"
#include "constants.h"
#include "vote_counter.h"

ssize_t getline_warpper(char **linep, size_t *linecapp, FILE *stream);
ssize_t getline_warpper(char **linep, size_t *linecapp, FILE *stream){
	return getline(linep, linecapp, stream);
}

//read file by lines, and dispatch them to a vote counter
int readfile(void *arg)
{
    char *filename;
    int dup_vote;
    FILE *fp;
    char *line, *val;
    size_t len;
    ssize_t read;
    int cnt=0;
    int cfinder = 0;
    short valid;
    long line_count = 0;
    filename = ((file_struct *)arg)->filename;
    dup_vote = ((file_struct *)arg)->dup_vote;

    u_int32_t *uid = malloc(sizeof(u_int32_t) * MAX_LINE_PRE_CHUNK);
    u_int32_t *voter = malloc(sizeof(u_int32_t) * MAX_LINE_PRE_CHUNK);
    u_int32_t vote_cnt;

    line = malloc(MAX_LINE_LEN);
    val = NULL;
    vote_cnt = 0;
    valid = FALSE;

    fp = fopen(filename, "r");
    if(fp == NULL)
    {
        printf("[error] %s does not exists\n", filename);
        return FALSE;
    }
    else
    {
        while((read = getline_warpper(&line, &len, fp)) > 0)
        {
            cnt++;
            line_count++;
            if(read>MAX_LINE_LEN)
            {
                printf("[error] %s may out of the range, the length of this string is %zu\n", line, read);
                free(line);
                return FALSE;
            }
            //got enough lines, deal with it
            if(vote_cnt>=MAX_LINE_PRE_CHUNK)
            {
                //TODO: dispatch vote data to vote counter
                count_vote(uid, voter, vote_cnt, dup_vote);
                vote_cnt = 0;
                uid = malloc(sizeof(u_int32_t) * MAX_LINE_PRE_CHUNK);
                voter = malloc(sizeof(u_int32_t) * MAX_LINE_PRE_CHUNK);
            }

            //seprate string by comma and convert it
            valid = FALSE;
            for(cfinder = 0; cfinder<read; cfinder++)
            {
                if (line[cfinder] == ',')
                {
                    valid = TRUE;
                    line[cfinder] = '\0';
                    break;
                }
            }
            if(!valid)
            {
                printf("[error] The input data is invalid!\n %s %d %d\n", line, read, line_count);
                exit(-1);
            }
            *(uid+vote_cnt) = atoi(line);
            *(voter+vote_cnt) = atoi(line+cfinder+1);
            (vote_cnt)++;
        }

        //flush remain data to vote counter
        if(vote_cnt>0)
        {
            count_vote(uid, voter, vote_cnt, dup_vote);
            vote_cnt = 0;
        }

        free(line);
        return TRUE;
    }
}
