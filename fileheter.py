#!/usr/bin/python2.6

import sys
import os

def get_file_list(file_number, prefix):
    file_list = []
    for i in range(0, file_number):
        file_list.append(prefix+str(i))
    return str(file_list).replace('[','').replace(']','').replace('\'','').replace(',','')

RUN_TIME = 30

# File Heterogeneity

# Description:
#       Generate 2^26 votes into a single file, but with an variable a from 1.1 to 5 increased by 0.5. And for each test, it runs for 50 times

FILE_NUM = 100
os.system('rm -f fh_*')
os.system('echo zipf, time, memory, io_time, mutex, mutex_time > fh_all')
for i in range(10, 20, 1):
    print "Test File Heterogeneity, alpha=",str(float(i)/10),' file number=',FILE_NUM,' file_distribution=1.0001'
    os.system('./data_generator.py '+str(float(i)/10)+' '+str(2**20)+' '+str(FILE_NUM)+' 1 fh_test_')
    os.system('./bench_worker.py '+str(RUN_TIME)+' fh_all zipf '+str(i)+' "'+get_file_list(FILE_NUM, 'fh_test_')+'"')
os.system('rm -f fh_test_*')

