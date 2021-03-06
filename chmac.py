#!/usr/bin/env python3
import os
import time
import sys
import random
import subprocess
import re
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

fail = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.RED}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"
success = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.GREEN}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"

class chmac:
    def __init__(self):
        self.mac = ""
        

    def get_mac(self, interface):
        out = subprocess.run(["ifconfig", interface], shell = False, capture_output = True).stdout.decode("utf-8")
        pattern = r'([0-9a-fA-F]{2}:?){6}'
        regex = re.compile(pattern)
        mac_addr = regex.search(out).group()
        self.mac = mac_addr
        return mac_addr


    def change_mac(self, interface, new_mac):
        subprocess.run(["ifconfig", interface, "down"], shell = False, capture_output = True)
        subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], shell = False, capture_output = True)
        subprocess.run(["ifconfig", interface, "up"], shell = False, capture_output = True)


    def gen_mac(self):
        local = ["2", "6", "a", "e"]
        _hex = [
                "0", 
                "1", 
                "2", 
                "3", 
                "4", 
                "5", 
                "6", 
                "7", 
                "8", 
                "9", 
                "a", 
                "b", 
                "c", 
                "d", 
                "e", 
                "f"
                ]
        random_mac = f"{random.choice(_hex)}{random.choice(local)}:{random.choice(_hex)}{random.choice(_hex)}:{random.choice(_hex)}{random.choice(_hex)}:{random.choice(_hex)}{random.choice(_hex)}:{random.choice(_hex)}{random.choice(_hex)}:{random.choice(_hex)}{random.choice(_hex)}"
        return random_mac


if __name__ == "__main__":
    if os.geteuid() == 0:
        pass
    else:
        print(f"{fail} You must run this as root")
        sys.exit(1)
    if len(sys.argv) < 2:
        print(f"{fail} Usage: python3 {sys.argv[0]} <INTERFACE> [<MAC>(optional)]")
        print(f"{fail} Example: python3 {sys.argv[0]} eth0 [2a:34:56:f6:a9:0b (optional)]") 
    else:
        mc = chmac()
        interface = sys.argv[1]
        old_mac = mc.get_mac(interface)
        new_mac = sys.argv[2] if len(sys.argv) == 3 else mc.gen_mac()
        print(f"{success} Current MAC - {old_mac}")
        print(f"{success} Changing MAC to {new_mac}")
        time.sleep(1)
        mc.change_mac(interface, new_mac)
        if old_mac == new_mac:
            print(f"{fail} Error Changing MAC")
        else:
            print(f"{success} MacAddress changed successfully")



