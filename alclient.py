'''NOTE:
1.alserver and alclient ,stop_button.txt,stop_button.py,executer6,indnt_exeserver.py should be in the same directory in PC
2.There must be something written in the last three lines after server fxn defn in alserver
3.
4.If even after calling stop, functioning has not stopped then give a few more keystrokes.This might not be rquired in ARBD as log file still gets updated even afer last keyboard event line.
5.IMP:The stop_button.py has to be run every time along with alclient.py or else it won't work prorperly as stop.txt in default condition has 'stop'.
6.Every testcase is saved of the form testcase_name.py, which has the code from indnt_exeserver.py, the lists link and testcase, and also the line sassy(link) (check the format of testcase at ln114)
7.compare fxn won't function properly if any user types "[display-svc] [debug] BRF data :".
8.If execution of whole file is completed, done.txt will have one line called 'done'.
9.done.txt and testcase.py files are buffer in arbd
10. make sure uinstall is installed in the ARBD
11.assuming wut won't get any value other than r ,e or x; make sure of this in GUI linking
yoyo 
'''

'''#for testing errors in a process
i=10
		for line in iter(lambda: p1.stderr.readline(),''):
					print line 
					i=i-1
'''
import os
import paramiko, getpass, re, time
import sys
import traceback
import Tkinter as tk
import time
import subprocess
import socket
from subprocess import Popen,call,PIPE
from executer6 import ex,ex2,di,timeparse,linker,timedifference
def recording(self,path,s,qu,stop_but,rec_error):
	try:
		recordp(self,path,s,qu,stop_but)
	except Exception as e:
		k=traceback.format_exc()
		print 'ayyo'
		print k
                rec_error.put(k)
def recordp(self,path,s,qu,stop_but):
        #elf.listbox1.insert(END,"sonu")
	
	#gives a file of the name testcase_name which has two lists.The first list is parsed one and the second list is unparsed.
	wut='r'
	s.send(wut)			#sending wut
	recv_msg=s.recv(1024)
	print recv_msg
	
	testcase_name=path
	
	qu.put("Recording started,you can start giving keystrokes...")
	print "Recording started,you can start giving keystrokes..." 	

	s.send('continue')
	qwer=0
	testcase=[]	#testcase contains the unparsed lines as srecieved	
	blink=[]		#blink contains parsed lines of the logfile. blink=BRF_BASED_link
	'''blink= [ 'o',b0,[l01],[l02],...,b1,[l11],[l12],...,b2,....,bn,[ln1],[ln2],...,bn_1,........bfinal/[lfinal] ]
	
		where bn = string containg nth BRF data line,bn_1 = string containg (n+1)th BRF data line
		and [lnm] = list of the form : [lnm]=[line,time,['k=uinput.KEY_K1','k=uinput.KEY_K2',...],timediff] .
		line is a string containing Keyboard Event, time is a string, third element is a list of the given format,
		timediff is an int and is the time difference (lnm_1 - lnm)
		b0 might come or might not come based on whether during recording first line from logfile is brfdata or keyboard event	

	'''
	blink.append('o')
	
	
	while qwer==0:
		
		if stop_but.qsize()!=0:
		
			u_input='stop'                           
		else:
			u_input='blah blah'
		
		#stop_button.py waits for 2 seconds after recieving the stop command to actually send stop to alclient.py
		#this is necessary as the last few BRF data lines in the log_file after the last keyboard event line is also required.
		line=s.recv(1024)
		print 'line;',line
		testcase.append(str(line))
		
		if ('BRF data' in line):
			blink.append(line)	
                        
			
		elif ('Keyboard event received' in line):
			ji=ex(line)
			blink.append([line,timeparse(line),ji])
			#print_ln=str(ji) + ' : ' + str(ex2(line))
			print_ln=''		#instead of ex2 and all you could just split the line
			for i in ex2(line):
				if print_ln!='':
					print_ln=print_ln+" + "+str(i)
				else:
					print_ln=str(i)
			print_ln="Keystrokes received: " + print_ln
			print print_ln
			qu.put(print_ln)
			
			#self.listbox1.insert(tk.END,print_ln+'\n')
			#self.listbox1.update_idletasks() 	#or else listbox is updated only after whole fxn is called
		if u_input=='stop':
			s.send('stop')	
			f=s.recv(1024)	
			print f
                        	
			qwer+=1
		
		else:
			
			s.send('continue')

	for i in range(len(blink)-1): #adding timedifference
		if str(type(blink[i]))=="<type 'list'>":
			
			k=i+1
                        
			while k<len(blink)-1:
				if str(type(blink[k]))=="<type 'list'>":
					break
				else:
					k+=1
			print blink[i][1],blink[k][1],blink[k]
                        
			if str(type(blink[k]))=="<type 'list'>":	#to make sure that last line is a keyboard event list
				blink[i].append(timedifference(blink[i][1],blink[k][1]))
	ik=len(blink)-1	
	while ik >0:
		if str(type(blink[ik]))=="<type 'list'>": #adding timediff to last element
			blink[ik].append(0)
			break
		else:
			ik-=1
	
	'''for i in range(len(testcase)-1):
				
			print testcase[i]
                        
			
			print blink[i+1]
                        
			print ' '
        '''                
	  		
    	with open(testcase_name, "w") as f1:
        		
			f1.write(str(blink)+'\n')
			f1.write(str(testcase)+'\n')
			   #to call the function sassy
	print "testcase generated;testcase name:"+testcase_name
	#no need to close files, with automatically closes
	
	#link is the arsed one and testcase is the unparsed.

	
def conn_send(userid,password,Ipaddress,Portnumber,shlf):
		

	try:
		port=int(Portnumber)
		host=str(Ipaddress)
		usr=str(userid)
		pswd=str(password)
		#>>!!host='192.168.7.2'
		#host='192.168.7.2'
		#----------------------------------------------------------------------------------------
		f=open('alserver.py','r')
		lines = f.readlines()
		f.close()

		f=open('alserver.py','w')
		for i in lines[:-4]:
			f.write(i)
	
		f.write('host= "'+host+'"')
		f.write('\nport='+str(port))
		f.write('\npassword= "'+str(pswd)+'"')
		f.write('\nserver(host,port,password)')
		f.close()
#----------------------------------
		f=open('connect.py','r')
		lines = f.readlines()
		f.close()

		f=open('connect.py','w')
		for i in lines[:-4]:
			f.write(i)
	
		f.write('host= "'+host+'"')
		f.write('\nusr= "'+str(usr)+'"')
		f.write('\npassword= "'+str(pswd)+'"')
		f.write('\nconn(host,usr,password)')
		f.close()
		cmd1='python connect.py'
		p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		time.sleep(5)
		'''		
		i=10
		for line in iter(lambda: p1.stderr.readline(),''):
				while i>0:
					print 'lo'
					print line 
					i=i-1
		
		'''
		k=0
		
		shlf.sock=socket.socket()
		shlf.sock.connect((host,port))
		#----------------------------------------------------------------------------------------
		
		'''		
		#file(alserver) sending
		ssh_client =paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		#ssh_client.connect(hostname=host,username='sudhi',password='@3wRETyyUI')
		#ssh_client.connect(hostname=host,username='ubuntu',password='.Book40')
		ssh_client.connect(hostname=host,username=usr,password=pswd)	#ssh_client.connect(host,usr,pswd) won't work because order in which paramters is taken is not same as hostname,username,password
		dir_path = os.path.dirname(os.path.realpath(__file__))
		ftp_client=ssh_client.open_sftp()
		ftp_client.put(dir_path+'/alserver.py','/home/ubuntu/alserver.py')
		time.sleep(1)	
		#file execution here....., also give try except to check if password is correct
		#....
	
		ki=raw_input('Execute alserver in arbd:')	#won't come in final code if file execution works
		shlf.sock=socket.socket()
		shlf.sock.connect((host,port))
		print 'connected'
		'''
	except Exception as e:
		k=traceback.format_exc()
		
                #write messssage box code
		return k
	else:
		return ('connected',shlf.sock,p1)

def compare(resulted_link_l,ideal_link_l):

	#resulted_link_l = resulted_link[l][-1],ideal_link_l = ideal_link[l][q]
	#compares last appended BRF data in resulted_link[l],ideal_link[l] 
	
	
	brf1=resulted_link_l.split("[display-svc] [debug] BRF data :")[-1]
	brf2=ideal_link_l.split("[display-svc] [debug] BRF data :")[-1]
	if brf1==brf2:
		return True
	else:
		return False
	

def execute(self,s,testcase_name,equ1,equ2,equ3):
	wut='e'
	s.send(wut)			#sending wut
	recv_msg=s.recv(1024)
	print recv_msg
	
	with open(testcase_name,'r') as f:
		ideal_link=f.readlines()[0]
		#print ideal_link
		ilink=eval(ideal_link)
		sendlist=[]
		executed=[]
		for line in ilink:
			if "BRF data" in line:
				
				if len(sendlist)==0:
					continue
				s.send(str(sendlist))
				print 'sendlist:'+str(sendlist)
				sendlist=[]
				outbrf=s.recv(1024)
				print outbrf,'<<outbrf',len(outbrf),type(outbrf)
				if not outbrf:
					break
				ibrf = str(line).split(" [display-svc] [debug] BRF data :")[-1]
				
				obrf = eval(outbrf)
				tick = False
				uip ='c'
				tup=[]
				
				print "IDEAL:" + ibrf
				print "RECEIVED:" + str(obrf)
				print ' '
				for string in obrf:
					if not "BRF data" in string:
						continue
					sbrf = str(string).split(" [display-svc] [debug] BRF data :")[-1]
					executed.append(string)
					
					if sbrf == str(ibrf):
						tick = True
						equ1.put(('',ibrf,sbrf,'Pass'))
						break
				if tick is True:
					print "BRF data: " + str(ibrf[-1]) + " matched!"
				else:
					print 'Failed'
					equ1.put(('',ibrf,sbrf,"Fail"))					
					equ3.put('wait')
					kyun='kyun'
					while kyun=='kyun':
						if equ2.qsize()==0:
							#print 'equ2.qsize():' + str(equ2.qsize())
							continue
						else:
							equget=equ2.get()
							kyun='notkyun'
							print 'equ2.get():'+equget
							if equget=='c':
								uip='c'
								
							elif equget=='s':
								uip='s'		
						print 'uip:'+uip
					#uip = raw_input("Test case '" + tc + "' failed: Enter 'c' to continue or 's' to stop:")
				if uip == "s":
					s.send("tervar=1")
					break
			elif not('o' in line):
				#no_key is not sent to alserver
				if line[-2]==['no_key']:
					delta=line[-1]
					time.sleep(delta)  #so that time delay is maintained
					equ1.put(('no_key','','',''))
					print 'no_key_received'
				else:
				
				
					j_1=line[0].split("Keyboard event received: ")[-1][:-1]  #refer ex2 in executer6 for details
					
					equ1.put((j_1,'','',''))
					sendlist.append(line)
					executed.append(line)
		print "Finished executing the testcase:'" + testcase_name
		equ3.put('finished')
	
	
#----------------------------------------------------------------------------------------

'''
#----------------------------------------------------------------------------------------
#host=raw_input('Enter the arbd(server) ip address:')
port=int(raw_input('Enter the port number to which you have to connect:'))
#>>!!host='192.168.7.2'
host='192.168.7.2'
#----------------------------------------------------------------------------------------
f=open('alserver.py','r')
lines = f.readlines()
f.close()

f=open('alserver.py','w')
for i in lines[:-3]:
	f.write(i)
	
f.write('host= "'+host+'"')
f.write('\nport='+str(port))
f.write('\nserver(host,port)')
f.close()
#----------------------------------------------------------------------------------------
#!!>>
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_client.connect(hostname=host,username='sudhi',password='@3wRETyyUI')
ssh_client.connect(hostname=host,username='ubuntu',password='.Book40')
dir_path = os.path.dirname(os.path.realpath(__file__))
ftp_client=ssh_client.open_sftp()
ftp_client.put(dir_path+'/alserver.py','/home/ubuntu/alserver.py')
time.sleep(1)
'''

'''
#__________________________________________________________________________
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,username='ubuntu',password='.Book40')



stdin,stdout,stderr=ssh.exec_command('echo ".Book40" | sudo -S ls')	
lo=stdout.readlines()
print lo

stdin,stdout,stderr=ssh.exec_command('sudo python /home/ubuntu/alserver.py', get_pty = True)
time.sleep(5)
#print stderr.readlines()
#print stdout.readlines()
stdin,stdout,stderr=ssh.exec_command('pgrep -af python')
print stdout.readlines()
print stderr.readlines()
'''
#____________________________________________________________________________
'''
ftp_client.put(dir_path+'/ser.sh','/home/ubuntu/ser.sh')
stdin,stdout,stderr=ssh_client.exec_command("chmod +x ser.sh")
ftp_client.put(dir_path+'/tempo.py','/home/ubuntu/tempo.py')
#ftp_client.put(dir_path+'/alserver.py',dir_path+'/alserversshed.py')
time.sleep(1)
#ftp_client.put(dir_path+ '/ser.sh','/home/ubuntu/ser.sh')
#ftp_client.put(dir_path+'/ser.sh',dir_path+'/ser.sh')
ftp_client.close()

ssh =paramiko.SSHClient()
session = ssh.get_transport().open_session()
session.set_combine_stderr(True)
session.get_pty()
command = 'sudo ./ser.sh'
session.exec_command("sudo bash -c \"" + command + "\"")
stdin = session.makefile('wb', -1)
#stdout = session.makefile('rb', -1)
stdin.write(temppwd + '\n')
stdin.flush()
#print(stdout.read().decode("utf-8"))


ssh = paramiko.SSHClient()


stdin,stdout,stderr=ssh.exec_command('sudo python alserver.py',timeout=15,get_pty=True)
stdin.write('temppwd\n')
stdin.flush()


stdin,stdout,stderr=ssh_client.exec_command("chmod +x ser.sh")
commands = ['sudo -S ./ser.sh true']
channel = ssh_client.invoke_shell()
# clear welcome message and send newline
time.sleep(1)
channel.recv(9999)
channel.send("\n")
for command in commands:
	    channel.send(command + "\n")
	    channel.send("temppwd\n")
	    print "chala"
	    while not channel.recv_ready(): #Wait for the server to read and respond
	        time.sleep(0.1)
	    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
	    output = channel.recv(9999) #read in
print(output.decode('utf-8'))
time.sleep(0.1)
channel.close()
time.sleep(1)

'''

'''
s=socket.socket()
s.connect((host,port))
print 'Connection established,sockets created and connected.'

wut=raw_input("Enter 'r' to record or 'e' to execute a recorded test case or 'x' to exit connection:")
#assuming wut won't get any value other than r ,e or x; make sure of this in GUI linking
while wut !='x':
	s.send(wut)
	recv_msg=s.recv(1024)
	if wut == 'r':
		print 'make sure stop_button.py is STARTED ON ' 
		recordclient(s)
	elif wut == "e":
		tc=raw_input("Please enter the name of test case to be executed(without '.py' or '.txt') :")
		#write code to make sure testcase exists
		execute(s,tc,ssh_client)
	wut=raw_input("Please enter 'r' to record or 'e' to execute a recorded test case or 'x' to exit connection:")


s.send(wut)
s.close()	#closes the socket, keep this at the last, or at the end of the loop

'''

#----------------------------------------------------------------------------------------



		
	
