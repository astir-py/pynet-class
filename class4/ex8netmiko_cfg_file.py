#!/usr/bin/env python
""" Configure devices from file with netmiko """

from netmiko import ConnectHandler
from test_devices import *

#devices = [pynet1, pynet2, juniper_srx]
devices = [pynet1, pynet2]
password = '88newclass'

def main():
    for device in devices:
        device['password'] = password
        net_connect = ConnectHandler(**device)
        print "\n" + device['ip'] + " before:\n {}".format(net_connect.send_command("sh ru | i buf|gi.*co"))
        net_connect.send_config_from_file(config_file = 'config_file.txt')
        print "\n" + device['ip'] + " after:\n {}".format(net_connect.send_command("sh ru | i buf|gi.*co"))


if __name__ == "__main__":
    main()
