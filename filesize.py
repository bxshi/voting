#!/usr/bin/python2.6

import sys
import os

def get_file_list(file_number, prefix):
    file_list = []
    for i in range(0, file_number):
        file_list.append(prefix+str(i))
    return str(file_list).replace('[','').replace(']','').replace('\'','').replace(',','')

RUN_TIME = 30
FILE_NUM = 100

# File Size Heterogeneity

# Description:
#	Generate 2^20 votes, and for a fixed number of files, the size vary from exponential to heterogeneity
os.system('rm -f fsh_*')
os.system('echo zipf, time, memory, io_time, mutex, mutex_time > fsh_all')
for i in range(10,20,1):
    os.system('./data_generator.py 1 '+str(2**20)+' '+str(FILE_NUM)+' '+str(float(i)/10)+' fsh_test_')
    os.system('./bench_worker.py '+str(RUN_TIME)+' fsh_all zipf '+str(i)+' "'+get_file_list(FILE_NUM, 'fsh_test_')+'"')
os.system('rm -f fsh_test_*')
