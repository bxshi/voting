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
    if(alpha == 1):
        votes = []
        for i in xrange(0, total_number):
	    votes.append(random.getrandbits(32))
        return votes

    votes = numpy.random.zipf(alpha, total_number)
    return votes

def get_file_id(alpha, file_number):
    return numpy.random.zipf(alpha) % file_number

def write_votes(votes, file_number, alpha, prefix):
    file_list = []
    data_list = []
    for i in xrange(0, file_number):
        data_list.append([])

    print "divide votes into seperate bucket"   
    bucket = generate_votes(alpha, len(votes))
    print "bucket initalized"
    for i in xrange(0, len(votes)):
        try:
            if votes[i] > MAX_INT32:
                votes[i] = votes[i] % (MAX_INT32+1)
            if bucket[i] > file_number:
                bucket[i] = bucket[i] % file_number
            data_list[bucket[i]].append(votes[i])
        except IndexError:
	    print i, votes[i]
            print bucket[i]
            print len(data_list)

    print "save votes into files" 
    for i in xrange(0, file_number):
        f = open(prefix+str(i), 'w')
        for item in data_list[i]:
            f.write(str(random.getrandbits(32))+','+str(item)+'\n')
        f.close()

def main(argv):
    if len(sys.argv) < 6:
        error
    print argv
    params = opts(argv)
    print "generate votes...\n"
    votes = list(generate_votes(params['zipf_alpha'], params['vote_number']))
    print "vote generated, start writing\n" 
    write_votes(votes, params['file_number'], params['file_zipf_alpha'], params['file_prefix'])
    
if __name__ == "__main__":
    main(sys.argv)
