import os
import paramiko
import json

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open('secret.json') as f:
    credentials = json.load(f)
username = credentials['linuxuser']
password = credentials['linuxpass']
server = credentials['linuxserver']
secretRemotePath = credentials['secretLocalRemotePath']
secretLocalPath = credentials['secretLocalPath']
payloadRemotePath = credentials['payloadRemotePath']
payloadLocalPath = credentials['payloadLocalPath']

ssh = paramiko.SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect(server, username=username, password=password)
sftp = ssh.open_sftp()
sftp.put(secretLocalPath, secretRemotePath)
sftp.put(payloadLocalPath, payloadRemotePath)
sftp.close()
ssh.close()

