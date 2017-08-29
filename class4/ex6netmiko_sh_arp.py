#!/usr/bin/env python
""" Show arp with netmiko """

from netmiko import ConnectHandler
from test_devices import *

devices = [pynet1, pynet2, juniper_srx]
password = '88newclass'

def main():
    for device in devices:
        device['password'] = password
        net_connect = ConnectHandler(**device)
        arptab = net_connect.send_command("sh arp")
        print "\n==========================\n\nARP table of " + device['ip'] + ":\n"
        print arptab
    print "\n==========================\n"

if __name__ == "__main__":
    main()
