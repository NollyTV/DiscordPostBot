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
remotepath = credentials['linuxremotepath']
localpath = "DiscordWebhookMessage.py"

ssh = paramiko.SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect(server, username=username, password=password)
sftp = ssh.open_sftp()
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()

