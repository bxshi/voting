#!/usr/bin/python2.6

import sys
import os

def get_file_list(file_number, prefix):
    file_list = []
    for i in range(0, file_number):
        file_list.append(prefix+str(i))
    return str(file_list).replace('[','').replace(']','').replace('\'','').replace(',','')

# File Heterogeneity

# Description:
#       Generate 2^26 votes into a single file, but with an variable a from 1.1 to 5 increased by 0.5. And for each test, it runs for 50 times

FILE_NUM = 500
os.system('rm -f fh_*')
os.system('echo zipf, time, memory, ratio, thread, mutex > fh_all')
for i in range(10, 50, 5):
    print "Test File Heterogeneity, alpha=",str(float(i)/10),' file number=',FILE_NUM,' file_distribution=1.0001'
    os.system('./data_generator.py '+str(float(i)/10)+' '+str(2**20)+' '+str(FILE_NUM)+' 1 fh_test_')
    os.system('./benchmark_runner.py 50 fh_all zipf '+str(float(i)/10)+' "'+get_file_list(FILE_NUM, 'fh_test_')+'"')
os.system('rm -f fh_test_*')

# Number Files

# Description:
#	Generate 2^26 votes, change distribution from 1 file to 2000 files, each runs 50 times
os.system('rm -f nf_*')
os.system('echo number, time, memory, ratio, thread, mutex > nf_all')
for i in range(1, 500, 50):
    print "Test Number Files"
    os.system('./data_generator.py 1 '+str(2**20)+' '+str(i)+' 1 nf_test_')
    os.system('./benchmark_runner.py 50 nf_all number '+str(i)+' "'+get_file_list(i, 'nf_test_')+'"')
os.system('rm -f nf_test_*')

# File Size Heterogeneity

# Description:
#	Generate 2^20 votes, and for a fixed number of files, the size vary from exponential to heterogeneity
os.system('rm -f fsh_*')
os.system('echo zipf, time, memory, ratio, thread, mutex > fsh_all')
for i in range(10, 50, 5):
    os.system('./data_generator.py 1 '+str(2**20)+' '+str(FILE_NUM)+' '+str(float(i)/10)+' fsh_test_')
    os.system('./benchmark_runner.py 50 fsh_all zipf '+str(float(i)/10)+' "'+get_file_list(FILE_NUM, 'fsh_test_')+'"')
os.system('rm -f fsh_test_*')
