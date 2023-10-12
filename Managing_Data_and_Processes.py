#Python Subprocesses




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


