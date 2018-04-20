import os,signal,uinput
 
import sys,signal
import time,datetime
import subprocess
import socket
from subprocess import Popen,call,PIPE
#p2.stdout.readline not lines
#make sure to remove all print lines in final

print 'pid:'+ str(os.getpid())
global Keyboard
Keyboard = uinput.Device([uinput.KEY_RESERVED, uinput.KEY_1, uinput.KEY_2, uinput.KEY_3, uinput.KEY_4, uinput.KEY_5, uinput.KEY_6
,    uinput.KEY_7 #8
,    uinput.KEY_8 #9
,    uinput.KEY_9 #10
,    uinput.KEY_0 #11
,    uinput.KEY_MINUS #12
,    uinput.KEY_EQUAL #13
,    uinput.KEY_BACKSPACE #
,    uinput.KEY_TAB #
,    uinput.KEY_Q #
,    uinput.KEY_W #
,    uinput.KEY_E #
,    uinput.KEY_R #
,    uinput.KEY_T #
,    uinput.KEY_Y #
,    uinput.KEY_U #
,    uinput.KEY_I #
,    uinput.KEY_O #
,    uinput.KEY_P #
,    uinput.KEY_LEFTBRACE #
,    uinput.KEY_RIGHTBRACE #
,    uinput.KEY_ENTER #
,    uinput.KEY_LEFTCTRL #
,    uinput.KEY_A #
,    uinput.KEY_S #
,    uinput.KEY_D #
,    uinput.KEY_F #
,    uinput.KEY_G #
,    uinput.KEY_H #
,    uinput.KEY_J #
,    uinput.KEY_K #
,    uinput.KEY_L #
,    uinput.KEY_SEMICOLON #
,    uinput.KEY_APOSTROPHE #
,    uinput.KEY_GRAVE #
,    uinput.KEY_LEFTSHIFT #
,    uinput.KEY_BACKSLASH #
,    uinput.KEY_Z #
,    uinput.KEY_X #
,    uinput.KEY_C #
,    uinput.KEY_V #
,    uinput.KEY_B #
,    uinput.KEY_N #
,    uinput.KEY_M #
,    uinput.KEY_COMMA #
,    uinput.KEY_DOT #
,    uinput.KEY_SLASH
,    uinput.KEY_RIGHTSHIFT
,    uinput.KEY_KPASTERISK
,    uinput.KEY_LEFTALT
,    uinput.KEY_SPACE
,    uinput.KEY_CAPSLOCK
,    uinput.KEY_F1
,    uinput.KEY_F2
,    uinput.KEY_F3
,    uinput.KEY_F4
,    uinput.KEY_F5
,    uinput.KEY_F6
,    uinput.KEY_F7
,    uinput.KEY_F8
,    uinput.KEY_F9
,    uinput.KEY_F10
,    uinput.KEY_NUMLOCK
,    uinput.KEY_SCROLLLOCK
,    uinput.KEY_KP7
,    uinput.KEY_KP8
,    uinput.KEY_KP9
,    uinput.KEY_KPMINUS
,    uinput.KEY_KP4
,    uinput.KEY_KP5
,    uinput.KEY_KP6
,    uinput.KEY_KPPLUS
,    uinput.KEY_KP1
,    uinput.KEY_KP2
,    uinput.KEY_KP3
,    uinput.KEY_KP0
,    uinput.KEY_KPDOT
,    uinput.KEY_ZENKAKUHANKAKU
,    uinput.KEY_102ND
,    uinput.KEY_F11
,    uinput.KEY_F12
,    uinput.KEY_RO
,    uinput.KEY_KATAKANA
,    uinput.KEY_HIRAGANA
,    uinput.KEY_HENKAN
,    uinput.KEY_KATAKANAHIRAGANA
,    uinput.KEY_MUHENKAN
,    uinput.KEY_KPJPCOMMA
,    uinput.KEY_KPENTER
,    uinput.KEY_RIGHTCTRL
,    uinput.KEY_KPSLASH
,    uinput.KEY_SYSRQ
,    uinput.KEY_RIGHTALT
,    uinput.KEY_LINEFEED
,    uinput.KEY_HOME
,    uinput.KEY_UP
,    uinput.KEY_PAGEUP
,    uinput.KEY_LEFT
,    uinput.KEY_RIGHT
,    uinput.KEY_END
,    uinput.KEY_DOWN
,    uinput.KEY_PAGEDOWN
,    uinput.KEY_INSERT
,    uinput.KEY_DELETE
,    uinput.KEY_MACRO
,    uinput.KEY_MUTE
,    uinput.KEY_VOLUMEDOWN
,    uinput.KEY_VOLUMEUP
,    uinput.KEY_POWER
,    uinput.KEY_KPEQUAL
,    uinput.KEY_KPPLUSMINUS
,    uinput.KEY_PAUSE
,    uinput.KEY_SCALE
,    uinput.KEY_KPCOMMA
,    uinput.KEY_HANGEUL
,    uinput.KEY_HANGUEL
,    uinput.KEY_HANJA
,    uinput.KEY_YEN
,    uinput.KEY_LEFTMETA
,    uinput.KEY_RIGHTMETA
,    uinput.KEY_COMPOSE #127
,    uinput.KEY_F13 #183
,    uinput.KEY_F14
,    uinput.KEY_F15
,    uinput.KEY_F16
,    uinput.KEY_F17
,    uinput.KEY_F18
,    uinput.KEY_F19
,    uinput.KEY_F20
,    uinput.KEY_F21
,    uinput.KEY_F22
,    uinput.KEY_F23
,    uinput.KEY_F24
,    uinput.KEY_PLAYCD
,    uinput.KEY_PAUSECD
,    uinput.KEY_PROG3
,    uinput.KEY_PROG4
,    uinput.KEY_DASHBOARD
,    uinput.KEY_SUSPEND
,    uinput.KEY_CLOSE
,    uinput.KEY_PLAY
,    uinput.KEY_FASTFORWARD
,    uinput.KEY_BASSBOOST
,    uinput.KEY_PRINT
,    uinput.KEY_HP
,    uinput.KEY_CAMERA
,    uinput.KEY_SOUND
,    uinput.KEY_QUESTION
,    uinput.KEY_EMAIL
,    uinput.KEY_CHAT
,    uinput.KEY_SEARCH
,    uinput.KEY_CONNECT
,    uinput.KEY_FINANCE
,    uinput.KEY_SPORT
,    uinput.KEY_SHOP
,    uinput.KEY_ALTERASE
,    uinput.KEY_CANCEL
,    uinput.KEY_BRIGHTNESSDOWN
,    uinput.KEY_BRIGHTNESSUP #225
,    uinput.KEY_UNKNOWN #240
,    uinput.KEY_VIDEO_NEXT #241
,    uinput.KEY_VIDEO_PREV #242
#    uinput.KEY_
])


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
		wut=c.recv(1024)		#here the program waits for signal from client
		
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
	tervar=0
	while tervar==0:
		#the latest logfile location is removed in each iteration so that any change in llf can be recorded.
		cmd1='ls -t /opt/arbd/logs/ | head -1 '
		p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		chi=p1.communicate() # don't write \n
		llf=str(chi[0][:-1]) #llf=latest log file
		#print chi[0][:-1]
		cmd2='tail -0f /opt/arbd/logs/' + llf	#should grep be removed? will it interact with stdout? 
		pp2 = subprocess.Popen(cmd2, stdin=PIPE, stdout=PIPE, stderr=PIPE,shell=True)
		#pid = os.getpgid(pp2.pid)
		recvlist=c.recv(1024)
		
		#print recvlist
		if recvlist=="tervar=1":
			break
		print recvlist
		rlist = eval(recvlist)
		print 'rlist: '+str(rlist)		#rlist=[[ln1],[ln2],...], [ln1]= one keyboard event line with many keys(key_A,key_B,etc..)
		loll=len(rlist)
		for rkeys in rlist:
			
			combo=rkeys[-2]
			delta=rkeys[-1]
			combo_list=[]
			print 'combo:'+str(combo)
			if not ("no_key" in combo):		#if Keyboard_event line was empty			
				for i in combo:
					if i!= "Key_not_yet_defined":
						print 'i:    ' +str(i)
						exec(i) in globals(), locals()	# i = 'k=uinput.KEY_KN' #globals,locals because exec cannot be used inside a function which calls a subfunction(iter here)
 						combo_list.append(k)
					elif i== "Key_not_yet_defined":
						loll = loll-1
						print "Recieved a not defined key, neglected it!"
			if len(combo_list)==0:
				print "This shouldn't have happened, no_key is not being sent to alserver"
				raise Exception
			else:				
				Keyboard.emit_combo(combo_list)
			print "combo_list: "+str(combo_list)
			print "....."
			#print "Keyboard event executed."
			time.sleep(delta)
		obrf=[]
		sv = 0
		rov=''
		#obrf will store all brf lines until all keyboard events has been executed. After all keyboard events has been executed it will store the brf lines that come within 500 ms. 

		#also I have changed the code such that alserver will wait for at max 5 sec after execution of keyboard events , to get data from logfile.
		current1=datetime.datetime.now()		
		maxt=current1+datetime.timedelta(0,5,0,0)
					#datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]]
		
		for line in iter(lambda: pp2.stdout.readline(),''):
			if datetime.datetime.now().time() > maxt.time():	#max 5 s condition
						#print datetime.datetime.now().time() > nxt.time()
						print 'max crossed'
						break
			if " [display-svc] [debug] BRF data :" in line:
				obrf.append(line)
				print 'brf line in newlog file: '+line
				
			elif "Keyboard event" in line and sv!=loll:   #second condition because Keyboard event lines were coming even after sv == len(rlist)
				sv+=1
				print "keyboard line in new logfile:" +line
				print 'sv:'+str(sv)
			
			if rov == 'bits_more':
					#print "Recording a bit more"
					#print datetime.datetime.now().time(), nxt.time()
					
					if datetime.datetime.now().time() > nxt.time():
						#print datetime.datetime.now().time() > nxt.time()
						break

			elif sv == loll:
					print "All keyboard events recorded" 
					rov='bits_more'
					current=datetime.datetime.now()
					nxt=current+datetime.timedelta(0,0,0,500)
					#datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]]
			
		#subprocess.call(os.killpg(pid, signal.SIGTERM))
		
		pp2.terminate()	
		print obrf
		c.send(str(obrf))	#only 2 brf data lines are sent atmost
		



host= "192.168.7.2"
port=2651
password= ".Book40"
server(host,port,password)