#!/usr/bin/env python

"Get OIDs from devices"

from snmp_helper import snmp_get_oid, snmp_extract

IP = '184.105.247.70'
COMMUNITY_STRING = 'galileo'
SNMP_PORT = '161'

device1 = ('184.105.247.70', COMMUNITY_STRING, SNMP_PORT)
device2 = ('184.105.247.71', COMMUNITY_STRING, SNMP_PORT)

oid1 = '1.3.6.1.2.1.1.5.0'
oid2 = '1.3.6.1.2.1.1.1.0'

devices = [device1, device2]
oids = [oid1, oid2]

for device in devices:
    for oid_ in oids:
        snmp_data = snmp_get_oid(device, oid_)
        output = snmp_extract(snmp_data)
        print output + "\n"

def main():
    print 'done'








if __name__ == '__main__':
    main()


