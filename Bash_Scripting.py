# Basic Linux Command

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



#Redirecting Streams


#cat stdout_example.py

#!/usr/bin/env python3

print("Dont mind me, just a bit of text here...")

#./stdout_example.py
Dont mind me, just a bit of text here...
#./stdout_example,py > newfile.txt
#cat newfile.txt
Dont mind me, just a bit of text here...
#./stdout_example,py >> newfile.txt        ##append the output of a command to a .txt file
#cat newfile.txt
Dont mind me, just a bit of text here...
Dont mind me, just a bit of text here...


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
