import os
import paramiko
import re

ssh = paramiko.SSHClient ()
ssh.set_missing_host_key_policy (paramiko.AutoAddPolicy ())

def fetch_bandex ():
    user = os.environ['LINUX_U']
    passwd = os.environ['LINUX_S']
    ssh.connect("linux.ime.usp.br", username=user, password=passwd)
    ssh_stdin, ssh_stdout, ssh_stderr = \
            ssh.exec_command ("/global/bin/bandex \n")
    out_str = str (ssh_stdout.read ().decode('utf-8'))
    terminal_codes_regex = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')
    out_str = terminal_codes_regex.sub ('', out_str)
    # print (out_str)
    ssh.close()
    return out_str

