from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell

# Use "getpass" in real script. Demonstration script only
dev = Device(host="x.x.x.x", user="user", passwd="pass")

with StartShell(dev) as ss:
    tuple_result = ss.run('cli -c "monitor traffic interface ge-1/0/5 no-resolve size 1500"', this=None, timeout=15)
    command_results = tuple_result[1]
    print(command_results)
