### MANAGING FILES WITH PYTHON

## HANDLING FILES

#cd data
#ls
#cat employees.csv

"""Full Name, Username, Department
Audrey Miller, audrey, Development
Arden Garcia, ardeng, Sales
Bailey Thomas, baileyt, Human Resources
Blake Sousa, sousa, IT infrastructure
Cameron Nguyen, nguyen, Marketing
Charlie Grey, greyc, Development
Chris Black, chrisb, User Experience Research
Courtney Silva, silva, IT infrastructure
Darcy Johnsonn, darcy, IT infrastructure
Elliot Lamb, elliotl, Development
Emery Halls, halls, Sales
Flynn McMillan, flynn, Marketing
Harley Klose, harley, Human Resources
Jean May Coy, jeanm, Vendor operations
Kay Stevens, kstev, Sales
Lio Nelson, lion, User Experience Research
Logan Tillas, tillas, Vendor operations
Micah Lopes, micah, Development
Sol Mansi, solm, IT infrastructure
"""


#cd ~/scripts
#nano generate_report.py

"""Convert employee data to dictionary

The goal of the script is to read the CSV file and generate a report with the total number of people in each department. 
To achieve this, we will divide the script into three functions.

Let's start with the first function: read_employees(). 
This function receives a CSV file as a parameter and returns a list of dictionaries from that file. 
Define the function read_employees. This function takes file_location (path to employees.csv) as a parameter.
Open the CSV file by calling open and then csv.DictReader.
DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), 
but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter. 
If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as the keys. 
So, in this case, the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter.
We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, 
so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. 
Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object.
Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance. 
We will now register a dialect empDialect.
You now need to iterate over the CSV file that you opened, i.e., employee_file. 
When you iterate over a CSV file, each iteration of the loop produces a dictionary from strings (key) to strings (value).
Append the dictionaries to an empty initialised list employee_list as you iterate over the CSV file.
Now return this list. To test the function, call the function and save it to a variable called employee_list. Pass the path to employees.csv as a parameter to the function. 
Print the variable employee_list to check whether it returns a list of dictionaries.
"""

#!/usr/bin/env python3

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list
employee_list = read_employees('/home/<username>/data/employees.csv')
print(employee_list)

#chmod +x generate_report.py
#./generate_report.py

"""[{'Department': 'Development', 'Username': 'audrey', 'Full Name': 'Audrey Miller'},
{'Department': 'Sales', 'Username': 'ardeng', 'Full Name': 'Arden Garcia'}, 
{'Department': 'Human Resources', 'Username': 'baileyt', 'Full Name': 'Bailey Thomas'}, 
{'Department': 'IT infrastructure', 'Username': 'sousa', 'Full Name': 'Blake Sousa'},
{'Department': 'Marketing', 'Username': 'nguyen', 'Full Name': 'Cameron Nguyen'}, 
{'Department': 'Development', 'Username': 'greyc', 'Full Name': 'Charlie Grey'}, 
{'Department': 'User Experience Research', 'Username': 'chrisb', 'Full Name': 'Chris Black'}, 
{'Department': 'IT infrastructure', 'Username': 'silva', 'Full Name': 'Courtney Silva'}, 
{'Department': 'IT infrastructure', 'Username': 'darcy', 'Full Name': 'Darcy Johnsonn'}, 
{'Department': 'Development', 'Username': 'elliotl', 'Full Name': 'Elliot Lamb'}, 
{'Department': 'Sales', 'Username': 'halls', 'Full Name': 'Emery Halls'}, 
{'Department': 'Marketing', 'Username': 'flynn', 'Full Name': 'Flynn McMillan'}, 
{'Department': 'Human Resources', 'Username': 'harley', 'Full Name': 'Harley Klose'}, 
{'Department': 'Vendor operations', 'Username': 'jeanm', 'Full Name': 'Jean May Coy'}, 
{'Department': 'Sales', 'Username': 'kstev', 'Full Name': 'Kay Stevens'},
{'Department': 'User Experience Research', 'Username': 'lion', 'Full Name': 'Lio Nelson'}, 
{'Department': 'Vendor operations', 'Username': 'tillas', 'Full Name': 'Logan Tillas'}, 
{'Department': 'Development', 'Username': 'micah', 'Full Name': 'Micah Lopes'}, 
{'Department': 'IT infrastructure', 'Username': 'solm', 'Full Name': 'Sol Mansi'}]"""




"""
Process employee data

The second function process_data() should now receive the list of dictionaries, i.e., 
employee_list as a parameter and return a dictionary of department:amount.

This function needs to pass the employee_list, received from the previous section, as a parameter to the function.
Now, initialize a new list called department_list, iterate over employee_list, and add only the departments into the department_list.
The department_list should now have a redundant list of all the department names. We now have to remove the redundancy and return a dictionary. 
We will return this dicationary in the format department:amount, where amount is the number of employees in that particular department.
Now, call this function by passing the employee_list from the previous section. Then, save the output in a variable called dictionary. Print the variable dictionary.

"""

#nano generate_report.py

#!/usr/bin/env python3

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list
employee_list = read_employees('/home/<username>/data/employees.csv')
print(employee_list)

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
dictionary = process_data(employee_list)
print(dictionary)

#./generate_report.py

"""
{'Sales': 3, 'Development': 4, 'Marketing': 2, 'User Experience Research': 2, 'Human Resources': 2, 'Vendor operations': 2, 'IT infrastructure': 4}
"""



"""
Generate a report

Next, we will write the function write_report. This function writes a dictionary of department: amount to a file.

The report should have the format:
<department1>: <amount1>
<department2>: <amount2>

This function requires a dictionary, from the previous section, and report_file, an output file to generate report, to both be passed as parameters.
You will use the open() function to open a file and return a corresponding file object. 
This function requires file path and file mode to be passed as parameters. The file mode is 'r' (reading) by default, 
so you should now explicitly pass 'w+' mode (open for reading and writing, overwriting a file) as a parameter.
Once you open the file for writing, iterate through the dictionary and use write() on the file to store the data.
Now call the function write_report() by passing a dictionary variable from the previous section and also passing a report_file. 
The report_file passed within this function should be similar to /home/<username>/data/report.txt. 
Replace <username> with the one mentioned in Connection Details Panel at left-hand side.
This script does not generate any output, but it creates a new file named report.txt within the data directory. 
This report.txt file should now have the count of people in each department.
"""

#nano generate_report.py


#!/usr/bin/env python3

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list
employee_list = read_employees('/home/<username>/data/employees.csv')
print(employee_list)

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
dictionary = process_data(employee_list)
print(dictionary)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()
write_report(dictionary, '/home/<username>/data/report.txt')

#./generate_report.py
#cd ~/data
#ls
#cat report.txt

"""
Development:4
Human Resources:2
IT infrastructure:4
Marketing:2
Sales:3
User Experience Research:2
Vendor operations:2
"""
