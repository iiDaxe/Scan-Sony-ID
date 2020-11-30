import requests
from colorama import Fore, init
import string
init()
import random
import urllib
from urllib import request
from lxml.html import fromstring
from itertools import cycle
import traceback
import re


def USERS(Number, IDLength):
    global Users
    if IDLength == 4:
        while True:
            x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-12345567890"
            a = random.choice(x)
            b = random.choice(x)
            c = random.choice(x)
            d = random.choice(x)
            if len(Users) == Number:
                break
            else:
                user = f"{a}{b}{c}{d}"
                Users.append(user)
    elif IDLength == 5:
        while True:
            x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-12345567890"
            a = random.choice(x)
            b = random.choice(x)
            c = random.choice(x)
            d = random.choice(x)
            e = random.choice(x)
            if len(Users) == Number:
                break
            else:
                user = f"{a}{b}{c}{d}{e}"
                Users.append(user)
    else:
        exit()


userAgint = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
]

proxy = []


def Scan_With_Proxy(username):
    global userAgint
    global proxy
    LisiUserAgent = str(random.choice(userAgint)).strip()
    UserAgentREQUEST = {"User-Agent": LisiUserAgent}
    random_address = random.choice(proxy)
    proxy = {f"http://{random_address}", f"https://{random_address}"}

    try:
        response = requests.post(
            'https://accounts.api.playstation.com/api/v1/accounts/onlineIds',
            headers=UserAgentREQUEST,
            proxies=proxy,
            json={
                "onlineId": username,
                "reserveIfAvailable": False
            })
    except Exception as e:
        print(str(e))
        pass
    if response.status_code == 400:
        print(Fore.RED, "[", Fore.LIGHTBLACK_EX, "-", Fore.RED, "]", Fore.RED,
              "ID: [ " + username + " ] Taken")

    elif response.status_code == 201:
        print(
            Fore.LIGHTWHITE_EX, "[ ", Fore.CYAN, "+", Fore.LIGHTWHITE_EX, " ]",
            Fore.LIGHTGREEN_EX, "ID:" + Fore.WHITE + " [ " + Fore.CYAN +
            username + Fore.WHITE + " ] " + Fore.LIGHTYELLOW_EX + " Available")
    else:
        print(response.status_code)
        print(response.content)


def Scan(username):
    global userAgint
    global proxy
    LisiUserAgent = str(random.choice(userAgint)).strip()
    UserAgentREQUEST = {"User-Agent": LisiUserAgent}

    try:
        response = requests.post(
            'https://accounts.api.playstation.com/api/v1/accounts/onlineIds',
            headers=UserAgentREQUEST,
            json={
                "onlineId": username,
                "reserveIfAvailable": False
            })
    except Exception as e:
        print(str(e))
        pass
    if response.status_code == 400:
        print(Fore.RED, "[", Fore.LIGHTBLACK_EX, "-", Fore.RED, "]", Fore.RED,
              "ID: [ " + username + " ] Taken")

    elif response.status_code == 201:
        print(
            Fore.LIGHTWHITE_EX, "[ ", Fore.CYAN, "+", Fore.LIGHTWHITE_EX, " ]",
            Fore.LIGHTGREEN_EX, "ID:" + Fore.WHITE + " [ " + Fore.CYAN +
            username + Fore.WHITE + " ] " + Fore.LIGHTYELLOW_EX + " Available")
    else:
        print(response.status_code)
        print(response.content)


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:299]:  #299 proxies max
        proxy = ":".join(
            [i.xpath('.//td[1]/text()')[0],
             i.xpath('.//td[2]/text()')[0]])
        proxies.add(proxy)
    return proxies


Users = []
print(
    Fore.LIGHTBLUE_EX, '''

  ██████  ▒█████   ███▄    █▓██   ██▓ ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▒██  ██▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒ ▒██ ██░▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒ ░ ▐██▓░▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░ ████▓▒░▒██░   ▓██░ ░ ██▒▓░▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒   ██▒▒▒ ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░▓██ ░▒░   ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░ ░ ░ ▒     ░   ░ ░ ▒ ▒ ░░  ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
      ░      ░ ░           ░ ░ ░     ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                             ░ ░     ░                       ░                               
''', Fore.WHITE)
NeedProxyOrNo = input(" [+] You Need Proxy With Scan [Y/N] : ").strip().upper()

if NeedProxyOrNo == 'Y':
    Proxss = input(
        " [+] You Have Proxy Or NEED random Proxies [Y/N] : ").strip().upper()

    if Proxss == "Y":
        FileProxy = input(" [+] Enter List For Proxy : ")
        OpenListProxy = open(FileProxy, 'r').readlines()
        for appendinproxylist in OpenListProxy:
            proxy.append(appendinproxylist)

    elif Proxss == "N":
        try:
            proxies = get_proxies()
            proxy.append(proxies)
            print("DONE")
        except:
            exit()

    print("", Fore.LIGHTWHITE_EX)
    random_or_no = input(" [+] You Need Random ID [Y/N]: ").strip().upper()

    if random_or_no == 'Y':
        IDLength = int(input(" [+] Enter Length ID [4/5] : "))
        numberofId = int(input(" [+] Enter How Many ID You NEED : "))
        USERS(numberofId, IDLength)
        for user in Users:
            Scan_With_Proxy(user)

    elif random_or_no == 'N':
        print("", Fore.LIGHTWHITE_EX)
        Filenmae = input(" [+] Enter ID List : ")
        openFile = open(Filenmae, 'r').readlines()
        for ID in openFile:
            Scan_With_Proxy(ID)

elif NeedProxyOrNo == 'N':
    print("", Fore.WHITE)
    random_or_no = input(" [+] You Need Random ID [Y/N]: ").strip().upper()
    if random_or_no == 'Y':
        IDLength = int(input(" [+] Enter Length ID [4/5] : "))
        numberofId = int(input(" [+] Enter How Many ID You NEED : "))
        USERS(numberofId, IDLength)
        for user in Users:
            Scan(user)
    elif random_or_no == 'N':
        print('', Fore.LIGHTGREEN_EX)
        Filenmae = input(" [+] Enter ID List : ")
        openFile = open(Filenmae, 'r').readlines()
        for ID in openFile:
            Scan(ID)
