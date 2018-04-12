import os
import paramiko, getpass, re, time
import sys
import time
import subprocess
import socket
from subprocess import Popen,call,PIPE
host='192.168.7.2'
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_client.connect(hostname=host,username='sudhi',password='@3wRETyyUI')
ssh_client.connect(hostname=host,username='ubuntu',password='.Book40')
dir_path = os.path.dirname(os.path.realpath(__file__))
ftp_client=ssh_client.open_sftp()
ftp_client.put(dir_path+'/alserver.py','/home/ubuntu/alserver.py')
time.sleep(3)
stdin,stdout,stderr=ssh_client.exec_command('sudo -S <<< ".Book40" python /home/ubuntu/alserver.py', get_pty = True)
time.sleep(500000)
print "running"
os._exit(0)
