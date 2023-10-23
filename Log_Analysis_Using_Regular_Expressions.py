### Log Analysis Using Regular Expressions 

"""Introduction

Imagine your company uses a server that runs a service called ticky, an internal ticketing system. 
The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand 
how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will 
process the system log and generate reports based on the information extracted from the log files.
What you'll do:
    Use regex to parse a log file
    Append and modify values in a dictionary
    Write to a file in CSV format
    Move files to the appropriate directory for use with the CSV->HTML converter"""


"""Exercise - 1

Working with a log file named syslog.log, which contains logs related to ticky.
In this section, we'll search and view different types of error messages. 
The error messages for ticky details the problems with the file with a timestamp for when each problem occurred."""

# cat syslog.log
"""
Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (username)
Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (username)
Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (username)
Jan 31 00:44:34 ubuntu.local ticky: ERROR Permission denied while closing ticket (username)
"""

# grep ticky syslog.log
"""
Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)
Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)
Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)
Jan 31 00:44:34 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)
Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)
Jan 31 01:29:16 ubuntu.local ticky: INFO Commented on ticket [#6518] (rr.robinson)
Jan 31 01:33:12 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mcintosh)
Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)
Jan 31 01:49:29 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mdouglas)
Jan 31 02:30:04 ubuntu.local ticky: ERROR Timeout while retrieving information (oren)
"""

# grep "ERROR" syslog.log
"""
Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)
Jan 31 00:44:34 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)
Jan 31 01:33:12 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mcintosh)
Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)
Jan 31 01:49:29 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mdouglas)
Jan 31 02:30:04 ubuntu.local ticky: ERROR Timeout while retrieving information (oren)
Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)
Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)
Jan 31 03:08:55 ubuntu.local ticky: ERROR Ticket doesn't exist (blossom)
Jan 31 03:39:27 ubuntu.local ticky: ERROR The ticket was modified while updating (bpacheco)
"""

# grep "ERROR Tried to add information to closed ticket" syslog.log
"""
Jan 31 01:33:12 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mcintosh)
Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)
Jan 31 01:49:29 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mdouglas)
Jan 31 04:31:49 ubuntu.local ticky: ERROR Tried to add information to closed ticket (oren)
Jan 31 05:12:39 ubuntu.local ticky: ERROR Tried to add information to closed ticket (oren)
Jan 31 05:18:45 ubuntu.local ticky: ERROR Tried to add information to closed ticket (sri)
Jan 31 08:01:40 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)
Jan 31 09:04:27 ubuntu.local ticky: ERROR Tried to add information to closed ticket (noel)
"""

# python3
# import re
# line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"


"""To match a string stored in line variable, we use the search() method by defining a pattern."""

# re.search(r"ticky: INFO: ([\w ]*) ", line)
"""
<re.Match object; span=(29, 57), match='ticky: INFO: Created ticket '>
"""


"""You can also get the ERROR message as we did for the INFO log above from the ERROR log line."""

# line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
# re.search(r"ticky: ERROR: ([\w ]*) ", line)
"""
<re.Match object; span=(29, 65), match='ticky: ERROR: Error creating ticket '>
"""




"""Exercise - 2

Use the Python interactive shell to create a dictionary."""


# fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
# sorted(fruit.items())
"""
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]
"""


"""We'll now sort the dictionary using the item's key. For this use the operator module.
Pass the function itemgetter() as an argument to the sorted() function. 
Since the second element of tuple needs to be sorted, pass the argument 0 to the itemgetter function of the operator module."""

# import operator
# sorted(fruit.items(), key=operator.itemgetter(0))
"""
[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]
"""


"""To sort a dictionary based on its values, pass the argument 1 to the itemgetter function of the operator module."""

#sorted(fruit.items(), key=operator.itemgetter(1))
"""
[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]
"""


"""Finally, you can also reverse the order of the sort using the reverse parameter. This parameter takes in a boolean argument.
To sort the fruit object from most to least occurrence, we pass the argument reverse=True."""

# sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)
"""
[('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]
"""

# exit()





"""Exercise - 3

We'll now work with a file named csv_to_html.py. 
This file converts the data in a CSV file into an HTML file that contains a table with the data."""

#!/usr/bin/env python3
import sys
import csv
import os

def process_csv(csv_file):
    """Turn the contents of the CSV file into a list of lists"""
    print("Processing {}".format(csv_file))
    with open(csv_file,"r") as datafile:
        data = list(csv.reader(datafile))
    return data

def data_to_html(title, data):
    """Turns a list of lists into an HTML table"""

    # HTML Headers
    html_content = """
<html>
<head>
<style>
table {
  width: 25%;
  font-family: arial, sans-serif;
  border-collapse: collapse;
}

tr:nth-child(odd) {
  background-color: #dddddd;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
</style>
</head>
<body>
"""

    # Add the header part with the given title
    html_content += "<h2>{}</h2><table>".format(title)

    # Add each row in data as a row in the table
    # The first line is special and gets treated separately
    for i, row in enumerate(data):
        html_content += "<tr>"
        for column in row:
            if i == 0:
                html_content += "<th>{}</th>".format(column)
            else:
                html_content += "<td>{}</td>".format(column)
        html_content += "</tr>"

    html_content += """</tr></table></body></html>"""
    return html_content


def write_html_file(html_string, html_file):

    # Making a note of whether the html file we're writing exists or not
    if os.path.exists(html_file):
        print("{} already exists. Overwriting...".format(html_file))

    with open(html_file,'w') as htmlfile:
        htmlfile.write(html_string)
    print("Table succesfully written to {}".format(html_file))

def main():
    """Verifies the arguments and then calls the processing function"""
    # Check that command-line arguments are included
    if len(sys.argv) < 3:
        print("ERROR: Missing command-line argument!")
        print("Exiting program...")
        sys.exit(1)

    # Open the files
    csv_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check that file extensions are included
    if ".csv" not in csv_file:
        print('Missing ".csv" file extension from first command-line argument!')
        print("Exiting program...")
        sys.exit(1)

    if ".html" not in html_file:
        print('Missing ".html" file extension from second command-line argument!')
        print("Exiting program...")
        sys.exit(1)

    # Check that the csv file exists
    if not os.path.exists(csv_file):
        print("{} does not exist".format(csv_file))
        print("Exiting program...")
        sys.exit(1)

    # Process the data and turn it into an HTML
    data = process_csv(csv_file)
    title = os.path.splitext(os.path.basename(csv_file))[0].replace("_", " ").title()
    html_string = data_to_html(title, data)
    write_html_file(html_string, html_file)

if __name__ == "__main__":
    main()


# sudo chmod +x csv_to_html.py

# nano user_emails.csv

Full Name, Email Address
Blossom Gill, blossom@abc.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@abc.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@abc.edu
Aurora Grant, enim.non@abc.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@abc.edu
Simon Rivera, sri@abc.edu
Benedict Pacheco, bpacheco@abc.edu
Maisie Hendrix, mai.hendrix@abc.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@abc.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@abc.edu
Bree Campbell, breee@utnisia.net



"""To visualize the data in the user_emails.csv file, you have to generate a webpage that'll be served by the webserver running on the machine.
The script csv_to_html.py takes in two arguments, the CSV file, 
and location that would host the HTML page generated. Give write permission to the directory that would host that HTML page:"""

# sudo chmod  o+w /var/www/html

"""Next, run the script csv_to_html.py script by passing two arguments: user_emails.csv file and the path /var/www/html/. 
Also, append a name to the path with an HTML extension. This should be the name that you want the HTML file to be created with."""

# ./csv_to_html.py user_emails.csv /var/www/html/emails.html

"""Navigate to the /var/www/html directory. Here, you'll find an HTML file created with the filename you passed to the above script."""

# ls /var/www/html

"""Now, to view this HTML page, open any web-browser and enter the following URL in the search bar."""

# [linux-instance-external-IP]/[html-filename].html





"""Generate reports

Now, we're going to practice creating a script, named ticky_check.py, that generates two different reports from this internal ticketing system log file i.e.,
syslog.log. This script will create the following reports:

    The ranking of errors generated by the system: A list of all the error messages logged and how many times each error was found, 
    sorted by the most common error to the least common error. This report doesn't take into account the users involved.

    The user usage statistics for the service: A list of all users that have used the system, 
    including how many info messages and how many error messages they've generated. This report is sorted by username.
"""

# nano ticky_check.py

"""Write a script to generate two different reports based on the ranking of errors generated by the system and the user usage statistics for the service. 

First, import all the Python modules that you'll use in this Python script. After importing the necessary modules, initialize two dictionaries: 
one for the number of different error messages and another to count the number of entries for each user (splitting between INFO and ERROR).

Now, parse through each log entry in the syslog.log file by iterating over the file.

For each log entry, you'll have to first check if it matches the INFO or ERROR message formats. You should use regular expressions for this. 
When you get a successful match, add one to the corresponding value in the per_user dictionary. 
If you get an ERROR message, add one to the corresponding entry in the error dictionary by using proper data structure.

After you've processed the log entries from the syslog.log file, you need to sort both the per_user and error dictionary before creating CSV report files.

Keep in mind that:

    The error dictionary should be sorted by the number of errors from most common to least common.
    The user dictionary should be sorted by username.

Insert column names as ("Error", "Count") at the zero index position of the sorted error dictionary. 
And insert column names as ("Username", "INFO", "ERROR") at the zero index position of the sorted per_user dictionary.

After sorting these dictionaries, store them in two different files: error_message.csv and user_statistics.csv.
"""


#!/usr/bin/env python3

import os
import re
import sys
import operator
import csv

error_counter = {}
error_user = {}
info_user = {}

#This function will read each line of the syslog.log file and check if it is an error or an info message.
def search_file():
    with open('syslog.log', "r") as myfile:
     for line in myfile:
        if " ERROR " in line:
            find_error(line)
            add_user_list(line, 1)
        elif " INFO " in line:
            add_user_list(line, 2)
    return


#If it is an error it will read the error from the line and increment into the dictionary
def find_error(str):
    match = re.search(r"(ERROR [\w \[]*) ", str)
    if match is not None:
        aux = match.group(0).replace("ERROR ", "").strip()
        if aux == "Ticket":
         aux = "Ticket doesn't exist"
        if not aux in error_counter:
            error_counter[aux] = 1
        else:
            error_counter[aux] += 1
    return

#This whill read the user from the string and add to the error or the info counter depending on the op number
def add_user_list(str, op):
    match = re.search(r'\(.*?\)', str)
    user = match.group(0)
    userA = user.strip("()")
    if op == 1:
        if not userA in error_user:
            error_user[userA] = 1
        else:
            error_user[userA] += 1
    elif op == 2:
        if not userA in info_user:
            info_user[userA] = 1
        else:
            info_user[userA] += 1
    return

#This function will read the list, arrange it and return a tuple with the dictionary items
def sort_list(op, list):
    if op == 1:
        s = sorted(list.items(), key=operator.itemgetter(1), reverse=True)
    elif op == 2:
        s = sorted(list.items(), key=operator.itemgetter(0))
    return s

#This is an extra function which will read the value of a user in the error dictionary and return its value if key exists
def getErrValue(keyV):
    for key, value in error_user:
        if key is keyV:
            return value
    return 0

#This function writes both csv files
def write_csv(op):
    if op == 1:
        with open('user_statistics.csv', 'w', newline='') as output:
            fieldnames = ['Username', 'INFO', 'ERROR']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in info_user:
                valError = getErrValue(key)
                csvw.writerow({'Username': key, 'INFO': value, 'ERROR': valError})
    if op == 2:
        with open('error_message.csv', 'w', newline='') as output:
            fieldnames = ['Error', 'Count']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in error_counter:
                csvw.writerow({'Error': key, 'Count': value})
    return

#This function adds zero to the other dictionary in case that user is not a key, it will add a key with the user and value 0
def add_zeros():
    for user in error_user.keys():
        if user not in info_user:
            info_user[user] = 0
    for user in info_user.keys():
        if user not in error_user:
            error_user[user] = 0
    return


#This will execute the functions
search_file()
add_zeros()
error_counter = sort_list(1, error_counter)
error_user = sort_list(2, error_user)
info_user = sort_list(2, info_user)
write_csv(1)
write_csv(2)




"""Visualize reports"""

# chmod +x ticky_check.py
# ./ticky_check.py

"""Executing ticky_check.py will generate two report file __error_message.csv __and user_statistics.csv.

You can now visualize the __error_message.csv __and user_statistics.csv by converting them to HTML pages. 
To do this, pass the files one by one to the script csv_to _html.py 
To convert the error_message.csv into HTML file run the following command:"""

# ./csv_to_html.py error_message.csv /var/www/html/error.html

"""To convert user_statistics.csv into HTML file, run the following command:"""

# ./csv_to_html.py user_statistics.csv /var/www/html/stat.html

"Now, to view these HTML pages, open any web-browser and enter the following URL in the search bar."

# [linux-instance-external-IP]/[html-filename].html
