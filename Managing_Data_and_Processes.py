
###Python Subprocesses



#Running System Commands

import subprocess

subprocess.run(["date"])
#Thu Oct 12 09:57:34 PM CEST 2023
#CompletedProcess(args=['date'], returncode=0)

subprocess.run(["sleep", "2"])
#CompletedProcess(args=['sleep', '2'], returncode=0)

result = subprocess.run(["ls", "this_file_does_not_exist"])
#ls: cannot access 'this_file_does_not_exist': No such file or directory
print(result.returncode)
#2



#Obtaining the Output of a System Command

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
#0
print(result.stdout)
#b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
print(result.stdout.decode().split())
#['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']


result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
#1
print(result.stdout)
#b''
print(result.stderr)
#b"rm: cannot remove 'does_not_exist': No such file or directory\n"




#Advanced Subprocess Management


#modifying the environment of a child process
import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)



###Processing Lof Files


#Filtering Log Files with Regular Expressions

#check_cron.py     
#!/usr/bin/env python3
import sys

logfile = sys.argv[1]
with open (logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        print(line.strip())


#cat syslog
#Jul 6 14:04:07 computer.name CRON[29440]: USER (good_user)
#Jul 6 14:04:07 computer.name CRON[29187]: USER (UUID:007)
#Jul 6 14:04:07 computer.name CRON[29440]: USER (naughty_user)
#Jul 6 14:04:07 computer.name CRON[29187]: USER (UUID:008)
#Jul 6 14:04:07 computer.name CRON[29440]: USER (naughty_user)

import re

pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:04:07 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])
#naughty_user



import re
import sys

logfile = sys.argv[1]
with open (logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)

        print(result[1])

#cmod +x check_cron.py 
#./check_cron.py syslog
# 
# good_user
# naughty_user
# naughty_user       





#Problem: We're using the same syslog, and we want to display the date, time, 
# and process id that's inside the square brackets. We can read each line of the syslog and pass the contents 
# to the show_time_of_pid function. Fill in the gaps to extract the date, time, and process id from the passed line, 
# and return this format: Jul 6 14:01:23 pid:29440.

import re
def show_time_of_pid(line):
  pattern = r'^(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+) [\w\.]+ [\w=]+\[([0-9]+)\]'
  result = re.search(pattern, line)
  return '{} pid:{}'.format(result[1],result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440






#Making Sense out of the Data

usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) +1
print(usernames)
#{'good_user': 1}
usernames[name] = usernames.get(name, 0) +1
print(usernames)
#{'good_user': 2}


import re
import sys

logfile = sys.argv[1]
usernames = {}
with open (logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) +1
print(usernames)


#./check_cron.py syslog
#
#{'good_user': 1, 'naughty_user': 2}

