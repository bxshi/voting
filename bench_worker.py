#!/usr/bin/python2.6 -W ignore

import sys
import os
import re

TEMP_TIME_LOG = 'tmp_bench_time.log'
TEMP_PROF_LOG = 'tmp_bench_prof.log'
TIME_ARG = '/usr/bin/time -f "%e;%M" -o "'+TEMP_TIME_LOG+'" '

def opts(argv):
    params = {}
    params['execution_times'] = int(argv[1])
    params['log_file'] = argv[2]
    params['custom_col'] = argv[3]
    params['custom_val'] = float(argv[4])
    params['arg'] = argv[5]
    return params
    
def do_benchmark(arguments):
   
    print TIME_ARG, ' vote_count ', arguments 
    os.system(TIME_ARG+' vote_count '+arguments+' > '+TEMP_PROF_LOG)
    pass

def accumulate_data(custom_val):

    # data : custom_col, time, memory, CPU/IO ratio, thread time, mutex call times

    data = []
    
    f = open(TEMP_TIME_LOG, 'r')
    t = f.read().split('\n')[0].split(';')
    print t 
    data.append(custom_val) 
    data.append(float(t[0]))
    data.append(int(t[1]))
    
    f.close()
    f = open(TEMP_PROF_LOG, 'r')
    prof = f.read().split('\n')[0].split(',')
    print prof
    io_time = float(prof[0]);
    mutex_call = int(prof[1]);
    average_mutex_time = float(prof[2]);

    data.append(io_time)
    data.append(mutex_call)
    data.append(average_mutex_time)
    
    return data

def main(argv):
    
    params = opts(argv)
    
    f = open(params['log_file'], 'aw')
    #f.write(params['custom_col']+', time, memory, ratio, thread, mutex\n')
    
    for i in range(0, params['execution_times']):
        do_benchmark(params['arg'])
        data = accumulate_data(params['custom_val'])
	print data
        f.write(str(data).replace('[','').replace(']',''))
	f.write('\n')

    f.close()
    
if __name__ == '__main__':
    main(sys.argv)
