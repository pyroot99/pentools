#!/usr/bin/env python3
import concurrent.futures
import requests
import sys
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
success = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.GREEN}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"
fail = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.RED}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"


def usage():
    print(f"{success} Usage: python3 {sys.argv[0]} <wordlist> <url> ")
    print(f"{success} Example: python3 {sys.argv[0]} sub.txt https://google.com ")


def make_subd_list(filename):
    with open(filename, 'r') as f:
        subd_list = f.read().splitlines()
    return subd_list


def fuzz(sub):
    try:
        temp_status_code = requests.get(f"{arr[0]}//{sub}.{arr[1]}").status_code
        if temp_status_code == 200:
            status_code = f"{Fore.GREEN}{temp_status_code}{Fore.RESET}"
        else:
            status_code = f"{Fore.RED}{temp_status_code}{Fore.RESET}"
        print(f"{success} {sub:<15} :{status_code}")
    except requests.exceptions.ConnectionError:
        pass


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)
    else:
        filename = sys.argv[1]
        base_url = sys.argv[2]
        arr = base_url.split("//")
        subd_list = make_subd_list(filename)
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(fuzz, subd_list)
        except KeyboardInterrupt:
            print(f"\n{fail}{Fore.RED} Exiting{Fore.RESET}")
            sys.exit(1)
