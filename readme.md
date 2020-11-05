### 背景

实验室网太差了，我一直在蹭楼下的网，不知道什么原因，最近wifi总是隔几分钟自己掉线，然后我手动断开wifi，再连接，他又好了。这样不是不能上网，但是隔几分钟被这样搞一下就很烦，于是决定写一个脚本自动完成这个工作。即隔一段时间检查一下网是不是断了，如果断了就自动连wifi。

### 具体实现

首先检查网络连通，我就用ping百度就可以了

```bash
ping baidu.com
```

如果ping不通，就会返回1，反之返回0

通过查阅相关资料，用命令行连接wifi的命令是：

```bash
netsh wlan connect name=b430 interface="WLAN 3"
```
其中，name是wifi的名字，WLAN 3是因为我有额外的网卡，指定某一个网卡来连接

### 程序部分

```python
import os
from time import sleep

cfg = {
    'check_time_period':1, #s
    'wlan_interface':'WLAN 3',
    'wifi_name':'b430'
}

if __name__ == "__main__":
    while True:
        res = os.system('ping baidu.com') # if fail retune 1, else 0
        if res == 1:
            connect_cmd = 'netsh wlan connect name={name} interface="{inter}"'.format(name=cfg['wifi_name'],inter=cfg['wlan_interface'])
            os.system(connect_cmd)
            print('reconnect')
        sleep(cfg['check_time_period'])    
            
```

通过测试，在启动脚本的情况下，手动断开wifi，会自动连接回去。

然后设一个计划任务，把这个脚本设为开机启动即可。