from flask import Flask, request, render_template
from jinja2 import Template
import ipcalc
import inspect
import ipaddress

from pprint import pprint
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    name = request.args.get('name')
    return render_template('ipcalculator.html')

@app.route("/ipcalcs", methods=['GET', 'POST'])
def ipcalcs():
    try:
        ipcalc_subnet = request.form.get('ipcalc_subnet')
        network_address = ipaddress.ip_network(ipcalc_subnet, strict=False)
        network_netmask = network_address.netmask
        #https://docs.python.org/3/howto/ipaddress.html
        if "/31" in str(ipcalc_subnet):
            network_hostmin = network_address[0]
            network_hostmax = network_address[-1]
            network_qty_hosts = 0
            network_broadcast = 'n/a'
        elif "/32" in str(ipcalc_subnet):
            network_hostmin = network_address[0]
            network_hostmax = network_address[0]
            network_qty_hosts = 0
            network_broadcast = 'n/a'
        else:
            network_hostmin = network_address[1]
            network_hostmax = network_address[-2]
            network_qty_hosts = network_address.num_addresses-2
            network_broadcast = network_address[-1]
    except ValueError:
            print('address/netmask is invalid for IPv4:', ipcalc_subnet)
            ipcalc_subnet='address/netmask is invalid for IPv4'
            network_address=''
            network_netmask=''
            network_hostmin=''
            network_hostmax=''
            network_broadcast=''
            network_qty_hosts=''
    return render_template(
    'ipcalculator.html'
    ,ipcalc_subnet=ipcalc_subnet
    ,network_address=network_address
    ,network_netmask=network_netmask
    ,network_hostmin=network_hostmin
    ,network_hostmax=network_hostmax
    ,network_broadcast=network_broadcast
    ,network_qty_hosts=network_qty_hosts
    )

if __name__ == '__main__':
    app.run()
