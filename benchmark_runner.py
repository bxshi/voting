#!/usr/bin/python2.6 -W ignore

import sys
import os

TEMP_TIME_LOG = 'tmp_bench_time.log'
TEMP_PROF_LOG = 'tmp_bench_prof.log'
PROF_ARG = 'gprof -b -p vote_count > '+TEMP_PROF_LOG
TIME_ARG = 'time -f "%E;%M" -o "'+TEMP_TIME_LOG+'" -a '

THREAD_OVERHEAD_LIST = ['add_vote', 'remove_vote', 'check_dup', 'init_mutex', 'threadpool_create','threadpool_destroy','threadpool_free']
MUTEX_LIST = ['add_vote', 'remove_vote', 'check_dup']
IO_OVERHEAD_LIST = ['getline_warpper']

def opts(argv):
    params = {}
    params['execution_times'] = int(argv[1])
    params['log_file'] = argv[2]
    params['arg'] = argv[3]
    return params
    
def do_benchmark(arguments):
    
    os.system(TIME_ARG+' vote_count '+arguments)
    os.system(PROF_ARG)
    pass

def accumulate_data():

    # data : time, memory, CPU/IO ratio, thread time, mutex call times

    data = []
    
    f = open(TEMP_TIME_LOG, 'r')
    t = f.read().split('\n')[0].split(';')
    
    for item in t:
        data.append(int(item))
    
    f.close()
    f = open(TEMP_PROF_LOG, 'r')
    prof = f.read().split('\n')
    critical_precent = 0
    io_precent = 0
    mutex_call_times = 0
    for line in prof:
        line = line.split('\t')
        if line[-1] in THREAD_OVERHEAD_LIST :
            critical_precent += float(line[0])
        if line[-1] in IO_OVERHEAD_LIST:
            io_precent += float(line[0])
        if line[-1] in MUTEX_LIST:
            mutex_call_times += int(line[3])
            
    data.append(io_precent/(1-io_precent))
    data.append(data[0] * critical_precent)
    data.append(mutex_call_times)
    
    return data

def main(argv):
    
    print argv
    
    params = opts(argv)
    
    f = open(params['log_file'], 'w')
    f.write('time, memory, ratio, thread, mutex\n')
    
    for i in range(0, params['execution_times']):
        do_benchmark(params['arg'])
        data = accumulate_data()
        for item in data:
            f.write(str(item).replace('[','').replace(']','')+'\n')
    f.close()
    
if __name__ == '__main__':
    main(sys.argv)
