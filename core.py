#!/usr/bin/python2.6

import sys
import os

def get_file_list(file_number, prefix):
    file_list = []
    for i in range(0, file_number):
        file_list.append(prefix+str(i))
    return str(file_list).replace('[','').replace(']','').replace('\'','').replace(',','')

RUN_TIME = 30

# Cores

# Description:

FILE_NUM = 100
VOTE_NUM = 1000000
os.system('rm -f c_*')
os.system('echo number, time, memory, io_time, mutex, mutex_time> c_all')
os.system('./data_generator.py 1 '+str(VOTE_NUM)+' '+str(FILE_NUM)+' 1 c_test_')
for i in range(1, 22, 1):
    print "Test Cores, core_count=",str(i),' file count=',FILE_NUM,' vote count=',VOTE_NUM
    os.system('./bench_worker.py '+str(RUN_TIME)+' c_all number '+str(i)+' "-cores '+str(i)+' '+get_file_list(FILE_NUM, 'c_test_')+'"')
os.system('rm -f c_test_*')

