#!/usr/bin/env python
""" Perform 'logging buffered <size>' using pexpect """

import pexpect

ip_address = '184.105.247.71'
username = 'pyclass'
password = '88newclass'
port = 22

def main():
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_address, port))
    ssh_conn.timeout = 5
    ssh_conn.expect('ssword')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')
    ssh_conn.sendline('sh run | i buf')
    ssh_conn.expect('#')
    print "\n" + ssh_conn.before + ssh_conn.after
    ssh_conn.sendline('conf t')
    ssh_conn.expect('#')
    ssh_conn.sendline('logging buf 16384')
    ssh_conn.expect('#')
    ssh_conn.sendline('exit')
    ssh_conn.expect('#')
    ssh_conn.sendline('sh run | i buf')
    ssh_conn.expect('#')
    print "\n" + ssh_conn.before + ssh_conn.after

if __name__ == "__main__":
    main()
