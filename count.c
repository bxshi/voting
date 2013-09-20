#include "constants.h"
#include <pthread.h>
#include <stdio.h>

pthread_mutex_t io_time;
pthread_mutex_t m_call;
pthread_mutex_t m_time;

float io_total_time;
unsigned int m_call_cnt;
float m_time_cnt;

void init_count_mutex(){
	pthread_mutex_init(&io_time, NULL);
	pthread_mutex_init(&m_call, NULL);
	pthread_mutex_init(&m_time, NULL);
	io_total_time = 0;
	m_call_cnt = 0;
	m_time_cnt = 0;
}

void add_io_time(float t){
	pthread_mutex_lock(&io_time);
	io_total_time += t;
	pthread_mutex_unlock(&io_time);
}
void add_mutex_time(float t){
	pthread_mutex_lock(&m_time);
	m_time_cnt += t;
	pthread_mutex_unlock(&m_time);
};
void add_mutex_call(){
	pthread_mutex_lock(&m_call);
	m_call_cnt++;
	pthread_mutex_unlock(&m_call);
};

void output(){
	printf("%f, %d, %f\n", io_total_time, m_call_cnt, m_time_cnt/m_call_cnt);
}
