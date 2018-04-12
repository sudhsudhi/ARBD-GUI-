import os,signal

import sys
import time
import subprocess
import socket
from subprocess import Popen,call,PIPE
#p2.stdout.readline not lines
#make sure to remove all print lines in final
def server(host,port):
	s=socket.socket()
	ip=''
	s.bind((ip,port))
	print 'waiting....'
	s.listen(1)
	c,addr=s.accept()
	print 'connected...'
	
	wut=c.recv(1024)
	c.send('recieved wut')
	while str(wut)!='x':
		if str(wut)=='r':
			recordserver(s,c)
			print 'recording'
		elif str(wut)=='e':
			exeserver(s,c)
			print 'executing'
		wut=c.recv(1024)
		c.send('recieved wut')
	s.close()	#close the socket, keep this at the last, or at the end of the loop

def follow(thefile):
	#keeps producing an infinitely long generator wrt time
    thefile.seek(0,2)
    while True:
	
        line = thefile.readline()
	 
        if not line:
            
	    time.sleep(0.1)
            continue
	    		
        yield line

def recordserver(s,c):

		#grep might interfer with stout.read so don't use grep		

		cmd1='ls -t /opt/arbd/logs/ | head -1 '
		#>>!!cmd1='ls -t /home/sudhi/COP/piping| head -1 '
		p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
				
		chi=p1.communicate() 
		
		llf=str(chi[0][:-1]) #llf=latest log file
		
		
		cmd2='tail -0f /opt/arbd/logs/' + llf   
		 
		#>>!!cmd2='tail -0f /home/sudhi/COP/piping/' + llf 
		#cmd2='sudo sh -c "tail -0f /home/sudhi/COP/arbd.log_2018-03-12_12-33 | grep  -E Keyboard.*event\|BRF.*data > /home/sudhi/COP/working_temporary/temp_log.txt" ' 	#make sure there is no space bw ' and sudo	
		p2 = subprocess.Popen(cmd2, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		#p2.stdin.write("temppwd\n")
		#p2.stdin.flush()
		#p2.stdin.write("@3wRETyyUI\n") #can't use communicate here because communicate will wait for process to terminate
		
		
		
		lenl=0
		
    		for line in iter(lambda: p2.stdout.readline(),''):
			if ('Keyboard event' in line) or ("BRF data" in line):			
				msg=c.recv(1024)
				#print line
				if msg=='continue':
					#print line
					
					c.send(line)
			
				if msg=='stop':
					p2.kill()	 #stops recording
					print 'os'					
					c.send('recording stopped')	
					break
		
def exeserver(s,c):
		#waits for 2 secs to make sure testcase has been received
		#grep might interfer with stout.read so don't use grep		
		
		cmd1='ls -t /opt/arbd/logs/ | head -1 '
		#>>!!cmd1='ls -t /home/sudhi/COP/piping| head -1 '
		p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
				
		chi=p1.communicate() 
		
		llf=str(chi[0][:-1]) #llf=latest log file
		
		
		cmd2='tail -0f /opt/arbd/logs/' + llf   
		 
		tc=c.recv(1024) #this line makes sure that testcase has been sent here, tc will be testcase_name
		time.sleep(2)	#further surety
		p2 = subprocess.Popen(cmd2, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		c.send('recording started')
		print 'recording started'
		msg=c.recv(1024) #msg will be 'start execution'
		
		
		cmd3='echo .Book40 | sudo -S python '+'/home/ubuntu/'+str(tc)
		p3 = subprocess.Popen(cmd3, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		print cmd3
		i=0	
		
		#for line in iter(lambda: p3.stderr.readline(),''):
			#while i<10:
				#i+=1
				#print line
					

		p4=subprocess.Popen('pgrep -af python', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		chi=p4.communicate() 
		print chi

		c.send('execution of testcase started')		
		print 'execution started'
		l=[]
		lenl=0
		
    		for line in iter(lambda: p2.stdout.readline(),''):		#p2.stdout.readline not lines
			
			if ('Keyboard event' in line) or ("BRF data" in line):			
				msg=c.recv(1024)
				
				if msg=='continue':
					#print line
					l.append(line)
					c.send(line)
				with open('done.txt','r') as f:
					k=f.readline()
					if k=='done':	#this means whole testcaes has been executed
						msg='stop2'
				if msg=='stop2':			
					c.send('Finished executing testcase')
					
					break
				if msg=='stop':			
					c.send('recording stopped')
					
					break
						
		
		os.killpg(os.getpgid(p3.pid), signal.SIGTERM) 	 #stops execution			
		os.killpg(os.getpgid(p2.pid), signal.SIGTERM) 	 #stops recording
		os.remove("done.txt")
		os.remove(str(tc))
host= "192.168.7.2"
port=9533
server(host,port)
