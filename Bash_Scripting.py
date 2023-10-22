### Basic Linux Command

# echo - used to print messages to the screen
# cat -  showing contents of files
# ls -  list the names of the files contained in directory
# chmod - change permissions of a file
# mkdir - create a new directory
# cd - change into directory
# pwd - print the current working directory
# cp - copy files
# touch - create an empty file
# ls -l  - shows the contents of a directory
# ls -la - shows hidden files 
# mv - rename or move a file
# cp - copy a file
# rm - delete files one by one / rm * - delete all files
# cd .. - change to the previous directory
# rmdir - delete directory


# mkdir mynewdir
# cd mynewdir
# pwd   
# cp ../spider.txt .
# touch myfile.txt
# ls -l
# ls -la
# mv myfile.txt emptyfile.txt
# cp spider.txt yetanotherfile.txt
# rm *
# ls -l
# rmdir mynewdir/
# ls mynewdir



###Redirecting Streams


#cat stdout_example.py

#!/usr/bin/env python3

print("Dont mind me, just a bit of text here...")

#./stdout_example.py
"""Dont mind me, just a bit of text here..."""
#./stdout_example,py > newfile.txt
#cat newfile.txt
"""Dont mind me, just a bit of text here..."""
#./stdout_example,py >> newfile.txt        ##append the output of a command to a .txt file
#cat newfile.txt
"""Dont mind me, just a bit of text here...
Dont mind me, just a bit of text here..."""


###redirect standard input.


#cat streams.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT " + data)
raiseValueError("Now we generate an error to STDERR")

#./streams.py < newfile.txt               


###redirecting the err output to a separate file

#./streams.py < newfile.txt 2> error_file.txt
#cat error_file.txt


### create a file using the echo command and redirecting its output to the file that we want to create
#echo "These are the contents of the file" > myamazingfile.txt
#cat myamazingfile.txt






###Pipes and Pipelines

# ls -l | less
#q


#cat spider.txt | tr ' ' ' \n' | sort | uniq - c | sort -nr | head

#       7 the
#       3 up
#       3 spider
#       3 and
#       2 rain
#       2 itsy
#       2 climbed
#       2 came
#       2 bitsy
#       1 waterspout.



# cat_capitalize.py

#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())

# cat haiku.txt
"""
advance your carrer,
automating with Python,
its so fun to learn.
"""
# cat hailu.txt | ./capitalize.py
"""
Advance your carrer,
Automating with Python,
Its so fun to learn.
"""
# ./capitalize.py < hailku.txt
"""
Advance your carrer,
Automating with Python,
Its so fun to learn.
"""





###Signalling Processes


# ping www.example.com
"""
4 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=53 time=153 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=53 time=171 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=53 time=193 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=4 ttl=53 time=216 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=5 ttl=53 time=136 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=6 ttl=53 time=115 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=7 ttl=53 time=129 ms
"""
#CTRL+C    (SIGINT)
"""
--- www.example.com ping statistics ---
7 packets transmitted, 7 received, 0% packet loss, time 6008ms
rtt min/avg/max/mdev = 115.113/158.963/215.701/33.564 ms
"""
# ping www.example.com
"""
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=53 time=210 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=53 time=137 ms
"""
#CTRL+C    (SIGSTOP)
"""
[1]+  Stopped                 ping www.example.com
"""
#fg




# kill - SIGTERM 
# PID - process identifier
# ps - list the currently running processes
# ps ax - lists all the running processes in the current computer
# grep - to only keep lines that contain the name of the process that we're looking for. 


# (1st terminal) ping www.example.com 
# (2nd terminal) ps ax | grep ping
"""
 2560 ?        Ssl    0:01 /usr/libexec/gsd-housekeeping
  25797 pts/1    S+     0:00 ping www.example.com
  25806 pts/2    S+     0:00 grep --color=auto ping
"""

# So our PS and grip commands found that the PID for the running ping command is 25797. 
# We can now use this identifier to send the signal that we want using the Killcommand. 

# kill 25797

"""Managing files and directories

    cd directory: changes the current working directory to the specified one

    pwd: prints the current working directory

    ls: lists the contents of the current directory

    ls directory: lists the contents of the received directory  

    ls -l: lists the additional information for the contents of the directory  

    ls -a: lists all files, including those hidden  

    ls -la: applies both the -l and the -a flags  

    mkdir directory: creates the directory with the received name

    rmdir directory: deletes the directory with the received name (if empty)

    cp old_name new_name: copies old_name into new_name

    mv old_name new_name: moves old_name into new_name

    touch file_name: creates an empty file or updates the modified time if it exists

    chmod modifiers files: changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable

    chown user files: changes the owner of the files to the given user

    chgrp group files: changes the group of the files to the given group

Operating with the content of files

    cat file: shows the content of the file through standard output

    wc file: counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin

    file file: prints the type of the given file, as recognized by the operating system

    head file: shows the first 10 lines of the given file

    tail file: shows the last 10 lines of the given file

    less file: scrolls through the contents of the given file (press "q" to quit)

    sort file: sorts the lines of the file alphabetically

    cut -dseparator -ffields file: for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

Additional commands

    echo "message": prints the message to standard output

    date: prints the current date

    who: prints the list of users currently logged into the computer

    man command: shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)

    uptime: shows how long the computer has been running

    free: shows the amount of unused memory on the current system  


Redirections, Pipes and Signals
Managing streams

    command > file: redirects standard output, overwrites file

    command >> file: redirects standard output, appends to file

    command < file: redirects standard input from file

    command 2> file: redirects standard error to file

    command1 | command2: connects the output of command1 to the input of command2

Operating with processes

    ps: lists the processes executing in the current terminal for the current user

    ps ax: lists all processes currently executing for all users  

    ps e: shows the environment for the processes listed  

    kill PID: sends the SIGTERM signal to the process identified by PID

    fg: causes a job that was stopped or in the background to return to the foreground

    bg: causes a job that was stopped to go to the background

    jobs: lists the jobs currently running or stopped

    top: shows the processes currently using the most CPU time (press "q" to quit)  """





###Creating Bash Scripts

#!/bin/bash

echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"

# ./gather-information.sh


#!/bin/bash

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"

# ./gather-information.sh







###Using Variables and Globs

example=hello
echo$example

#hello


#!/bin/bash

line="____________________________"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"

# ./gather-information.sh


echo *.py
#the shell turns it into a list containing all the filenames to end with py in the current directory

echo c*
#et the list of all files that start with a certain prefix. 

echo * 
#We can also use a star with no prefix or suffix which would match all the files in the current directory. 

echo ?????.py
#the question mark symbol can be used to match exactly one character instead of any amount of characters, 







### Conditional Execution in Bash



#cat check_localhost.sh

#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
        echo "Everything is OK!"
else
        echo "ERROR! 127.0.0.1 is not en /etc/hosts"
fi

#chmod +x check_localhost.sh
#./check_localhost.sh

127.0.0.1	localhost
Everything is OK!

#if test -n "$PATH"; then echo "Your path is not empty"; fi

Your path is not empty

#if [ -n "$PATH" ]; then echo "Your path is not empty"; fi



#https://ryanstutorials.net/bash-scripting-tutorial/

#https://linuxconfig.org/bash-scripting-tutorial-for-beginners

#https://www.shellscript.sh




### Advanced Bash Concepts



### While Loops in Bash Scripts

#cat while.sh
#chmod +x while.sh

#!/bin/bash

n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done

#./while.sh

"""
Iteration number 1
Iteration number 2
Iteration number 3
Iteration number 4
Iteration number 5
"""



#cat random-exit.py

#!/usr/bin/env python

import sys
import random

value=random.randint(0,3)
print("Returning: " + str(value))
sys.exit(value)

#chmod +x random-exit.py
#./random-exit.py
"""
Returning: 1
"""
#./random-exit.py
"""
Returning: 3
"""
#./random-exit.py
"""
Returning: 1
"""


#atom retry.sh
#chmod +x retry.sh

#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n+=1))
    echo "Retry #$n"
done;

#./retry.sh ./random-exit.py
"""
Returning: 3
Retry #1
Returning: 2
Retry #2
Returning: 1
Retry #3
Returning: 0
"""


### For Loops in Bash Scripts


# cat fruits.sh

#!/bin/bash

for fruit in peach orange apple; do
    echo "I like $fruit"
done

# ./fruits.sh
"""
I like peach
I like orange
I like apple
"""


# cd old_website/
# ls -l
"""
total 0
-rw-r--r-- 1 user user 0 May 24  2019 about.HTM
-rw-r--r-- 1 user user 0 May 24  2019 contact.HTM
-rw-r--r-- 1 user user 0 May 24  2019 footer.HTM
-rw-r--r-- 1 user user 0 May 24  2019 header.HTM
-rw-r--r-- 1 user user 0 May 24  2019 index.HTM
"""
# basename index.HTM .HTM
"""index"""

#!/bin/bash

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    echo mv "$file" "$name.html"
done

# chmod +x rename.sh
# ./rename.sh
"""
mv about.HTM about.html
mv contact.HTM contact.html
mv footer.HTM footer.html
mv header.HTM header.html
mv index.HTM index.html
"""

#!/bin/bash

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html"
done
    
# ./rename.sh
#ls -l

"""
total 0
-rw-r--r-- 1 user user 0 May 24  2019 about.html
-rw-r--r-- 1 user user 0 May 24  2019 contact.html
-rw-r--r-- 1 user user 0 May 24  2019 footer.html
-rw-r--r-- 1 user user 0 May 24  2019 header.html
-rw-r--r-- 1 user user 0 May 24  2019 index.html
"""




### Advanced Command Interaction

# tail /var/log/syslog
# tail /var/log/syslog | cut -d' ' -f5-
# cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head

# cat toploglines.sh

#!/bin/bash

for logfile in var/log/*log; do
    echo "Processing $logfile"
    cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head
done

#./toploglines.sh






### Qwiklabs Assessment: Editing Files Using Substrings

"""
cat [file] - The cat command allows us to create single or multiple files, view the contents of a file, concatenate files, 
and redirect output in terminal or other files.

grep [pattern] [file-directory] - The grep command, which stands for "global regular expression print", 
processes text line-by-line and prints any lines that match a specified pattern.

cut [options] [file] - The cut command extracts a given number of characters or columns from a file. 
A delimiter is a character or set of characters that separate text strings.

cut -d [delimiter] -f [field number] - For delimiter separated fields, the - d option is used. 
The -f option specifies the field, a set of fields, or a range of fields to be extracted.
"""

## Linux I/O Redirection

"""
Redirection is defined as switching standard streams of data from either a user-specified source or user-specified destination. 
Here are the following streams used in I/O redirection:

    Redirection into a file using >
    Append using >>

Redirection into a file

Each stream uses redirection commands. A single greater than sign (>) or a double greater than sign (>>) 
can be used to redirect standard output.
If the target file doesn't exist, a new file with the same name will be created.
Commands with a single greater than sign (>) overwrite existing file content.

cat > [file]

Commands with a double greater than sign (>>) do not overwrite the existing file content, but it will append to it.

cat >> [file]

So, rather than creating a file, the >> command is used to append a word or string to the existing file.
"""



# cd data
# cat list.txt
"""
001 jane /data/jane_profile_07272018.doc
002 kwood /data/kwood_profile_04022017.doc
003 pchow /data/pchow_profile_05152019.doc
004 janez /data/janez_profile_11042019.doc
005 jane /data/jane_pic_07282018.jpg
006 kwood /data/kwood_pic_04032017.jpg
007 pchow /data/pchow_pic_05162019.jpg
008 jane /data/jane_contact_07292018.csv
009 kwood /data/kwood_contact_04042017.csv
010 pchow /data/pchow_contact_05172019.csv"""

# ls
"""
jane_contact_07292018.csv   kwood_profile_04022017.doc
jane_profile_07272018.doc   list.txt
janez_profile_11042019.doc  pchow_pic_05162019.jpg
kwood_pic_04032017.jpg
"""

# grep 'jane' ../data/list.txt
"""
001 jane /data/jane_profile_07272018.doc
004 janez /data/janez_profile_11042019.doc
005 jane /data/jane_pic_07282018.jpg
008 jane /data/jane_contact_07292018.csv
"""

# grep ' jane ' ../data/list.txt
"""
001 jane /data/jane_profile_07272018.doc
005 jane /data/jane_pic_07282018.jpg
008 jane /data/jane_contact_07292018.csv
"""

# grep " jane " ../data/list.txt | cut -d ' ' -f 1
"""
001
005
008
"""

# grep " jane " ../data/list.txt | cut -d ' ' -f 2
"""
jane
jane
jane
"""

# grep " jane " ../data/list.txt | cut -d ' ' -f 3
"""
/data/jane_profile_07272018.doc
/data/jane_pic_07282018.jpg
/data/jane_contact_07292018.csv
"""

# grep " jane " ../data/list.txt | cut -d ' ' -f 1-3
"""
001 jane /data/jane_profile_07272018.doc
005 jane /data/jane_pic_07282018.jpg
008 jane /data/jane_contact_07292018.csv
"""

# grep " jane " ../data/list.txt | cut -d ' ' -f 1,3
"""
001 /data/jane_profile_07272018.doc
005 /data/jane_pic_07282018.jpg
008 /data/jane_contact_07292018.csv
"""







## Test command

"""We'll now use the test command to test for the presence of a file. 
The command test is a command-line utility on Unix-like operating systems that evaluates conditional expressions.
"""
# test EXPRESSION

"""We'll use this command to check if a particular file is present in the file system. 
We do this by using the -e flag. This flag takes a filename as a parameter and returns True if the file exists.
We'll check the existence of a file named jane_profile_07272018.doc"""

# if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
"""File exists"""

## Create a file using a Redirection operator

"""We'll now use the redirection operator (>) to create an empty file simply by specifying the file name. 
The syntax for this is: > [file-name] """

# > test.txt
"""
jane_contact_07292018.csv  jane_profile_07272018.doc  janez_profile_11042019.doc  
kwood_pic_04032017.jpg  kwood_profile_04022017.doc  list.txt  pchow_pic_05162019.jpg  test.txt
"""

# echo "I am appending text to this test file" >> test.txt
# cat test.txt
"""
I am appending text to this test file
"""







## Iteration

"""
    For: A for loop repeats the execution of a group of statements over a set of items.
    While: A while loop executes a set of instructions as long as the control condition remains true.
    Until: An until loop executes a set of instructions as long as the control condition remains false.
"""

# for i in 1 2 3; do echo $i; done
"""
1
2
3
"""






## Find files using bash script

"""
This script should catch all "jane" lines and store them in another text file called oldFiles.txt. 
Create the text file oldFiles.txt and make sure it's empty. This oldFiles.txt file should save files with username "jane".
Now, search for all lines that contain the name "jane" and save the file names into a variable. Let's call this variable files, we will refer to it with that name later in the lab.
Since none of the files present in the file list.txt are available in the file system, check if file names present in files variable are actually present in the file system. 
To do this, we'll use the test command that we practiced in the previous section.
Now, iterate over the files variable and add a test expression within the loop. 
If the item within the files variable passes the test, add/append it to the file oldFiles.txt.
"""

#cd ~/scripts
#nano findJane.sh


#!/bin/bash

> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for f in $files;do
  if [ -e $HOME$f ];then
  echo $HOME$f>>oldFiles.txt
  fi
done


#chmod +x findJane.sh
#./findJane.sh
#cat oldFiles.txt

"""
/home/student-02-196e48437fa8/data/jane_profile_07272018.doc
/home/student-02-196e48437fa8/data/jane_contact_07292018.csv
"""



##Rename files using Python script

"""
Since oldFiles.txt is passed as a command line argument, it's stored in the variable sys.argv[1]. 
Open the file from the first argument to read its contents using open() method. 
You can either assign it to a variable or use a with block. Hint: traverse each line in the file using readlines() method. 
Use line.strip() to remove any whitespaces or newlines and fetch the old name.

Once you have the old name, use replace() function to replace "jane" with "jdoe". 
This method replaces occurrences of any older substring with the new substring. 
The old and new substrings are passed as parameters to the function. 
Therefore, it returns a string where all occurrences of the old substring is replaced with the new substring.

Now, invoke a subprocess by calling run() function. This function takes arguments used to launch the process. 
These arguments may be a list or a string.
In this case, you should pass a list consisting of the command to be executed, followed by arguments to the command.
Use the mv command to rename the files in the file system. This command moves a file or directory. 
It takes in source file/directory and destination file/directory as parameters. 
We'll move the file with old name to the same directory but with a new name.

Now it must be clear. You should pass a list consisting of the mv command, 
followed by the variable storing the old name and new name respectively to the run() function within the subprocess module.
"""


#nano changeJane.py

#!/usr/bin/env python3

import sys
import subprocess

f = open(sys.argv[1], "r")
for line in f.readlines():
        old_name = line.strip()
        new_name = old_name.replace("jane", "jdoe")
        subprocess.run(["mv", old_name, new_name])
f.close()


#chmod +x changeJane.py
#./changeJane.py oldFiles.txt
#cd ~/data
#ls

"""
janez_profile_11042019.doc  jdoe_contact_07292018.csv  
jdoe_profile_07272018.doc  kwood_pic_04032017.jpg  
kwood_profile_04022017.doc  list.txt  pchow_pic_05162019.jpg  test.txt
"""


