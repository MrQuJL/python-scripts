from multiprocessing import Process
import os

print('Process (%s) start...' % os.getpid())

#pid = os.fork()

def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())

p = Process(target=run_proc, args=('test',))











