#!/usr/bin/python2.6 -W ignore

import sys
import os
import re

TEMP_TIME_LOG = 'tmp_bench_time.log'
TEMP_PROF_LOG = 'tmp_bench_prof.log'
PROF_ARG = 'gprof -b -p vote_count > '+TEMP_PROF_LOG
TIME_ARG = '/usr/bin/time -f "%E;%M" -o "'+TEMP_TIME_LOG+'" '

THREAD_OVERHEAD_LIST = ['add_vote', 'remove_vote', 'check_dup', 'init_mutex', 'threadpool_create','threadpool_destroy','threadpool_free']
MUTEX_LIST = ['add_vote', 'remove_vote', 'check_dup']
IO_OVERHEAD_LIST = ['getline_warpper']

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
    os.system(TIME_ARG+' vote_count '+arguments)
    os.system(PROF_ARG)
    pass

def accumulate_data(custom_val):

    # data : custom_col, time, memory, CPU/IO ratio, thread time, mutex call times

    data = []
    
    f = open(TEMP_TIME_LOG, 'r')
    t = f.read().split('\n')[0].split(';')
   
    data.append(custom_val) 
    data.append(float(t[0].split(':')[0])*60 + float(t[0].split(':')[1]))
    data.append(int(t[1]))
    
    f.close()
    f = open(TEMP_PROF_LOG, 'r')
    prof = f.read().split('\n')[4:]
    critical_precent = 0
    io_precent = 0
    mutex_call_times = 0
    for line in prof:
	
        line = re.sub(' +',' ',line).split(' ')
        if line[-1] in THREAD_OVERHEAD_LIST :
            critical_precent += float(line[1])
        if line[-1] in IO_OVERHEAD_LIST:
            io_precent += float(line[1])
        if line[-1] in MUTEX_LIST:
            mutex_call_times += int(line[4])
            
    data.append(float(io_precent)/float(100-io_precent))
    data.append(data[1] * critical_precent/100)
    data.append(mutex_call_times)
    
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
