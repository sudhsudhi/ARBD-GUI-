import time
f=open('stop_button.txt','w')
f.write('blah blah')
f.close()
cmnd=raw_input("To stop recording enter 'stop' ;")
while cmnd!='stop':
	f=open('stop_button.txt','w')
	f.write(cmnd)
	f.close()
	cmnd=raw_input("To stop recording enter 'stop' ;")
f=open('stop_button.txt','w')

f.write('stop')
f.close()
