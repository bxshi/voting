#!/usr/bin/python2.6

import sys
import os

def get_file_list(file_number, prefix):
    file_list = []
    for i in range(0, file_number):
        file_list.append(prefix+str(i))
    return str(file_list).replace('[','').replace(']','').replace('\'','').replace(',','')

RUN_TIME = 30

# Number Files

# Description:
#	Generate 2^26 votes, change distribution from 1 file to 2000 files, each runs 50 times
os.system('rm -f nf_*')
os.system('echo number, time, memory, io_time, mutex, mutex_time > nf_all')
for i in range(1, 150, 10):
    print "Test Number Files"
    os.system('./data_generator.py 1 '+str(2**20)+' '+str(i)+' 1 nf_test_')
    os.system('./bench_worker.py '+str(RUN_TIME)+' nf_all number '+str(i)+' "'+get_file_list(i, 'nf_test_')+'"')
os.system('rm -f nf_test_*')
