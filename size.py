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

FILE_NUM = 1
os.system('rm -f size_*')
os.system('echo number, time, memory, ratio, thread, mutex > size_all')
for i in range(26, 28, 2):
    
    os.system('./data_generator.py 1 '+str(2**i)+' '+str(FILE_NUM)+' 1 size_test_')
    os.system('./bench_worker.py '+str(RUN_TIME)+' size_all number '+str(2**i)+' "-cores 1 '+get_file_list(FILE_NUM, 'size_test_')+'"')
os.system('rm -f size_test_*')

