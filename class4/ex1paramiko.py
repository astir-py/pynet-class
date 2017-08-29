#!/usr/bin/env python

""" Get router version """

import paramiko
import time

ip_address = '184.105.247.71'
username = 'pyclass'
password = '88newclass'
port = 22

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip_address, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

remote_conn=remote_conn_pre.invoke_shell()

output=remote_conn.send("term len 0\n")
time.sleep(1)
output=remote_conn.recv(5000)
output=remote_conn.send("sh ver\n")
time.sleep(2)
output=remote_conn.recv(5000)
print output

