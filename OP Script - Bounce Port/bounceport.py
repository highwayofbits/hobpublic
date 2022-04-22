from jnpr.junos import Device
from jnpr.junos.exception import *
from jnpr.junos.utils.config import Config
import argparse
from time import sleep

arguments = {
    "interface": "Port Name to bounce",
    "sleep": "Time to wait before enabling the port."
}

def apply_config(device_instance, commands):
    try:
        with Config(device_instance) as cu:
            print("Action: Loading the configuration")
            cu.load(commands, format = "set")
            print("Action: Committing the configuration")
            cu.commit()
    except:
        print("There was an issue with applying the configuration.")
        return False

    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    for key in arguments:
        parser.add_argument('-' + key, required=True, help=arguments[key])
    args = parser.parse_args()
    print(args)

    with Device() as dev:
        print("Disabling the port.")
        if apply_config(dev, "set interfaces " + args.interface + " disable"):
            print ("Sleeping " + str(args.sleep) + " before enabling the port.")
            sleep(float(args.sleep))

            print("Enabling the port.")
            if apply_config(dev, "delete interfaces " + args.interface + " disable"):
                print("The port is fully bounced!")
            else:
                print("Something went wrong. The interface will stay disabled.")
