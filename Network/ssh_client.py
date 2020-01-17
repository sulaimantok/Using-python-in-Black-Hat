import threading
import paramiko
import subprocess

def ssh_connect(ip,user,passwd,command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.recv(1024)
    return

#please replace this parameter, with you'r infomation ssh server
ssh_connect('localhost','sulaiman','mantep21','id')
