#!/usr/bin/env python
""" Enter and verify config mode with netmiko """

from netmiko import ConnectHandler
from test_devices import *

devices = [pynet1, pynet2, juniper_srx]
password = '88newclass'

def main():
    for device in devices:
        device['password'] = password
        net_connect = ConnectHandler(**device)
        net_connect.config_mode()
        print "\n==========================\n\nChecking " + device['ip'] + " is in config mode..."
        print "\nConfig mode: {}".format(net_connect.check_config_mode())
        print "\nCurrent prompt: {}".format(net_connect.find_prompt())
    print "\n==========================\n"

if __name__ == "__main__":
    main()
