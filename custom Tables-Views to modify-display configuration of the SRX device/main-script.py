from jnpr.junos import Device
from customTables.BGPneighTable import BGPneighTable
import getpass

host_ip = input("Host: ")
host_user = input("Username: ")
host_pass = getpass.getpass("Password: ")

def list_groups(dev_table):
    print("#########################################")
    print("Getting the list of BGP groups.")
    dev_table.get()
    for group in dev_table:
        print("Group Name: {}".format(group.group_name))
        print("Group Type: {}".format(group.group_type))
        print("Group Peer AS: {}".format(group.group_peer_as))
        print("Group Local AS: {}".format(group.group_local_as))
        print("Neighbor: {}, Local Address: {}".format(group.neighbor_name,group.local_address))
    print("#########################################")

with Device(host=host_ip,user=host_user, passwd=host_pass,port=22) as dev:
    bgpt = BGPneighTable(dev)
    list_groups(bgpt)

    print("Defining a new BGP group.")
    bgpt.group_name='ext123'
    bgpt.group_type='external'
    bgpt.group_peer_as='65555'
    bgpt.group_local_as='64512'
    bgpt.neighbor_name='10.20.30.2'
    bgpt.local_address='10.20.30.1'
    print("Adding a new BGP group.")
    bgpt.append()
    bgpt.set(merge=True, comment="Table related commit. Adding ext123 group.")

    list_groups(bgpt)



