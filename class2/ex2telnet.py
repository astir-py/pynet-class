#!/usr/bin/env python

"""Telnet to router and show ip interfaces"""

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    ip_address = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    connect = telnetlib.Telnet(ip_address, TELNET_PORT, TELNET_TIMEOUT)
    output = connect.read_until("name:", TELNET_TIMEOUT)
    connect.write(username + "\n")
    output = connect.read_until("sword:", TELNET_TIMEOUT)
    connect.write(password +"\n")
    time.sleep(1)

    connect.write("sh ip int br" + "\n")
    time.sleep(2)
    output = connect.read_very_eager()
    print output

    connect.close()

if  __name__ == '__main__':
    main()
