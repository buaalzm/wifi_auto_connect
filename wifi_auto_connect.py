import os
from time import sleep
from datetime import datetime

cfg = {
    'check_time_period':5, #s
    'wlan_interface':'WLAN 3',
    'wifi_name':'b430'
}

def log():
    os.chdir(r'D:\Code\wifi_auto_connect')
    if not os.path.exists('log'):
        os.mkdir('log')
    filename = datetime.now().strftime('%Y-%m-%d')+'.log'
    path = os.path.join('log',filename)
    
    with open(path,'a+') as log_file:
        log_file.write(datetime.now().strftime("%Y/%m/%d, %H:%M:%S")+'\n')

if __name__ == "__main__":
    while True:
        res = os.system('ping baidu.com -n 2') # if fail retune 1, else 0
        if res == 1:
            connect_cmd = 'netsh wlan connect name={name} interface="{inter}"'.format(name=cfg['wifi_name'],inter=cfg['wlan_interface'])
            os.system(connect_cmd)
            print('reconnect')
            log()
        sleep(cfg['check_time_period'])    
            