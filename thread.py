'''
import threading,multiprocessing

def recording():
	for i in range(1,100000):
		
		print i



p=multiprocessing.Process(target=recording)
p.start()

print "Thread started...."
p.join()
print "fgh"

'''

'''
h=open('rec_out.txt','r')
def follow(thefile):
	#keeps producing an infinitely long generator wrt time
    thefile.seek(0,2)

    while True:
	
        line = thefile.readline()
	 
        if not line:
            
	    time.sleep(0.1)
	    with open('stop_button.txt') as fd:
		w=fd.readline()
		
	    print w=='stop'
	    if w=='stop':
			
			print ';lk'
			break
			
            else:
		continue
	    		
        yield line

for i in follow(h):
	print i
'''
from multiprocessing import Queue

qu=Queue()
qu.put('dd')
while qu.qsize()!=0:
	print qu.get()
	k=raw_input('not h')
	if k == 'h':
		break
	qu.put(k)
	





