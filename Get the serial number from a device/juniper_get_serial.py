from pprint import pprint
from jnpr.junos import Device
import sys, getopt

#get the first argument: IP address
hostip = sys.argv[1]

#replace 'youruser','yourpass' with the respective data
#ideally username should be taken when running the script and not stored as clear text within the script
dev = Device(host=hostip, user='youruser', password='yourpass',port=22)
dev.open()

print ('*********************************************')
print ('Device IP:' + hostip)
#get the second argument of your choice
print ('Asset ref:'+ sys.argv[2])
print ('Serial number:'+dev.facts['serialnumber'])
print ('*********************************************')

#always logout to not keep loads of sessions on one ...
#device until it will expire. Multiple users plus a script...
#might lock the device.
dev.close() 