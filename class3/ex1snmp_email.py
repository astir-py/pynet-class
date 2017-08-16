#!/usr/bin/env python

""" Send email on config change """

from snmp_helper import snmp_get_oid_v3, snmp_extract

SNMP_PORT = '161'

# Devices
pynet_rtr1 = ("184.105.247.70", SNMP_PORT)
pynet_rtr2 = ("184.105.247.71", SNMP_PORT)

devices = [pynet_rtr1, pynet_rtr2]

# User credentials
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

snmp_user = (a_user, auth_key, encrypt_key)

# OIDs
# Uptime when running config last changed
oid = '1.3.6.1.4.1.9.9.43.1.1.1.0'   

# Uptime when running config last saved (note any 'write' constitutes a save)    
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'   

# Uptime when startup config last saved   
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'


#oid = [ccmHistoryRunningLastChanged]

# read OIDs from devices
for device in devices:
    snmp_data = snmp_get_oid_v3(device, snmp_user, oid)
    lastchanged = snmp_extract(snmp_data)
    print(lastchanged + "\n")

