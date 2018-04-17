import os,signal
 
import sys
import time
import subprocess
import socket
from subprocess import Popen,call,PIPE
#p2.stdout.readline not lines
#make sure to remove all print lines in final
def server(host,port,pwd):
	s=socket.socket()
	ip=''
	s.bind((ip,port))
	print 'waiting....'
	s.listen(1)
	c,addr=s.accept()
	print 'connected...'
	
	wut='p'
	while str(wut)!='x':
		wut=c.recv(1024)
		
		c.send('received wut:'+wut)
	
		if str(wut)=='r':
			
			recordserver(s,c)
			print 'recording'
		elif str(wut)=='e':
			exeserver(s,c)
			print 'executing'
	if wut == 'x':
	
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
	#updated latest UI	
	l = 0
	cmd1='ls -t /opt/arbd/logs/ | head -1 '
	p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
	chi=p1.communicate() # don't write \n
	llf=str(chi[0][:-1]) #llf=latest log file
	#print chi[0][:-1]
	tervar=0
	cmd2='tail -0f /opt/arbd/logs/' + llf	#should grep be removed? will it interact with stdout? 
	while tervar==0:
		pp2 = subprocess.Popen(cmd2, stdin=PIPE, stdout=PIPE, stderr=PIPE,shell=True)
		#pid = os.getpgid(pp2.pid)
		recvlist=c.recv(1024)
		#print recvlist
		if recvlist=="tervar=1":
			break
		rlist = eval(recvlist)
		print 'rlist: '+str(rlist)		#rlist=[[ln1],[ln2],...], [ln1]= one keyboard event line with many keys(key_A,key_B,etc..)
		for rkeys in rlist:
			
			combo=rkeys[-2]
			delta=rkeys[-1]
			combo_list=[]
			#print combo_list
			if not ("no_key" in combo):		#if Keyboard_event line was empty			
				for i in combo:
					if i!= "Key_not_yet_defined":
						print 'i:    ' +str(i)
						exec(i) in globals(), locals()	# i = 'k=uinput.KEY_KN' #globals,locals because exec cannot be used inside a function which calls a subfunction(iter here)
 						combo_list.append(k)
					elif i== "Key_not_yet_defined":
						print "Recieved a not defined key, neglected it!"
			Keyboard.emit_combo(combo_list)
			print "combo_list: "+str(combo_list)
			#print "Keyboard event executed."
			time.sleep(delta)
		obrf=[]
		sv = 0
		rov=''
		#obrf will store all brf lines until all keyboard events has been executed. After all keyboard events has been executed it will store the brf lines that come within 500 ms.
		for line in iter(lambda: pp2.stdout.readline(),''):
			
			if " [display-svc] [debug] BRF data :" in line:
				obrf.append(line)
				print 'brf line: '+line
				
			elif "Keyboard event" in line and sv!=len(rlist):   #second condition because Keyboard event lines were coming even after sv == len(rlist)
				sv+=1
				print "keyboard line:" +line
				print 'sv:'+str(sv)
			
			if rov == 'bits_more':
					#print "Recording a bit more"
					#print datetime.datetime.now().time(), nxt.time()
					
					if datetime.datetime.now().time() > nxt.time():
						#print datetime.datetime.now().time() > nxt.time()
						break

			elif sv == len(rlist):
					print "All keyboard events recorded" 
					rov='bits_more'
					current=datetime.datetime.now()
					nxt=current+datetime.timedelta(0,0,0,500)
					#datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]]
			
		#subprocess.call(os.killpg(pid, signal.SIGTERM))
		
		pp2.terminate()	
		print obrf
		c.send(str(obrf)+'yolo')	#only 2 brf data lines are sent atmost
		

host= "192.168.7.2"
port=9562
password= "temppwd"
server(host,port,password)
