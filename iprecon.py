#This script is built to gather ip,location and banner of the host url
#!/usr/bin/env python3
import requests
import sys
import json
import socket
import colorama
from colorama import Fore, Back, Style
import re

colorama.init(autoreset=True)


fail = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.RED}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"
success = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.GREEN}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"

def usage():
    print(fail + f"{Fore.RED} Usage{Fore.RESET}: python3 " + sys.argv[0] + " <url>")
    print(fail + f"{Fore.RED} Example{Fore.RESET}: python3 " + sys.argv[0] + " https://google.com")


def get_ip(url):
    return socket.gethostbyname(url)


def locate(ip):
    r = requests.get("https://ipinfo.io/" + ip + "/json")
    return json.loads(r.text)

def results(ip, location):
    print(success + "IP of " + f"{Fore.CYAN}" + sys.argv[1] + f"{Fore.RESET}" + " is " + ip)
    print(success + "Location: " + location["loc"])
    print(success + "Region: " + location["region"])
    print(success + "City: " + location["city"])
    print(success + "Country: " + location["country"])
    sys.exit(0)

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            usage()
            sys.exit(1)
        else:
            pattern = re.compile(r"https?://")
            target = pattern.sub("",sys.argv[1])
            ip = get_ip(target)
            location = locate(ip)
            results(ip, location)
    except:
        print("")
