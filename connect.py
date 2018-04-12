import paramiko,os,time
def conn(host,usr,pswd):
	ssh_client =paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#ssh_client.connect(hostname=host,username='sudhi',password='@3wRETyyUI')
	ssh_client.connect(hostname=host,username=usr,password=pswd)
	dir_path = os.path.dirname(os.path.realpath(__file__))
	ftp_client=ssh_client.open_sftp()
	ftp_client.put(dir_path+'/alserver.py','/home/ubuntu/alserver.py')
	time.sleep(3)
	stdin,stdout,stderr=ssh_client.exec_command('sudo -S <<< ".Book40" python /home/ubuntu/alserver.py', get_pty = True)
	time.sleep(999999)
	print "running"
	os._exit(0)
host= "192.168.7.2"
usr= "ubuntu"
password= ".Book40"
conn(host,usr,password)