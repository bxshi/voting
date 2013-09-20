#!/usr/bin/python2.6

import sys
import os

def get_file_list(file_number, prefix):
    file_list = []
    for i in range(0, file_number):
        file_list.append(prefix+str(i))
    return str(file_list).replace('[','').replace(']','').replace('\'','').replace(',','')

RUN_TIME = 30 

# Block Size

# Description:

FILE_NUM = 10
VOTE_NUM = 1000000
os.system('rm -f bs_*')
os.system('echo number, time, memory, io_time, mutex, mutex_time  > bs_all')
os.system('./data_generator.py 1 '+str(VOTE_NUM)+' '+str(FILE_NUM)+' 1 bs_test_')
print('./data_generator.py 1 '+str(VOTE_NUM)+' '+str(FILE_NUM)+' 1 bs_test_')
for i in range(20, 1000000, 100000):
    print "Test Block Size, block_size=",str(i),' file count=',FILE_NUM,' vote count=',VOTE_NUM
    os.system('./bench_worker.py '+str(RUN_TIME)+' bs_all number '+str(i)+' "-blocksize '+str(i)+' '+get_file_list(FILE_NUM, 'bs_test_')+'"')
    print('./bench_worker.py '+str(RUN_TIME)+' bs_all number '+str(i)+' "-blocksize '+str(i)+' '+get_file_list(FILE_NUM, 'bs_test_')+'"')
os.system('rm -f bs_test_*')

