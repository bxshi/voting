//
//  vote_counter.h
//  assign1
//
//  Created by Baoxu Shi on 13-8-30.
//  Copyright (c) 2013年 Baoxu Shi. All rights reserved.
//

#ifndef assign1_vote_counter_h
#define assign1_vote_counter_h
void init_mutex();
int count_vote(unsigned int uid, unsigned int vid, int vote_cnt, int dup_vote);
void add_vote(u_int32_t vote);

void get_vote_result(int rank);

#endif
