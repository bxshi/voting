//
//  vote_counter.c
//  assign1
//
//  Created by Baoxu Shi on 13-8-30.
//  Copyright (c) 2013年 Baoxu Shi. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#include "constants.h"
#include "uthash.h"
#include "count.h"
#include "time.h"

#define HASH_NUM 256
#define HASH_MASK 0xff //HASH_MASK should <= HASH_NUM

//initialize hash table
struct vote_result *vr = NULL;
struct vote_history *vh = NULL;

pthread_mutex_t vr_lock;
pthread_mutex_t vh_lock;

int mutex_lock_warpper(pthread_mutex_t *mutex){
	int res;
	float seconds;
	clock_t start,end;
	add_mutex_call();
	start = clock();
	res = pthread_mutex_lock(mutex);
	end = clock();
	add_mutex_time((float)(end-start)/CLOCKS_PER_SEC);
	return res;
}

int mutex_unlock_warpper(pthread_mutex_t *mutex){
	int res;
	float seconds;
	clock_t start,end;
	start = clock();
	res = pthread_mutex_unlock(mutex);
	end = clock();
	add_mutex_time((float)(end-start)/CLOCKS_PER_SEC);
	return res;
} 

struct result_chunk
{
    struct vote_result *vr;
    pthread_mutex_t vr_lock;

    struct vote_history *vh;
    pthread_mutex_t vh_lock;
};

struct result_chunk *rc_list;

void init_mutex()
{

    int i;
    rc_list = malloc(sizeof(struct result_chunk) * HASH_NUM);
    for(i = 0; i< HASH_NUM; i++)
    {
        rc_list[i].vr = NULL;
        rc_list[i].vh = NULL;
        pthread_mutex_init(&(rc_list[i].vr_lock), NULL);
        pthread_mutex_init(&(rc_list[i].vh_lock), NULL);
    }

    pthread_mutex_init(&vr_lock, NULL);
    pthread_mutex_init(&vh_lock, NULL);
}

int hash_locator(u_int32_t uid)
{
    return uid & HASH_MASK;
}

//maybe copy pointer is faster than copy int?
void add_vote(u_int32_t vote)
{
    struct vote_result *p;
    struct result_chunk *rc;

    rc = &rc_list[hash_locator(vote)];
    mutex_lock_warpper(&(rc->vr_lock));
    HASH_FIND_INT(rc->vr, &vote, p);
    if(!p)
    {
        p = malloc(sizeof(struct vote_result));
        p->uid = vote;
        p->count = 1;
        HASH_ADD_INT(rc->vr, uid, p);
    }
    else
    {
        p->count++;
    }
    mutex_unlock_warpper(&(rc->vr_lock));

}

void remove_vote(u_int32_t vote)
{
    struct vote_result *p;
    struct result_chunk *rc;

    rc = &rc_list[hash_locator(vote)];

    mutex_lock_warpper(&(rc->vr_lock));
    HASH_FIND_INT(rc->vr, &vote, p);
    if(!p)
    {
        printf("[error]");
    }
    else
    {
        p->count--;
    }
    mutex_unlock_warpper(&(rc->vr_lock));

};

short check_dup(u_int32_t uid, u_int32_t vote)
{
    struct vote_history *p;
    struct result_chunk *rc;

    rc = &rc_list[hash_locator(uid)];

    mutex_lock_warpper(&(rc->vh_lock));
    HASH_FIND_INT(rc->vh, &uid, p);
    if(!p)
    {
        //first vote
        p = malloc(sizeof(struct vote_history));
        p->uid = uid;
        p->vote = vote;
        HASH_ADD_INT(rc->vh, uid, p);
        mutex_unlock_warpper(&(rc->vh_lock));

        return FALSE;
    }
    else
    {
        //dup vote
        if(p->vote!=0)
        {
            //remove vote
            remove_vote(p->vote);
            p->vote = 0;
        }
        mutex_unlock_warpper(&(rc->vh_lock));

        return TRUE;
    }
}

void count_vote(unsigned int uid, unsigned int vid, int vote_cnt, int dup_vote)
{
    int cnt;

    cnt = 0;

    while(cnt<vote_cnt)
    {

        if(dup_vote)
        {
            if(!check_dup(uid, vid))
            {
                //not dup
                add_vote(vid);
            }
        }
        else
        {
            add_vote(vid);
        }
        cnt++;
    }
}

int sort_func(struct vote_result *a, struct vote_result *b)
{
    return b->count - a->count;
};

void get_vote_result(int rank)
{
    struct vote_result *p, *tmp, *maxp;
    int i, j, count, uid, hash_cnt;

    j = 0;

    while(rank>j)
    {

        count = 0;
        hash_cnt = -1;
        maxp = NULL;

        for(i=0; i<HASH_NUM; i++)
        {
            if(rc_list[i].vr)
            {
                HASH_ITER(hh,rc_list[i].vr,p,tmp)
                {
                    if((p->count) > count)
                    {
                        uid = p->uid;
                        count = p->count;
                        maxp = p;
                        hash_cnt = i;
                    }
                }
            }
        }

        maxp->count = 0;
	j++;
        //printf("%d,%d,%d\n", ++j, uid, count);
    }

}

