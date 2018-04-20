import os,signal
import time
import multiprocessing
import tkMessageBox
import Tkinter as tk
from Tkinter import *
import ttk
from alclient import conn_send,execute,recording
from subprocess import Popen,call,PIPE
import subprocess
from executer6 import ex,ex2,di,timeparse,linker,timedifference
from random import randint
abc = None
#socket can be called by abc
#take care of wut in record ,execute and disconnect
#in disconnect make sure the process connect.py in your latop is closed and the created sockets are destroyed.
'''#for testing errors in a process
i=10
		for line in iter(lambda: p1.stderr.readline(),''):
				while i>0:
					print line 
					i=i-1
'''

class mainclass():
    def __init__(self,master):
        global button12,button13
        #self.text = tk.StringVar()
        #tk.Tk.__init__(self,master,*args,**kwargs)
        self.master = master
        master.frame = tk.Frame(master)
        #master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(),master.winfo_screenheight()))
        self.textx=""
        master.title("Automated RBD testing")
        master["bg"]= "white"
        label1 = Label(master,text="Automated RBD Testing App",bg="white",fg="black",font=  ("Arial","30","bold italic"))
        label1.grid(row=1,column=1,columnspan=7)
        #label1.place(relx=0.5,rely=0.4,anchor="center")
        self.button1 = ttk.Button(master, text="Connect", command=lambda:self.newone())
        self.button1.grid(row=3,column=1)
        self.button4 = ttk.Button(master, text="Disconnect", command=lambda:self.disconnect(),state= DISABLED)	#end nimbal's process at disconnect
        self.button4.grid(row=3,column=3)
        #self.text.set("connect")
        #self.button1.place(relx=0.5,rely=0.5,anchor="center")
        #button2 = ttk.Button(master, text="Excecute Testcases", command=lambda:self.execute())
        #button2.place(relx=0.6,rely=0.5,anchor="center")
        #master.rowconfigure(0,weight=1)
        #master.columnconfigure(0,weight=1)
        self.button2 = ttk.Button(master, text="Record", command=lambda:self.Record())
        self.button2.grid(row=3,column=5)
        #self.button2.place(relx=0.4,rely=0.5,anchor="center")
        #button2.lower(master.frame)
        self.button3 = ttk.Button(master, text="Excecute", command=lambda:self.execute_testcase())
        self.button3.grid(row=3,column=7)
        #self.button3.place(relx=0.6,rely=0.5,anchor="center")
        #button3.lower(master.frame)
        master.grid_rowconfigure(0,minsize=200,weight=1)
        master.grid_rowconfigure(2,minsize=20)
        master.grid_rowconfigure(7,minsize=250,weight=1)
        #master.grid_rowconfigure(2,weight=1)
        #master.grid_rowconfigure(3,weight=0)
        #master.grid_rowconfigure(0,minsize=,weight=)
        #master.grid_rowconfigure(0,minsize=,weight=)
        master.grid_columnconfigure(0,minsize=325,weight=1)
        master.grid_columnconfigure(2)
        master.grid_columnconfigure(8,minsize=250,weight=1)
        master.grid_columnconfigure(4)
        master.grid_columnconfigure(6)

        menu= Menu(master)
        master.config(menu=menu)
        Settingsmenu=Menu(menu)
        menu.add_cascade(label="Settings",menu=Settingsmenu)
        Settingsmenu.add_command(label="credetentials",command=lambda:self.credit())
    '''def execute(self):
        #print "s"
        root2=Toplevel(self.master,bg="white")
        app = execute_testcase(root2)'''
    def Record(self):
        #print "s"
        root2=Toplevel(self.master)
        app = Record_Testcases(root2)
    def credit(self):
        fileopen = open("settings.txt","r")
        self.root3=Toplevel(self.master)
        self.root3.geometry("300x200")
        label0 = Label(self.root3,text="Please enter credidentials").grid(row=0,column=0,columnspan=2)
        label1 = Label(self.root3,text="User ID").grid(row=1,column=0,sticky=E)
        label2 = Label(self.root3,text="Password").grid(row=2,column=0,sticky=E)
        label3 = Label(self.root3,text="IP Address").grid(row=3,column=0,sticky=E)
        #label4 = Label(self.root3,text="Port number").grid(row=4,column=0,sticky=E)
        self.Entry1=Entry(self.root3)
        self.Entry1.grid(row=1,column=1)
        #self.Entry1.focus_set()
        self.Entry2=Entry(self.root3)
        self.Entry2.grid(row=2,column=1)
        self.Entry3=Entry(self.root3)
        self.Entry3.grid(row=3,column=1)
        self.Entry4=Entry(self.root3)
        #self.Entry4.grid(row=4,column=1)
        self.root3.grid_rowconfigure(5, minsize=20)
        #button4 = Button(self.root3, text="OK", command=lambda:self.newone(self.root3),height=1,width=8).grid(row=6,column=0)
        button5 = Button(self.root3, text="Update", command=lambda:self.Update(),height=1,width=8).grid(row=6,column=0,columnspan=2)
        f=  fileopen.readlines()
        self.Entry1.insert(0,f[0][:-1])
        self.Entry2.insert(0,f[1][:-1])
        self.Entry3.insert(0,f[2][:-1])
        #self.Entry4.insert(0,f[4][:-1])
        fileopen.close()
    def port(self):
        self.root4=Toplevel(self.master)
        label0 = Label(self.root4,text="Please enter credidentials").grid(row=0,column=0,columnspan=2)
        label1 = Label(self.root4,text="Port number").grid(row=1,column=0,sticky=E)
        self.Entry5=Entry(self.root4)
        self.Entry5.grid(row=1,column=1)
        self.root4.grid_rowconfigure(2, minsize=20)
        button4 = Button(self.root4, text="OK", command=lambda:self.newone(),height=1,width=8).grid(row=3,column=0,columnspan=2)
    
    def newone(self):
        
        Portnumber = randint(1000,9999)
        execfile("alclient.py")
        #p='connected'
	with open('settings.txt','r') as f:
		k=f.readlines()		
		userid=k[0][:-1]
		password=k[1][:-1]
		Ipaddress=k[2][:-1]
        print userid,password,Ipaddress,Portnumber
	p=conn_send(userid,password,Ipaddress,Portnumber,self)
	print p
	if p[0]=='connected':
		#self.root4.destroy()
                self.button2["state"]='normal'
                self.button3["state"]='normal'
                self.button4["state"]='normal'
                self.button1["state"]='disabled'
                #label10.destroy()
                self.label11 = Label(self.master,text="Connected",bg="white",fg="black",font=  ("Arial","15","bold italic"))
                self.label11.grid(row=0,column=1,columnspan=5)
		self.socc=p[1]
		self.conn_proc=p[2]
		global abc
                abc=p[1]     
                print abc , type(abc)
		self.proc=p[2]
         
	else:
		tkMessageBox.showinfo('Error: ',p)
	
		
    def disconnect(self):
        #self.text.set("Disconnect")
	#handle socket closing also
	#take users password
	
        self.button1["text"]="Disconnect"
        self.button2["state"]= "snormal"
        self.button3["state"]="normal"
	f =open('disconn.txt','r')
	k=f.readline()
	pid=int(k.rstrip())
        os.kill(pid, signal.SIGTERM)
	self.button1["state"]='normal'
	
	tkMessageBox.showinfo('Info.','DISCONNECTED.',parent=self.master) 		#sudhi
	
	#sudhi

    def Update(self):
        userid= self.Entry1.get()
        password= self.Entry2.get()
        Ipaddress = self.Entry3.get()
        #Portnumber = self.Entry4.get()
	print userid,password,Ipaddress
        fil = open("settings.txt",'w')
        fil.write(userid+'\n')
        fil.write(password+'\n')
        fil.write(Ipaddress+'\n')
        #fil.write(userid+'\n')
        fil.close()
        #self.root3.destroy()
#------------------------------------------new----------------------------

    def execute_testcase(self):
        self.root4=Toplevel(self.master,bg="white")
        root4 = self.root4
        master = root4
        self.tree1 = ttk.Treeview(root4)
        tree = self.tree1
        tree.grid(row=0,column=0,sticky="nsew")
        root4.grid_columnconfigure(0,weight=1)
        root4.rowconfigure(1,weight=1)
        root4.rowconfigure(0,weight=1)
        abspath = os.path.abspath("tacread")
        self.root_node = tree.insert('', 'end', text="tacread", open=True)
        self.process_directory(self.root_node, abspath)
        #self.table(root4)
	botton12 = Button(master, text="RUN", command=lambda:self.run(),height=2,width=15,bg="Skyblue")
        botton12.grid(row=1,column=0)
        #button13 = self.botton19
        botton13 = Button(master, text="STOP", command="",height=2,width=15,bg= "Skyblue")
        botton13.grid(row=2,column=0)
        #button13 =self.button20
        style = ttk.Style()
        #style.configure(".", font=('Helvetica', 12))
        #style.configure("Treeview", foreground='red')
        style.configure("Treeview.Heading", foreground='Black',background="SkyBlue")
        self.tree2 = ttk.Treeview( master, columns=('KeyStrokes','Ideal Output','Received output','Pass/fail'))
        #self.tree2.heading('#0', text='Main heading')
        #self.tree2.heading('#1', text='heading')
        #self.tree2.heading('#2', text='sub heading')
        self.tree2.heading('#3', text='Pass/fail')
        self.tree2.heading('#0', text='KeyStrokes')
        self.tree2.heading('#1', text='Ideal Output')
        self.tree2.heading('#2', text='Received output')
        self.tree2.column('#2',width=220, stretch=False)
        self.tree2.column('#1',width=350, stretch=False)
        self.tree2.column('#0',width=220, stretch=False)
        self.tree2.column('#3',width=220, stretch=False)
        #self.tree2.column('#4',width=150, stretch=False)
        ##self.tree2.column('#5',width=150, stretch=False)
        #self.tree2.column('#6',width=150, stretch=False)
        self.tree2.grid(row=0,column=1, columnspan=7,rowspan=3, sticky='nsew')
        #self.tree.pack()
        self.treeview = self.tree2
        scrollbar1=Scrollbar(master,command=self.tree2.yview)
        scrollbar1.grid(row=0,column=8,rowspan=3,sticky=N+S)
        self.treeview.configure(yscrollcommand=scrollbar1.set)
        master.rowconfigure(0,weight=1)
        master.columnconfigure(0,weight=1)
        master.columnconfigure(1,weight=1)
        master.columnconfigure(2,weight=1)
        master.columnconfigure(3,weight=1)
        master.columnconfigure(4,weight=1)
        master.columnconfigure(5,weight=1)
        #scrollbar1.pack(side=RIGHT)
        #self.loadtable1()
        
        self.treeview.tag_configure("fail",background="coral1")
        self.treeview.tag_configure("pass",background="DarkOliveGreen1")
	
	
          #--------------------------------------------------
        root4.popup_menu = Menu(root4) 
        root4.popup_menu.add_command(label="Excecute",command=lambda:self.excecuter())
        tree.bind("<Button-3>",self.popup) 
    def popup(self, event): 
        iid = self.tree1.identify_row(event.y) 
        if iid:
           print "a"
           self.item_iid1 = self.tree1.selection()[0]
	   print 	self.item_iid1
           print  ".txt" in self.tree1.item(self.item_iid1,'text')
           if ".txt" in self.tree1.item(self.item_iid1,'text') :   
              self.tree1.selection_set(iid) 
              try: 
                  self.pop = self.root4.popup_menu.tk_popup(event.x_root, event.y_root, 0) 
              finally: 
                  self.root4.popup_menu.grab_release() 
        else: 
            pass
        

        #------------------------------------------------------
    def excecuter(self):
        text1 =""
        item_iid = self.item_iid1
        path = self.tree1.item(item_iid,'text')
        ab = self.tree1.parent(item_iid)
        print 'ab'
        while path !="" :
             text1 = path +"/"  +text1
             item_iid = self.tree1.parent(item_iid)
             path =  self.tree1.item(item_iid,'text')
        self.finalpath4 = os.getcwd()+"/"+text1[:-1]
	#_____________________________
	
	f= open(self.finalpath4,'r') 
	ideal_link=f.readlines()[0]
	#print ideal_link
	ilink=eval(ideal_link)
	sendlist=[]
	
	brfl=[]
	b2=0
	
	for line in ilink:
			if "BRF data" in line:
		
				brfl.append(line)
				
				if len(sendlist)==0:
					continue
				sendlist=[]
				
				ibrf = ''
				print str(b2)+'<b2',str(len(brfl))
				for i in range(b2,len(brfl)):

					k=str(brfl[i]).split(" [display-svc] [debug] BRF data :")[-1].strip('\n')
					ibrf+= k+" / "
					self.tree2.insert('',"end",text='',values=(ibrf,'',''))
                                        print ibrf
                                        #self.tree2.update_idletasks()	
											
			elif not('o' in line):
		
				b2=len(brfl)-1
				#no_key is not sent to alserver
				if line[-2]==['no_key']:
									
					self.treeview.insert('',"end",text='no_key',values=('','',''))
					print 'no_key_received'
				else:
				
				
					j_1=line[0].split("Keyboard event received: ")[-1][:-1]  #refer ex2 in executer6 for details
					self.treeview.insert('',"end",text=j_1,values=('','',''))
					sendlist.append(line)
        #button12["state"] = "normal"
					
    def run(self):
        self.variable = "initial"
        self.keylists = self.tree2.get_children()
        self.loop = 0
        self.equ1=multiprocessing.Queue()
	self.equ2=multiprocessing.Queue()
	self.equ3=multiprocessing.Queue()
	self.exe_error=multiprocessing.Queue()	
	
	self.et1=multiprocessing.Process(target=execute,args=(self,abc,self.finalpath4,self.equ1,self.equ2,self.equ3,self.exe_error))
        self.et1.start()
	self.equ_check()
    	
    def equ_check(self):
                #print self.equ3.qsize()
		if self.exe_error.qsize()!=0:
				#show error
				print 'Error aagaya'
				error1=self.exe_error.get()
				if "Broken pipe" in error1:
					tkMessageBox.showinfo('Error: ',"CONNECTION BROKEN,CONNECT AGAIN\n"+str(error1),parent=self.master)
				else:
					tkMessageBox.showinfo('Error: ',str(error1),parent=self.master)
				return		#out of equ_check	
		if self.equ3.qsize()==0:
			if self.equ1.qsize()!=0:
				p=self.equ1.get()
				print 'p:'+str(p)
                                if p[3] =="Failed":
                                       self.treeview.item(self.keylists[self.loop],text=p[0],values=(p[1],p[2],p[3]),tags ="fail")
                                elif p[3] =="Passed":
                                       self.treeview.item(self.keylists[self.loop],text=p[0],values=(p[1],p[2],p[3]),tags ="pass")
				else:
				       self.treeview.item(self.keylists[self.loop],text=p[0],values=(p[1],p[2],p[3]))
                                #self.treeview.yview_moveto(1)
                                
                                self.loop +=1
				self.treeview.update_idletasks()     #my line 
		if self.equ3.qsize()!=0:
			if self.equ1.qsize()!=0:
				p=self.equ1.get()
				print 'p:'+str(p)
                                #self.treeview.item(self.keylists[self.loop],text=p[0],values=(p[1],p[2],p[3]))
                                if p[3] =="Failed":
                                       self.treeview.item(self.keylists[self.loop],text=p[0],values=(p[1],p[2],p[3]),tags ="fail")
                                elif p[3] =="Passed":
                                       self.treeview.item(self.keylists[self.loop],text=p[0],values=(p[1],p[2],p[3]),tags ="pass")
				else:
				       self.treeview.item(self.keylists[self.loop],text=p[0],values=(p[1],p[2],p[3]))
                                #self.treeview.yview_moveto(1)
                                self.loop+=1
				self.treeview.update_idletasks()     #my line 

			equ3v=self.equ3.get()
			
			if equ3v =='wait':
				 
				
				
								
				if self.variable=="stop":
					return
				elif self.variable=="waiting":
					self.equ3.put('wait')
				elif self.variable == "initial":
					print 'unmatched '
				         
				        #self.treeview.see(END)                                  #my line 
					print 'mesgboxing'
					#mesgbox =   tkMessageBox.askyesno("Error","BRF data didn't match! Continue execution or stop?",parent=self.root4)
		                        self.root89 = Toplevel(self.root4)
		                        root89 = self.root89
		                        label0 = Label(root89,text="BRF data didn't match! Continue execution or stop?").grid(row=0,column=0,columnspan=3)
		                        botton12 = Button(root89, text="continue", command=lambda:self.con(),height=2,width=15).grid(row=2,column=0)
		                        botton12 = Button(root89, text="stop", command=lambda:self.sto(),height=2,width=15).grid(row=2,column=2)
		                        root89.rowconfigure(1,minsize=10)
		                        root89.columnconfigure(1,minsize=10)
                                         #----------------------------
                                        self.center(root89)
					#---------------------------------
					self.variable="waiting" 
					self.equ3.put('wait')
			if equ3v=='finished':
					
					#self.treeview.insert('',"end",text='',values=('','Finished execution',''))
					tkMessageBox.showinfo("info","Finished excecution",parent=self.root4)
                                        self.loop=0
					self.et1.join()
					print "Thread joined, finished execution.."	
					return 														
                self.master.after(50,self.equ_check)
    def center(self,win):
	    """
	    centers a tkinter window
	    :param win: the root or Toplevel window to center
	    """
	    win.update_idletasks()
	    width = win.winfo_width()
	    frm_width = win.winfo_rootx() - win.winfo_x()
	    win_width = width + 2 * frm_width
	    height = win.winfo_height()
	    titlebar_height = win.winfo_rooty() - win.winfo_y()
	    win_height = height + titlebar_height + frm_width
	    x = win.winfo_screenwidth() // 2 - win_width // 2
	    y = win.winfo_screenheight() // 2 - win_height // 2
	    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
	    win.deiconify()

    def con(self):
        
	self.equ2.put('c')
	self.variable="initial"
	if self.equ3.qsize()!=0:
		k=self.equ3.get() # to empty equ3
	self.root89.destroy()
    def sto(self):
        self.variable = "stop"
	self.root89.destroy()
	self.equ2.put('s')
				
	#self.treeview.insert('',"end",text='',values=('','Execution stopped by user' ,''))
        tkMessageBox.showinfo("info","Execution stopped by user",parent=self.root4)
	self.loop =0
	self.et1.join()
	
        
    def process_directory(self, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.tree1.insert(parent, 'end', text=p, open=False)
            if isdir:
                self.process_directory(oid, abspath)

    def table(self,master):
        self.botton19 = Button(master, text="RUN", command=lambda:self.run(),height=2,width=15,bg="Skyblue",state=DISABLED)
        self.botton19.grid(row=1,column=0)
        self.botton20 = Button(master, text="STOP", command="",height=2,width=15,bg= "Skyblue",state=DISABLED)
        self.botton20.grid(row=2,column=0)
        style = ttk.Style()
        #style.configure(".", font=('Helvetica', 12))
        #style.configure("Treeview", foreground='red')
        style.configure("Treeview.Heading", foreground='Black',background="SkyBlue")
        self.tree2 = ttk.Treeview( master, columns=('KeyStrokes','Ideal Output','Received output','Pass/fail'))
        #self.tree2.heading('#0', text='Main heading')
        #self.tree2.heading('#1', text='heading')
        #self.tree2.heading('#2', text='sub heading')
        self.tree2.heading('#3', text='Pass/fail')
        self.tree2.heading('#0', text='KeyStrokes')
        self.tree2.heading('#1', text='Ideal Output')
        self.tree2.heading('#2', text='Received output')
        self.tree2.column('#2',width=220, stretch=False)
        self.tree2.column('#1',width=220, stretch=False)
        self.tree2.column('#0',width=220, stretch=False)
        self.tree2.column('#3',width=220, stretch=False)
        #self.tree2.column('#4',width=150, stretch=False)
        ##self.tree2.column('#5',width=150, stretch=False)
        #self.tree2.column('#6',width=150, stretch=False)
        self.tree2.grid(row=0,column=1, columnspan=7,rowspan=3, sticky='nsew')
        #self.tree.pack()
        self.treeview = self.tree2
        scrollbar1=Scrollbar(master,command=self.tree2.yview)
        scrollbar1.grid(row=0,column=8,rowspan=3,sticky=N+S)
        self.treeview.configure(yscrollcommand=scrollbar1.set)
        master.rowconfigure(0,weight=1)
        #self.master.columnconfigure(0,weight=0)
        #scrollbar1.pack(side=RIGHT)
        #self.loadtable1()
        
        self.treeview.tag_configure("fail",background="red")
        self.treeview.tag_configure("pass",background="green")
        #------------------------------------
        #style = ttk.Style()
        #style.configure("Treeview.Heading", font=(None, 10))
	#self.treeview.insert('',"end",text=p[0],values=(p[1],p[2],"pass"))
        #self.treeview.insert('',"end",text=p[0],values=(p[1],p[2],"pass"))
        '''self.treeview.insert('',"end",text='q+w',values=('','',""))
        self.treeview.insert('',"end",text='e',values=('','',""))
        self.treeview.insert('',"end",text='r',values=('qwer','qwer',"Passed!"))
        self.treeview.insert('',"end",text='t',values=('qwert','qwert',"Passed!"))
        self.treeview.insert('',"end",text='y',values=('','',""))
        self.treeview.insert('',"end",text=' ',values=('','',""))
        self.treeview.insert('',"end",text='i',values=('qwerty i','qwerty i',"Passed!"))
        self.treeview.insert('',"end",text='s',values=('qwerty is','qwerty is',"Passed!"))
        self.treeview.insert('',"end",text=' ',values=('qwerty is ','qwerty is ',""))
	self.treeview.insert('',"end",text='l',values=('qwerty is l','qwerty is ',"Fail!"))
	mesgbox =   tkMessageBox.askyesno("Error","BRF data didn't match! Continue execution or stop?",parent=self.root4)
	'''


#----------------------------------------------
class Record_Testcases:
    def __init__(self,master):
        self.master = master
        style = ttk.Style()
	self.printer=[] #s#
        #self.Labelx = Label(master,text="")
        #self.Labelx.grid(row=0,column=0)
        #self.Entry=Entry(master,width=80,state = DISABLED)
        #self.Entry.grid(row=0,column=1,columnspan=3,sticky=NSEW)
        #self.master.grid_rowconfigure(1, minsize=20)
        #self.button7 = Button(master, text="Ok", command=lambda:self.abcd(),height=1,width=8,state = DISABLED)
        #self.button7.grid(row=2,column=1)
        #self.button8 = Button(master, text="Start Recording", command=lambda:self.recording1(),height=1,state=DISABLED)
        #self.button8.grid(row=2,column=2)
        self.button9 = Button(master, text="End Recording", command=lambda:self.stop(),height=1,state=DISABLED)
        self.button9.grid(row=5,column=0)
        #---------------------------------------
   	self.tree2 = ttk.Treeview( master, columns=('Sr. number','Keyword name','keyword'))
   	style.configure("Treeview.Heading", foreground='Black',background="SkyBlue")
   	self.tree2.heading('#0', text='S No.')
        self.tree2.heading('#1', text='BRF DATA')
        self.tree2.heading('#2', text='Keyboard Event')
        self.tree2.column('#0',width=50, stretch=False)
        self.tree2.column('#1',width=600, stretch=False)
        self.tree2.column('#2',width=280, stretch=False)
        self.tree2.grid(row=0,column=1, rowspan=8, sticky='nsew')
        #style.configure("Treeview", foreground='red')
   	#recordclient(self.socc,self.Entry.get())
        self.tree = ttk.Treeview(master)
        tree =  self.tree
        #tree.pack(side=LEFT,fill=Y)
        tree.grid(row=0,column=0,sticky="nsew",rowspan=4)
        #self.master.grid_rowconfigure(1, weight=1)
        #tree.grid(row=0,column=0,rowspan=2,columnspan=8,sticky=NSEW)
        #.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(),self.winfo_screenheight()))
        abspath = os.path.abspath("tacread")
        self.root_node = self.tree.insert('', 'end', text="tacread", open=True)
        self.process_directory(self.root_node, abspath)
        #tree.bind("<Double-1>", self.OnDoubleClick)
        #tree.bind("<Double-1>",self.running)
        #self.master.grid_columnconfigure(0,weight=1)
        master.grid_columnconfigure(1,weight=1)
        #master.columnconfigure(0,weight=0)
        master.rowconfigure(2,weight=1)
        master.rowconfigure(0,weight=1)
        master.rowconfigure(1,weight=0)
        master.rowconfigure(3,weight=3)
        #master.columnconfigure(3,minsize=20,weight=0)
        master.rowconfigure(4,minsize=20,weight=0)
        master.rowconfigure(5,minsize=20,weight=1)
        master.rowconfigure(6,minsize=20,weight=0)
        #tacread = tree.insert("",0,"tacread",text = "tacread")
        scrollbar1 = Scrollbar(master,orient = "vertical")
        #self.listbox1 = Listbox(master,yscrollcommand = scrollbar1.set)
        #self.listbox1= listbox1
        #self.listbox1.grid(row=3,column=1,sticky=NSEW,columnspan=8)
        scrollbar1 = Scrollbar(master,orient = "vertical",command=self.tree2.yview)
        scrollbar1.config(command = self.tree2.yview)
        scrollbar1.grid(row=0,column=2,sticky=NSEW,rowspan=8)
	master.popup_menu = Menu(master)
        master.popup_menu.add_command(label="Add Menu",command=lambda:self.addmenu(master))
        master.popup_menu.add_command(label="Add Testcase",command=lambda:self.addtestcase(master))
        master.popup_menu.add_command(label="Delete",command=lambda:self.delete(master))

        self.tree.bind("<Button-3>",self.popup)
    def popup(self, event):

        iid = self.tree.identify_row(event.y)

        if iid:

         self.tree.selection_set(iid)

         try:

            self.pop = self.master.popup_menu.tk_popup(event.x_root, event.y_root, 0)

         finally:

            self.master.popup_menu.grab_release()

        else:

            pass

        self.item_iid = self.tree.selection()[0]

    def addmenu(self,master):
        #self.Labelx["text"] = "Enter the name of submenu" 
        #self.pop.destroy()
        self.root4=Toplevel(self.master)
        label0 = Label(self.root4,text="Please enter the name of menu").grid(row=0,column=0,columnspan=2)
        label1 = Label(self.root4,text="Name").grid(row=1,column=0,sticky=E)
	self.center(self.root4)
        self.Entry5=Entry(self.root4)
        self.Entry5.grid(row=1,column=1)
        self.root4.grid_rowconfigure(2, minsize=20)
        button4 = Button(self.root4, text="OK", command=lambda:self.abcd(),height=1,width=8).grid(row=3,column=0,columnspan=2)
        #---------------------------------------
        text1 = ""
        item_iid = self.item_iid
        path = self.tree.item(item_iid,'text')
        ab = self.tree.parent(self.item_iid)
        #print ab
        while path !="" :
             text1 = path +"/"  +text1
             item_iid = self.tree.parent(item_iid)
             path =  self.tree.item(item_iid,'text')
        #self.Entry["state"] = "normal"
        #self.button7["state"] = "normal"
        self.finalpath = os.getcwd()+"/" +text1
       #print os.path.abspath(os.path.dirname(__path__))
        '''parent_iid = self.tree.parent(self.item_iid)[0]
        text3= (self.tree.item(self.item_iid)['text'])
        if parent_iid:
             text2 = (self.tree.item(parent_iid)['text'])
             parent_parent_iid = self.tree.parent(parent_iid)[0]     
             if parent_parent_iid:
                   text1 = (self.tree.item(parent_parent_iid)['text'])
                   newpath =
             else:
                   newpath ="" 
             
        else:
             self.Entry.insert(0,text1)
        if not os.path.exists(newpath):
                os.makedirs(newpath)
        else:
                tkMessageBox.showinfo('Error: ',"This folder already exists")'''
    def abcd(self):
        #print self.finalpath
      if self.Entry5.get() =="":
        tkMessageBox.showinfo('Error: ',"please enter a valid name",parent=self.master)
      else:     
        path = self.finalpath+self.Entry5.get()
        if not os.path.exists(path):
             print path
             os.makedirs(path)
             self.root4.destroy()
             #self.Entry.delete(0,END)
             #self.Entry["state"] = DISABLED
             #self.button7["state"] = DISABLED
        else:
             tkMessageBox.showinfo('Error: ',"this folder already exists",parent=self.master)
        self.tree.delete(*self.tree.get_children())
        abspath = os.path.abspath("tacread")
        self.root_node = self.tree.insert('', 'end', text="tacread", open=True)
        self.process_directory(self.root_node, abspath)
    
    def center(self,win):
	    """
	    centers a tkinter window
	    :param win: the root or Toplevel window to center
	    """
	    win.update_idletasks()
	    width = win.winfo_width()
	    frm_width = win.winfo_rootx() - win.winfo_x()
	    win_width = width + 2 * frm_width
	    height = win.winfo_height()
	    titlebar_height = win.winfo_rooty() - win.winfo_y()
	    win_height = height + titlebar_height + frm_width
	    x = win.winfo_screenwidth() // 2 - win_width // 2
	    y = win.winfo_screenheight() // 2 - win_height // 2
	    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
	    win.deiconify()
	
    def recording1(self):
     if self.Entry6.get() =="":
        tkMessageBox.showinfo('Error: ',"please enter a valid name",parent=self.master)
     else:
	#self.button8["state"]=DISABLED
        path = self.finalpath1+self.Entry6.get()+".txt"
        print path
        if not os.path.exists(path):
             print path
             #os.makedirs(path)
             f = open(path,'w')
             f.close()
             self.root5.destroy()
             #self.Entry.delete(0,END)
             #self.Entry["state"] = DISABLED
             self.button9["state"] ="normal"
        else:
             tkMessageBox.showinfo('Error: ',"this folder already exists",parent=self.master)
        self.tree.delete(*self.tree.get_children())
        abspath = os.path.abspath("tacread")
        self.root_node = self.tree.insert('', 'end', text="tacread", open=True)
        self.process_directory(self.root_node, abspath)
        #self.listbox1.insert(0,path)
	print 'lll'
	self.qu=multiprocessing.Queue()
	self.stop_but=multiprocessing.Queue()
	self.rec_error=multiprocessing.Queue()
	self.qu.put(('',"Recording Started.",''))	#to make sure queue size is not zero initially, make sure line is here only
	self.rt1=multiprocessing.Process(target=recording,args=(self,path,abc,self.qu,self.stop_but,self.rec_error))
					#(target=execute,args=(self,abc,self.finalpath4,self.equ1,self.equ2,self.equ3))
        self.rt1.start()
	
	


	self.qu_check()


	print "Thread started...."
	
	
    def qu_check(self):
		#write code to check if credentials are wrong (code might still work without throwing any errors, but won't give any output)
                p=0
		#check qsize and empty documentation. qsize gices approx size.
		#most probably there is no problem in qsize, it works fine
		print 'chal'
		while self.qu.qsize()!=0 :
			
			po=self.qu.get()
		        #self.tree2.insert('',"end",text='',values=('',''))
                        #print "wer"+p[0]+p[1]+p[2] 
                        self.tree2.insert('',"end",text=po[0],values=(po[1],po[2]))
                        self.tree2.update_idletasks()
                        self.tree2.yview_moveto(1)
			#self.listbox1.insert(END,self.qu.get())	
			#self.listbox1.update_idletasks() 	#or else listbox is updated only after whole fxn is called
                        #self.listbox1.see(END)
		
		print str(self.stop_but.qsize()) +'but_size'
		if not self.rec_error.empty():
				#show error
				print 'Error aagaya'
				error1=self.rec_error.get()
				print error1
				if "'NoneType' object has no attribute 'send'" in error1:
					tkMessageBox.showinfo('Error.Probably connection not established. Details: ',str(error1),parent=self.master)
				elif "Broken pipe" in error1:
					tkMessageBox.showinfo('Error: ',"CONNECTION BROKEN,CONNECT AGAIN\n"+str(error1),parent=self.master)
				else:
					tkMessageBox.showinfo('Error: ',str(error1),parent=self.master)
				return		#out of qu_check	
		if not self.stop_but.empty():
				print 'stopped'
                                tkMessageBox.showinfo('end',"FINISHED RECORDING, TESTCASE GENERATED.",parent=self.master)
				#self.listbox1.insert(END,"FINISHED RECORDING, TESTCASE GENERATED.")	
				#self.listbox1.update_idletasks() 	#or else listbox is updated only after whole fxn is called
                        	#self.listbox1.see(END)
                                p=1
				return		#out of qu_check
                self.master.after(50,self.qu_check)
                
    def addtestcase(self,master):
        
        self.root5=Toplevel(self.master)
        label0 = Label(self.root5,text="Please enter the name of Testcase").grid(row=0,column=0,columnspan=2)
        label1 = Label(self.root5,text="Name").grid(row=1,column=0,sticky=E)
        self.Entry6=Entry(self.root5)
        self.Entry6.grid(row=1,column=1)
        self.root5.grid_rowconfigure(2, minsize=20)
        button4 = Button(self.root5, text="Start Recording", command=lambda:self.recording1(),height=1).grid(row=3,column=0,columnspan=2)
        #self.Labelx["text"] = "Enter the name of Testcase"
        #-----------------------------------------------------------------------
        #master.popup_menu.destroy()
        text1 = ""
        item_iid = self.item_iid
        path = self.tree.item(item_iid,'text')
        ab = self.tree.parent(self.item_iid)
        #print ab
        while path !="" :
             text1 = path +"/"  +text1
             item_iid = self.tree.parent(item_iid)
             path =  self.tree.item(item_iid,'text')
        #self.Entry["state"] = "normal"
        self.finalpath1 = os.getcwd()+"/"+text1
        #self.Entry["state"] = "normal"
        #self.button8["state"] = "normal"
        #self.button9["state"] = "normal"

    def process_directory(self, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.tree.insert(parent, 'end', text=p, open=False)
            if isdir:
                self.process_directory(oid, abspath)
    	
    def stop(self):
	
        self.stop_but.put("stopped...")
	time.sleep(4)
        print 'Recording stopped, processing and generating testcase....'
	
	self.rt1.join()
        print "Joined"
    '''def OnDoubleClick(self, event):
        item_iid = self.tree.selection()[0]
        parent_iid = self.tree.parent(item_iid)[0]
        parent_parent_iid = self.tree.parent(parent_iid)[0]
        text1 = (self.tree.item(parent_parent_iid)['text'])
        text2 = (self.tree.item(parent_iid)['text'])
        text3= (self.tree.item(item_iid)['text'])
        if parent_iid:
             if parent_parent_iid:
                   self.Entry.insert(0,text1+"_"+text2+"_"+text3)
             else:
                   self.Entry.insert(0,text1+"_"+text2)
             
        else:
             self.Entry.insert(0,text1)'''
   


'''
class Record_Testcases():
    def __init__(self,master):
        self.master = master
        Labelx = Label(self.master,text="Select the testcases").grid(row=0,column=0,columnspan=2)
        self.Entry=Entry(master)
        self.Entry.grid(row=0,column=1)
        master.grid_rowconfigure(1, minsize=20)
        button4 = Button(master, text="Record", command=lambda:self.recording(),height=1,width=8).grid(row=2,column=1)
        button5 = Button(master, text="Stop", command=lambda:self.stop(),height=1,width=8).grid(row=2,column=2)
   	
   	#recordclient(self.socc,self.Entry.get())
        tree = ttk.Treeview(master)
        #tree.pack(side=LEFT,fill=Y)
        tree.grid(row=2,column=0,sticky="nsew",rowspan=2)
        #tree.grid(row=0,column=0,rowspan=2,columnspan=8,sticky=NSEW)
        #.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(),self.winfo_screenheight()))
        helps = tree.insert("",0,"help",text = "Help")
        #tree.bind("<Double-1>", self.OnDoubleClick)
        #tree.bind("<Double-1>",self.running)
        master.grid_columnconfigure(0,weight=1)
        #master.grid_columnconfigure(1,weight=1)
        #master.columnconfigure(0,weight=1)
        master.rowconfigure(1,weight=1)
        master.rowconfigure(0,weight=1)
        tree.insert(helps,"end",text="testcase1")
        tree.insert(helps,"end",text="testcase2")
        tree.insert(helps,"end",text="testcase3")
        tree.insert(helps,"end",text="testcase4")
        tree.insert(helps,"end",text="testcase5") 
        system = tree.insert("",0,"Systeminformation",text = "System Information")
        tree.insert(system,"end",text="testcase1")
        tree.insert(system,"end",text="testcase2")
        tree.insert(system,"end",text="testcase3")
        tree.insert(system,"end",text="testcase4")
        tree.insert(system,"end",text="testcase5")
        setting = tree.insert("",0,"settings",text = "Settings")

        tree.insert(setting,"end",text="testcase1")
        tree.insert(setting,"end",text="testcase2")
        tree.insert(setting,"end",text="testcase3")
        tree.insert(setting,"end",text="testcase4")
        tree.insert(setting,"end",text="testcase5")
        filebrowser = tree.insert("",0,"filebrowser",text = "File Browser")
        tree.insert(filebrowser,"end",text="Open File browser")
        tree.insert(filebrowser,"end",text="First Letter Navigation")
        tree.insert(filebrowser,"end",text="File/folder creation")
        tree.insert(filebrowser,"end",text="cut/copy operations")
        tree.insert(filebrowser,"end",text="Paste operation")
        tree.insert(filebrowser,"end",text="Delete operation")
        tree.insert(filebrowser,"end",text="rename operation")
        tree.insert(filebrowser,"end",text="Mark multiple files/folders")
        browser = tree.insert("",0,"browser",text = "Web Browser")
        tree.insert(browser,"end",text="Starting Web Browser")
        tree.insert(browser,"end",text="Reading a web browser")
        tree.insert(browser,"end",text="Opening a link")
        tree.insert(browser,"end",text="Back and forward")
        tree.insert(browser,"end",text="changing URL/Opening new URL")
        email = tree.insert("",0,"email",text = "Email")
        tree.insert(email,"end",text="testcase1")
        tree.insert(email,"end",text="testcase2")
        tree.insert(email,"end",text="testcase3")
        tree.insert(email,"end",text="testcase4")
        tree.insert(email,"end",text="testcase5")
        word = tree.insert("",0,"Word processor",text = "Word Processor")
        tree.insert(word,"end",text="testcase1")
        tree.insert(word,"end",text="testcase2")
        tree.insert(word,"end",text="testcase3")
        tree.insert(word,"end",text="testcase4")
        tree.insert(word,"end",text="testcase5")
        notepad = tree.insert("",0,"notepad",text = "Notepad")
        tree.insert(notepad,"end",text="testcase1")
        tree.insert(notepad,"end",text="testcase2")
        tree.insert(notepad,"end",text="testcase3")
        tree.insert(notepad,"end",text="testcase4")
        tree.insert(notepad,"end",text="testcase5")
        Applicationmenu = tree.insert("",0,"Applicationmenu",text = "Applicationmenu")
        tree.insert(Applicationmenu,"end",text="Opening Menu")
        nttm = tree.insert(Applicationmenu,"end",text="Navigate through the menu")
        tree.insert(nttm,"end",text="First letter navigation")
        tree.insert(nttm,"end",text="Exit the menu")
        menu = tree.insert(Applicationmenu,"end",text="Menu items")
        tree.insert(menu,"end",text="notepad")
        tree.insert(menu,"end",text="Word processor")
        tree.insert(menu,"end",text="Email")
        tree.insert(menu,"end",text="Web Browser")
        tree.insert(menu,"end",text="File Browser")
        tree.insert(menu,"end",text="Settings")
        tree.insert(menu,"end",text="Help")
        tree.insert(menu,"end",text="System Information")
        listbox1 = Listbox(master)
        self.listbox1= listbox1
        listbox1.grid(row=3,column=1,sticky=NSEW,columnspan=2)
        #scrollbar1 = Scrollbar(root,orient = "vertical")
        #scrollbar1.config(command = listbox1.yview)
        #scrollbar1.grid(row=1,column=12,rowspan=7,sticky=NSEW)
    def recording(self):
	#gives a file of the name testcase_name which has two lists.The first list is parsed one and the second list is unparsed.
	testcase_name=self.Entry.get()
	print "Recording started,you can start giving keystrokes..."
	s=abc	
	s.send('continue')
	qwer=0
	testcase=[]	#testcase contains the unparsed lines as srecieved	
	blink=[]		#blink contains parsed lines of the logfile. blink=BRF_BASED_link
'''
'''	
	blink= [ 'o',b0,[l01],[l02],...,b1,[l11],[l12],...,b2,....,bn,[ln1],[ln2],...,bn_1,........bfinal/[lfinal] ]
	
		where bn = string containg nth BRF data line,bn_1 = string containg (n+1)th BRF data line
		and [lnm] = list of the form : [lnm]=[line,time,['k=uinput.KEY_K1','k=uinput.KEY_K2',...],timediff] .
		line is a string containing Keyboard Event, time is a string, third element is a list of the given format,
		timediff is an int and is the time difference (lnm_1 - lnm)
		b0 might come or might not come based on whether during recording first line from logfile is brfdata or keyboard event	

'''
'''
	blink.append('o')
	f=open('stop_button.txt','w')
	f.write('blah blah')
	f.close()
	while qwer==0:
		
		
		stop_button=open("stop_button.txt","r")
		stop_button.seek(0,0)
		u_input=stop_button.readline()                            
		stop_button.close()
		
		#stop_button.py waits for 2 seconds after recieving the stop command to actually send stop to alclient.py
		#this is necessary as the last few BRF data lines in the log_file after the last keyboard event line is also required.
		line=s.recv(1024)
		testcase.append(str(line))
		
		if ('BRF data' in line):
			blink.append(line)	
                        
			
		elif ('Keyboard event received' in line):
			ji=ex(line)
			blink.append([line,timeparse(line),ji])
			print_ln=str(ji) + ' : ' + str(ex2(line))
			self.listbox1.insert(print_ln)
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
			ik-=1
	
	
	print 'The test case recorded is:'
	for i in range(len(testcase)-1):
				
			print testcase[i]
			
			print blink[i+1]
			print ' '
	  		
    	with open(testcase_name+'.txt', "w") as f1:
        		
			f1.write(str(blink)+'\n')
			f1.write(str(testcase)+'\n')
			   #to call the function sassy
	
	#no need to close files, with automatically closes
	
	#link is the arsed one and testcase is the unparsed.
    def stop(self):
        f=open('stop_button.txt','w')

	f.write('stop')
	f.close()
'''
        
'''class execute_testcase():
    def __init__(self,master):
        #print "y"
        self.master=master
        tree = ttk.Treeview(master)
        #tree.pack(side=LEFT,fill=Y)
        tree.grid(row=0,column=0,sticky="nsew")
        #tree.grid(row=0,column=0,rowspan=2,columnspan=8,sticky=NSEW)
        #.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(),self.winfo_screenheight()))
        helps = tree.insert("",0,"help",text = "Help")
        #tree.bind("<Double-1>", self.OnDoubleClick)
        #tree.bind("<Double-1>",self.running)
        master.grid_columnconfigure(0,weight=1)
        #master.grid_columnconfigure(1,weight=1)
        #master.columnconfigure(0,weight=1)
        master.rowconfigure(1,weight=1)
        master.rowconfigure(0,weight=1)
        tree.insert(helps,"end",text="testcase1")
        tree.insert(helps,"end",text="testcase2")
        tree.insert(helps,"end",text="testcase3")
        tree.insert(helps,"end",text="testcase4")
        tree.insert(helps,"end",text="testcase5") 
        system = tree.insert("",0,"Systeminformation",text = "System Information")
        tree.insert(system,"end",text="testcase1")
        tree.insert(system,"end",text="testcase2")
        tree.insert(system,"end",text="testcase3")
        tree.insert(system,"end",text="testcase4")
        tree.insert(system,"end",text="testcase5")
        setting = tree.insert("",0,"settings",text = "Settings")
        tree.insert(setting,"end",text="testcase1")
        tree.insert(setting,"end",text="testcase2")
        tree.insert(setting,"end",text="testcase3")
        tree.insert(setting,"end",text="testcase4")
        tree.insert(setting,"end",text="testcase5")
        filebrowser = tree.insert("",0,"filebrowser",text = "File Browser")
        tree.insert(filebrowser,"end",text="Open File browser")
        tree.insert(filebrowser,"end",text="First Letter Navigation")
        tree.insert(filebrowser,"end",text="File/folder creation")
        tree.insert(filebrowser,"end",text="cut/copy operations")
        tree.insert(filebrowser,"end",text="Paste operation")
        tree.insert(filebrowser,"end",text="Delete operation")
        tree.insert(filebrowser,"end",text="rename operation")
        tree.insert(filebrowser,"end",text="Mark multiple files/folders")
        browser = tree.insert("",0,"browser",text = "Web Browser")
        tree.insert(browser,"end",text="Starting Web Browser")
        tree.insert(browser,"end",text="Reading a web browser")
        tree.insert(browser,"end",text="Opening a link")
        tree.insert(browser,"end",text="Back and forward")
        tree.insert(browser,"end",text="changing URL/Opening new URL")
        email = tree.insert("",0,"email",text = "Email")
        tree.insert(email,"end",text="testcase1")
        tree.insert(email,"end",text="testcase2")
        tree.insert(email,"end",text="testcase3")
        tree.insert(email,"end",text="testcase4")
        tree.insert(email,"end",text="testcase5")
        word = tree.insert("",0,"Word processor",text = "Word Processor")
        tree.insert(word,"end",text="testcase1")
        tree.insert(word,"end",text="testcase2")
        tree.insert(word,"end",text="testcase3")
        tree.insert(word,"end",text="testcase4")
        tree.insert(word,"end",text="testcase5")
        notepad = tree.insert("",0,"notepad",text = "Notepad")
        tree.insert(notepad,"end",text="testcase1")
        tree.insert(notepad,"end",text="testcase2")
        tree.insert(notepad,"end",text="testcase3")
        tree.insert(notepad,"end",text="testcase4")
        tree.insert(notepad,"end",text="testcase5")
        Applicationmenu = tree.insert("",0,"Applicationmenu",text = "Applicationmenu")
        tree.insert(Applicationmenu,"end",text="Opening Menu")
        nttm = tree.insert(Applicationmenu,"end",text="Navigate through the menu")
        tree.insert(nttm,"end",text="First letter navigation")
        tree.insert(nttm,"end",text="Exit the menu")
        menu = tree.insert(Applicationmenu,"end",text="Menu items")
        tree.insert(menu,"end",text="notepad")
        tree.insert(menu,"end",text="Word processor")
        tree.insert(menu,"end",text="Email")
        tree.insert(menu,"end",text="Web Browser")
        tree.insert(menu,"end",text="File Browser")
        tree.insert(menu,"end",text="Settings")
        tree.insert(menu,"end",text="Help")
        tree.insert(menu,"end",text="System Information")
        self.table()
    def table(self):
        style = ttk.Style()
        #style.configure(".", font=('Helvetica', 8), foreground="white")
        style.configure("Treeview", foreground='red')
        style.configure("Treeview.Heading", foreground='Black',background="SkyBlue")
        self.tree = ttk.Treeview( self.master, columns=('Main heading', 'heading','sub heading','Testcase','KeyStrokes','Output','Passed'))
        self.tree.heading('#0', text='Main heading')
        self.tree.heading('#1', text='heading')
        self.tree.heading('#2', text='sub heading')
        self.tree.heading('#3', text='Testcase')
        self.tree.heading('#4', text='KeyStrokes')
        self.tree.heading('#5', text='Output')
        self.tree.heading('#6', text='Passed')
        self.tree.column('#2',width=150, stretch=False)
        self.tree.column('#1',width=160, stretch=False)
        self.tree.column('#0',width=150, stretch=False)
        self.tree.column('#3',width=150, stretch=False)
        self.tree.column('#4',width=150, stretch=False)
        self.tree.column('#5',width=150, stretch=False)
        self.tree.column('#6',width=150, stretch=False)
        self.tree.grid(row=0,column=1, columnspan=7,rowspan=3, sticky='nsew')
        #self.tree.pack()
        self.treeview = self.tree
        scrollbar1=Scrollbar(self.master,command=self.tree.yview)
        scrollbar1.grid(row=0,column=8,rowspan=3,sticky=N+S)
        self.treeview.configure(yscrollcommand=scrollbar1.set)
        self.master.rowconfigure(0,weight=1)
        #self.master.columnconfigure(0,weight=0)
        #scrollbar1.pack(side=RIGHT)
        self.loadtable1()
        botton1 = Button(self.master, text="RUN", command="",height=2,width=15,bg="Skyblue")
        botton1.grid(row=1,column=0)
        botton2 = Button(self.master, text="STOP", command="",height=2,width=15,bg= "Skyblue")
        botton2.grid(row=2,column=0)
    def loadtable1(self):
        f = open("inputkey.txt","r")
        for line in f:
              self.treeview.insert('',"end",text ="Application Menu",values=("Opening Menu","","",line))
        g = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Application Menu",values=("Navigate through the menu","First letter navigation","",line))
        h = open("inputkey.txt","r")
        for line in h:
              self.treeview.insert('',"end",text ="Application Menu",values=("Navigate through the menu","Exit the Menu","",line))
        i = open("inputkey.txt","r")
        for line in i:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","notepad","",line))
        j = open("inputkey.txt","r")
        for line in j:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","Word processor","",line))
        k = open("inputkey.txt","r")
        for line in k:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","Email","",line))
        l = open("inputkey.txt","r")
        for line in l:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","File Browser","",line))
        m = open("inputkey.txt","r")
        for line in m:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","Settings","",line))
        n = open("inputkey.txt","r")
        for line in n:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","Help","",line))
        o = open("inputkey.txt","r")
        for line in o:
              self.treeview.insert('',"end",text ="Application Menu",values=("Menu items","System Information","",line))
        g = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase1",line))
        h = open("inputkey.txt","r")
        for line in h:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase2",line))
        i = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase3",line))
        j = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase4",line))
        k = open("inputkey.txt","r")
        for line in g:
              self.treeview.insert('',"end",text ="Notepad",values=("","","Testcase5",line))'''
def main():
    root =Tk()
    app = mainclass(root)
    root.mainloop()

if __name__=='__main__':
    main()







'''helps = tree.insert("",0,"help",text = "Help")
        tree.insert(helps,"end",text="testcase1")
        tree.insert(helps,"end",text="testcase2")
        tree.insert(helps,"end",text="testcase3")
        tree.insert(helps,"end",text="testcase4")
        tree.insert(helps,"end",text="testcase5") 
        system = tree.insert("",0,"Systeminformation",text = "System Information")
        tree.insert(system,"end",text="testcase1")
        tree.insert(system,"end",text="testcase2")
        tree.insert(system,"end",text="testcase3")
        tree.insert(system,"end",text="testcase4")
        tree.insert(system,"end",text="testcase5")
        setting = tree.insert("",0,"settings",text = "Settings")

        tree.insert(setting,"end",text="testcase1")
        tree.insert(setting,"end",text="testcase2")
        tree.insert(setting,"end",text="testcase3")
        tree.insert(setting,"end",text="testcase4")
        tree.insert(setting,"end",text="testcase5")
        filebrowser = tree.insert("",0,"filebrowser",text = "File Browser")
        tree.insert(filebrowser,"end",text="Open File browser")
        tree.insert(filebrowser,"end",text="First Letter Navigation")
        tree.insert(filebrowser,"end",text="File/folder creation")
        tree.insert(filebrowser,"end",text="cut/copy operations")
        tree.insert(filebrowser,"end",text="Paste operation")
        tree.insert(filebrowser,"end",text="Delete operation")
        tree.insert(filebrowser,"end",text="rename operation")
        tree.insert(filebrowser,"end",text="Mark multiple files/folders")
        browser = tree.insert("",0,"browser",text = "Web Browser")
        tree.insert(browser,"end",text="Starting Web Browser")
        tree.insert(browser,"end",text="Reading a web browser")
        tree.insert(browser,"end",text="Opening a link")
        tree.insert(browser,"end",text="Back and forward")
        tree.insert(browser,"end",text="changing URL/Opening new URL")
        email = tree.insert("",0,"email",text = "Email")
        tree.insert(email,"end",text="testcase1")
        tree.insert(email,"end",text="testcase2")
        tree.insert(email,"end",text="testcase3")
        tree.insert(email,"end",text="testcase4")
        tree.insert(email,"end",text="testcase5")
        word = tree.insert("",0,"Word processor",text = "Word Processor")
        tree.insert(word,"end",text="testcase1")
        tree.insert(word,"end",text="testcase2")
        tree.insert(word,"end",text="testcase3")
        tree.insert(word,"end",text="testcase4")
        tree.insert(word,"end",text="testcase5")
        notepad = tree.insert("",0,"notepad",text = "Notepad")
        tree.insert(notepad,"end",text="testcase1")
        tree.insert(notepad,"end",text="testcase2")
        tree.insert(notepad,"end",text="testcase3")
        tree.insert(notepad,"end",text="testcase4")
        tree.insert(notepad,"end",text="testcase5")
        Applicationmenu = tree.insert("",0,"Applicationmenu",text = "Applicationmenu")
        tree.insert(Applicationmenu,"end",text="Opening Menu")
        nttm = tree.insert(Applicationmenu,"end",text="Navigate through the menu")
        tree.insert(nttm,"end",text="First letter navigation")
        tree.insert(nttm,"end",text="Exit the menu")
        menu = tree.insert(Applicationmenu,"end",text="Menu items")
        tree.insert(menu,"end",text="notepad")
        tree.insert(menu,"end",text="Word processor")
        tree.insert(menu,"end",text="Email")
        tree.insert(menu,"end",text="Web Browser")
        tree.insert(menu,"end",text="File Browser")
        tree.insert(menu,"end",text="Settings")
        tree.insert(menu,"end",text="Help")
        tree.insert(menu,"end",text="System Information")'''
