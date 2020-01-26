# Enforce user to provide optional parameters
# This example won't run on Sololearn because it may require continuous input.
# Run the script with argument -h to see the help text.

import argparse

def process_args():
    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('-i', '--interface', help='Desired interface')
    parser.add_argument('-a', '--address', help='Desired address')
    args = parser.parse_args()
    interface = args.interface
    while not interface:
        interface = input("Please enter the interface: ")
    address = args.address
    while not address:
        address = input("Please enter the address: ")
    return interface, address

if __name__ == '__main__':
    interface, address = process_args()
    print(f"Interface = {interface}")
    print(f"Address   = {address}")
