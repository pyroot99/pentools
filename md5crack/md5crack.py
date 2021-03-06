#!/usr/bin/env python3
import argparse
import hashlib
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
fail = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.RED}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"
success = f"{Fore.YELLOW}[{Style.BRIGHT}{Fore.GREEN}+{Style.NORMAL}{Fore.YELLOW}]{Style.RESET_ALL}"

def parse_it():
    parser = argparse.ArgumentParser(description="MD5 HashCracker", usage = f"{success} md5crack.py --md5 HASH --wordlist WORDLIST" )
    parser.add_argument("--md5", dest="hash", help="md5 hash", required=True)
    parser.add_argument("--wordlist", dest="wordlist", help="wordlist file", required=True)
    arguments = parser.parse_args()
    return arguments


def wordlist(arguments):
    with open(arguments.wordlist) as f:
        arr = f.read().splitlines()
    return arr


def crack(arguments, arr):
    cracked = ""
    for word in arr:
        if hashlib.md5(bytes(word, encoding = 'utf-8')).hexdigest() == arguments.hash:
            print(f"{success}MD5 hash has been cracked: {Fore.GREEN}{word}{Fore.RESET}")
            cracked = word
            break
    if cracked == "":
        print(f"{fail} Failed to crack.\n{fail} Try using a {Fore.RED}different/bigger{Fore.RESET} wordlist")


if __name__ == '__main__':
    arguments = parse_it()
    arr = wordlist(arguments)
    crack(arguments, arr)

