#!/usr/bin/python2.6

import sys
import os

def get_file_list(file_number, prefix):
    file_list = []
    for i in range(0, file_number):
        file_list.append(prefix+str(i))
    return str(file_list).replace('[','').replace(']','').replace('\'','')

# File Heterogeneity

# Description:
#       Generate 2^26 votes into a single file, but with an variable a from 1.1 to 5 increased by 0.5. And for each test, it runs for 50 times

for i in range(11, 12, 5):
    os.system('./data_generator.py '+str(float(i)/10)+' '+str(2**10)+' 10 1.1 fh_test_')
    os.system('./benchmark_runner.py 1 fh_res_'+str(i)+' "'+get_file_list(50, 'fh_test_')+'"')