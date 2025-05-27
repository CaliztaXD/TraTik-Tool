import os
from time import sleep
from datetime import datetime

os.environ['TZ'] = 'Asia/Ho_Chi_Minh'

try:
    import requests
except:
    os.system("pip3 install requests")
    import requests

try:
    from pystyle import Colors, Colorate, Write, Center, Add, Box
except:
    os.system("pip3 install pystyle")
    from pystyle import Colors, Colorate, Write, Center, Add, Box

headers = {
    'authority': 'traodoisub.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'traodoisub tiktok tool',
}

def login_tds(token):
    try:
        r = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={token}', headers=headers, timeout=5).json()
        if 'success' in r:
            os.system('clear')
            print(Colors.green + f"Login successful!\nUser: {Colors.yellow + r['data']['user'] + Colors.green} | Current Xu: {Colors.yellow + r['data']['xu']}")
            return 'success'
        else:
            print(Colors.red + "Invalid TDS token, please check again!\n")
            return 'error_token'
    except:
        return 'error'

def load_job(type_job, token):
    try:
        r = requests.get(f'https://traodoisub.com/api/?fields={type_job}&access_token={token}', headers=headers, timeout=5).json()
        if 'data' in r:
            return r
        elif "countdown" in r:
            sleep(round(r['countdown']))
            print(Colors.red + f"{r['error']}\n")
            return 'error_countdown'
        else:
            print(Colors.red + f"{r['error']}\n")
            return 'error_error'
    except:
        return 'error'

def duyet_job(type_job, token, uid):
    try:
        r = requests.get(f'https://traodoisub.com/api/coin/?type={type_job}&id={uid}&access_token={token}', headers=headers, timeout=5).json()
        if "cache" in r:
            return r['cache']
        elif "success" in r:
            print(Colors.yellow + "------------------------------------------")
            print(f"{Colors.cyan}Task completed {r['data']['job_success']} | {Colors.green}{r['data']['msg']} | {Colors.yellow}{r['data']['xu']}")
            print(Colors.yellow + "------------------------------------------")
            return 'error'
        else:
            print(Colors.red + f"{r['error']}")
            return 'error'
    except:
        return 'error'

def check_tiktok(id_tiktok, token):
    try:
        r = requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={id_tiktok}&access_token={token}', headers=headers, timeout=5).json()
        if 'success' in r:
            os.system('clear')
            print(Colors.green + f"{r['data']['msg']} | ID: {Colors.yellow + r['data']['id'] + Colors.green}")
            return 'success'
        else:
            print(Colors.red + f"{r['error']}\n")
            return 'error_token'
    except:
        return 'error'

os.system('clear')
banner = r'''
████████╗██████╗░░█████╗░  ████████╗██╗██████╗░
╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██║██╔══██╗
░░░██║░░░██████╦╝██║░░██║  ░░░██║░░░██║██████╦╝
░░░██║░░░██╔══██╗██║░░██║  ░░░██║░░░██║██╔══██╗
░░░██║░░░██████╦╝╚█████╔╝  ░░░██║░░░██║██████╦╝
░░░╚═╝░░░╚═════╝░░╚════╝░  ░░░╚═╝░░░╚═╝╚═════╝░
'''
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner)))
print(Colors.red + Center.XCenter(Box.DoubleCube("TRA TIK - Free TDS TikTok Tool v1.0")))

table_menu = f"""
{Colors.green}+----+-------------+
| ID |   Action    |
+----+-------------+
| 1  | Follow      |
| 2  | Like (Heart)|
+----+-------------+"""
print(table_menu)

while True:
    try:
        with open('TDS.txt', 'r') as f:
            token_tds = f.read()
        cache = 'old'
    except FileNotFoundError:
        token_tds = Write.Input("Enter your TDS token: ", Colors.green_to_yellow, interval=0.0025)
        with open('TDS.txt', 'w') as f:
            f.write(token_tds)
        cache = 'new'

    for _ in range(3):
        check_log = login_tds(token_tds)
        if check_log in ['success', 'error_token']:
            break
        else:
            sleep(2)

    if check_log == 'success':
        break
    else:
        sleep(1)
        os.system('clear')

if check_log == 'success':
    try:
        with open('ID.txt', 'r') as f:
            id_tiktok = f.read()
    except FileNotFoundError:
        id_tiktok = Write.Input("Enter TikTok ID: ", Colors.green_to_yellow, interval=0.0025)
        with open('ID.txt', 'w') as f:
            f.write(id_tiktok)

    for _ in range(3):
        check_log = check_tiktok(id_tiktok, token_tds)
        if check_log in ['success', 'error_token']:
            break
        else:
            sleep(2)

while True:
    print(table_menu)
    try:
        choice = int(Write.Input("Choose job type: ", Colors.green_to_yellow, interval=0.0025))
        if choice in [1, 2]:
            break
    except:
        os.system('clear')

while True:
    try:
        delay = int(Write.Input("Enter delay time (seconds): ", Colors.green_to_yellow, interval=0.0025))
        if delay > 1:
            break
    except:
        os.system('clear')

while True:
    try:
        max_job = int(Write.Input("How many tasks before stop: ", Colors.green_to_yellow, interval=0.0025))
        if max_job > 9:
            break
    except:
        os.system('clear')

os.system('clear')

if choice == 1:
    type_load = 'tiktok_follow'
    type_duyet = 'TIKTOK_FOLLOW_CACHE'
    type_nhan = 'TIKTOK_FOLLOW'
    type_type = 'FOLLOW'
    api_type = 'TIKTOK_FOLLOW_API'
else:
    type_load = 'tiktok_like'
    type_duyet = 'TIKTOK_LIKE_CACHE'
    type_nhan = 'TIKTOK_LIKE'
    type_type = 'LIKE'
    api_type = 'TIKTOK_LIKE_API'

job_done = 0

while True:
    jobs = load_job(type_load, token_tds)
    sleep(2)
    if isinstance(jobs, dict):
        for job in jobs['data']:
            uid = job['id']
            link = job['link']
            os.system(f'termux-open-url {link}')
            check = duyet_job(type_duyet, token_tds, uid)

            if check != 'error':
                job_done += 1
                now = datetime.now().strftime("%H:%M:%S")
                print(f'{Colors.yellow}[{job_done}] {Colors.red}| {Colors.cyan}{now} {Colors.red}| {Colors.pink}{type_type} {Colors.red}| {Colors.light_gray}{uid}')
                if check > 9:
                    sleep(3)
                    duyet_job(type_nhan, token_tds, api_type)

            if job_done == max_job:
                break
            else:
                for i in range(delay, -1, -1):
                    print(Colors.green + f'Waiting: {i}s', end='\r')
                    sleep(1)

    if job_done == max_job:
        print(Colors.green + f"Completed {max_job} jobs!")
        break