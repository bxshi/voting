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
#include <fcntl.h>
#include <time.h>
#include "file_reader.h"
#include "constants.h"
#include "vote_counter.h"
#include "count.h"


ssize_t read_warpper(float *t, int fildes, void *buf, size_t nbyte);
ssize_t read_warpper(float *t, int fildes, void *buf, size_t nbyte){
	ssize_t rtn ;
        float  seconds;
        clock_t start, end;
        start  = clock();
        rtn = read(fildes, buf, nbyte);
	end = clock();
	*t = (float)(end - start) / CLOCKS_PER_SEC; 
	add_io_time(*t);
        return rtn;
}

//read file by lines, and dispatch them to a vote counter
int readfile(void *arg)
{
    float total_read_time = 0;
    char *filename;
    int dup_vote;
    filename = ((file_struct *)arg)->filename;
    dup_vote = ((file_struct *)arg)->dup_vote;
    
    int fd;
    long block_size = ((file_struct *)arg)->block_size;
    unsigned char buffer[block_size+1];
    int bytesRead = 0;
    char *line;
    char *beg;
    char *end;
    char remainder[32];
    int pairReady = 1;
    unsigned int uid = 0;
    unsigned int vid = 0;
    
    remainder[0] = '\0';
    fd = open(filename, O_RDONLY);
    
    while((bytesRead = read_warpper(&total_read_time, fd, buffer, block_size)) > 0 )
    {
        buffer[block_size] = '\0';
        beg = end = buffer;
        
        if (uid>0){
            // There was a uid from the previous buffer
            end = strchr(beg,'\n');
            if (end!=NULL){
                end[0] = '\0';
                if (remainder[0]!='\0' && remainder[0]!=EOF){
                    // Add data from new buffer the remainder
                    char* tmp = remainder+strlen(remainder);
                    strcpy(tmp,beg);
                    vid = atoi(remainder);
                    remainder[0] = '\0';
                } else {
                    vid = atoi(beg);
                }
                beg = end+1;
                pairReady = 1;
            } else {
                // The file must be over because there is no newline
                vid = atoi(beg);
                pairReady = 1;
            }
        } else {
            end = strchr(beg,',');
            if (end!=NULL){
                end[0] = '\0';
                if (remainder[0]!='\0'){
                    // Add data from new buffer the remainder
                    char* tmp = remainder+strlen(remainder);
                    strcpy(tmp,beg);
                    uid = atoi(remainder);
                    remainder[0] = '\0';
                } else {
                    uid = atoi(beg);
                }
                beg = end+1;

                // Find end of voteID in string
                end = strchr(beg,'\n');
                if (end!=NULL){
                    end[0] = '\0';
                    vid = atoi(beg);
                    beg = end+1;
                    pairReady = 1;

                } else {
                    // The file must be over because there is no newline
                    vid = atoi(beg);
                    pairReady = 1;
                }
            }
        }
        if (pairReady){
            
            
            // Cast the votes
            // Any changes here need to be made to the identical code below
            count_vote(uid, vid, 1, dup_vote);
            
            uid = 0;
            vid = 0;
        }
        while(end>0) {
            // Find end of userID in string
            line = beg;
            end = strchr(beg,',');
            if (end!=NULL){
                end[0] = '\0';
                uid = atoi(beg);
                beg = end+1;
                
                // Find end of voteID in string
                end = strchr(beg,'\n');
                if (end!=NULL){
                    end[0] = '\0';
                    vid = atoi(beg);
                    beg = end+1;
                    
                    
                    // Cast the votes
                    // Any changes here need to be made to the identical code above
                    count_vote(uid, vid, 1, dup_vote);
                    
                    
                    uid = 0;
                    vid = 0;

                } else strcpy(remainder,beg);
            } else strcpy(remainder,beg);
        }
    }
    
}
