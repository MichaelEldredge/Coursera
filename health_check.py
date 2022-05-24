#!/usr/bin/env python3
import psutil
import shutil
from os.path import expanduser
import socket


print("CPU usage is less than 80%")
cpu_use_test = psutil.cpu_percent(1) < 80
print(cpu_use_test)

stat = shutil.disk_usage(expanduser("~"))
print("Disk space use is less than 80%:")
disk_space_test = stat[1]/stat[0] < .8
print(disk_space_test)

print("At least 500 MB of memory:")
memory_test = psutil.virtual_memory().available / 2 ** 20 > 500
print(memory_test)

print("localhost resolves to 127.0.0.1")
localhost_ip_test =  socket.gethostbyname('localhost') == "127.0.0.1"
print(localhost_ip_test)