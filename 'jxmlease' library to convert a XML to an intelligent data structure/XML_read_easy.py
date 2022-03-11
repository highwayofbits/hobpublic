from jnpr.junos import Device
import jxmlease
import getpass

host_ip = input("Host: ")
host_user = input("Username: ")
host_pass = getpass.getpass("Password: ")

with Device(host=host_ip,user=host_user, passwd=host_pass, port=22) as dev:
    list_of_interfaces = dev.rpc.get_interface_information(terse=True, interface_name='ge-0/0/7')
    myparser = jxmlease.EtreeParser()
    myxml_converted = myparser(list_of_interfaces)
    print("Printing the converted data as dictionary:")
    print(myxml_converted)

    for interface in  myxml_converted['interface-information']['physical-interface']:
        print ('Interface: {}, Admin Status: {}, Operational Status: {}'.format(interface['name'],
                                                                                interface['admin-status'],
                                                                                interface['oper-status']))

