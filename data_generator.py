#!/usr/bin/python2.6 -W ignore

import sys
import numpy
import random

MAX_INT32 = 0xffffffff

def error():
    print "usage: \n"
    exit()

def opts(argv):
    params = {}
    params['zipf_alpha'] = float(argv[1])
    params['vote_number'] = int(argv[2])
    params['file_number'] = int(argv[3])
    params['file_zipf_alpha'] = float(argv[4])
    params['file_prefix'] = argv[5]
    return params

def generate_votes(alpha, total_number):
    votes = numpy.random.zipf(alpha, total_number) % (MAX_INT32+1)
    print votes
    return votes

def get_file_id(alpha, file_number):
    return numpy.random.zipf(alpha) % file_number

def write_votes(votes, file_number, alpha, prefix):
    file_list = []
    for i in range(0, file_number):
        file_list.append(open(prefix+str(i), 'w'))
    
    while len(votes) > 0:
        try:
            v = str(votes.pop())
            fid = file_list[get_file_id(alpha, len(file_list))]
            fid.write(str(random.getrandbits(32))+','+str(v)+'\n')
        except IndexError:
            break;
    
    for i in range(0, len(file_list)):
        file_list[i].close()

def main(argv):
    if len(sys.argv) < 6:
        error
    print argv
    params = opts(argv)
    
    votes = list(generate_votes(params['zipf_alpha'], params['vote_number']))
    
    write_votes(votes, params['file_number'], params['file_zipf_alpha'], params['file_prefix'])
    
if __name__ == "__main__":
    main(sys.argv)