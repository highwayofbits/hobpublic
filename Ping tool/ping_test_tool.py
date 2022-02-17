from pprint import pprint

#juniper library that will let us login to the device and perform actions
from jnpr.junos import Device

#we will use this to pass arguments to the script from the command line
import sys

#user will have to input a password which will be hashed #this will be taken from the command line that will be run
import getpass

#grab the argument passed when the script was run
hostip = sys.argv[1]

#get username. in the previous version of python we would use raw_input function instead
username = input("Username:")

#get pass - hidden while typing
passwd = getpass.getpass("Password for " + username + ":")

#connect to the device (NETCONF SSH will be on port 22)
dev = Device(host=hostip, user=username, password=passwd,port=22)
dev.open()

#get the serial number
print ('Serial number:'+dev.facts['serialnumber'])

#get info about the interface fe-0/0/6
sw = dev.rpc.get_interface_information(interface_name='fe-0/0/6')

#find name,IP of the first unit
print (sw.xpath(".//logical-interface/name")[0].text)
ip1 = (sw.xpath(".//interface-address/ifa-local")[0].text) print(ip1)

#run ping command
xmldata=(dev.rpc.ping(count='2', source=ip1, host=ip1,normalize='true'))

#validate the output of ping:
#if ping will fail it will give you the failure reason.
#if there will be 0% packet loss it will give you basic stats
if (xmldata.xpath(".//responses-received")[0].text) == '0':
  print ('Ping failure reason:' + (xmldata.xpath(".//ping-failure")[0].text))
  print ('Error Message:' + (xmldata.xpath(".//error-message")[0].text))
  print ('Packet loss:'+(xmldata.xpath(".//packet-loss")[0].text))
  print ('Probes sent:'+(xmldata.xpath(".//probes-sent")[0].text))
  print ('Responses received:'+(xmldata.xpath(".//responses- received")[0].text))
else:
  print ('RTT Average:' + (xmldata.xpath(".//rtt-average")[0].text))
  print ('RTT Minimum:' + (xmldata.xpath(".//rtt-minimum")[0].text))
  print ('RTT Maximum:' + (xmldata.xpath(".//rtt-maximum")[0].text))
  print ('Packet loss:'+(xmldata.xpath(".//packet-loss")[0].text))
  print ('Probes sent:'+(xmldata.xpath(".//probes-sent")[0].text))
  print ('Responses received:'+(xmldata.xpath(".//responses-received")[0].text))

#Always close the session. Otherwise you will lock the device with too many logged in users.
dev.close()