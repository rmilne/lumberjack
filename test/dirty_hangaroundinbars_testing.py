#!/usr/bin/env python

import json
import os
import subprocess
import sys
import time

settings = {
        'log_path': './test.log',
        'log_splits': {
            'match.log': ['test log 5', 'log 7']
            },
        'rest': 3
        }


with open('test_settings.json', 'w') as f:
    json.dump(settings, f)

def write_logs(lines=10):
    with open(settings['log_path'], 'a') as logfile:
        for x in range(lines):
            logfile.write('test log %s\n' % x)
            time.sleep(0.1)

def remove_logs():
    print 'removing inode %s' % os.stat(settings['log_path']).st_ino
    os.unlink(settings['log_path'])

def count_lines(path):
    try:
        with open(path) as f:
            lines = [l for l in f.readlines()]
            print '%s : %s' % (len(lines), path)
            print lines
            print 'inode %s' % os.stat(path).st_ino
            return len(lines)
    except Exception as e:
        print 'exception %s' % e
        pass
    return 0

p = subprocess.Popen(['../lumberjack.py', 'test_settings.json'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print 'write logs'
write_logs()
count_lines(settings['log_path'])
time.sleep(4)
print
count_lines('match.log')
count_lines('test.log.offset')
#remove_logs()
os.rename('test.log', 'test.log.old')

write_logs(6)
time.sleep(8)
print
count_lines(settings['log_path'])
count_lines('match.log')
count_lines('test.log.offset')

remove_logs()
p.kill()

try:
    os.unlink('match.log')
    os.unlink('test.log.offset')
except Exception as e:
    print 'exception deleting files: %s' % e
