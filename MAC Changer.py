import subprocess
import re

def change_mac(interface, new_mac):
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    subprocess.call("clear", shell=True)
    subprocess.call("ifconfig " + interface , shell=True)
    print("\n \n[+]Done!")

show_interface = input("[+] Show interfaces? y/n: ")

if show_interface.lower() == "y":
    subprocess.call("\n ifconfig -s", shell=True)

interface = input("\n[+]Please select an interface: ")
new_mac = input("\n[+]Enter the new MAC address: ")

change_mac(interface, new_mac)

ifconfig_result = subprocess.check_output("ifconfig", interface)

changed_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if changed_mac:
    print("[+] Your new MAC address is ", changed_mac)
else:
    print("[-] Could not find MAC address")
