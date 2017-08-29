#!/usr/bin/env python
""" Execute 'logging buffered <size>' with netmiko """

from netmiko import ConnectHandler
from test_devices import *

#devices = [pynet1, pynet2, juniper_srx]
devices = [pynet2]
password = '88newclass'

def main():
    for device in devices:
        device['password'] = password
        net_connect = ConnectHandler(**device)
        print (net_connect.send_command("show run | i buff"))
        net_connect.config_mode()
        net_connect.send_command("logging buffered 8192")
        net_connect.exit_config_mode()
        print (net_connect.send_command("show run | i buff"))       

if __name__ == "__main__":
    main()
