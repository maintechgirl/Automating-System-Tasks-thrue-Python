###Unit Testing


###Manual Test

#rearrenge.py

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])

# from rearrange import rearrange_name
# rearrange_name("Lovelace, Ada")    #"Ada Lovelace"





###Automatic Test


#rearrenge.py

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])


#rearrenge_test.py

#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()    

#chmod +x rearrange_test.py
#./rearrange_test.py            #OK





###Edge Cases


#rearrenge_test.py

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

   def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)




unittest.main()  

#chmod +x rearrange_test.py
#./rearrange_test.py            #(def test_empty)         TypeError: "NoneType" object is not subscriptable
                                #(def test_double_name)   OK 
                                #(def test_one_name)      AssertionError: "" != "Voltaire"


#rearrenge.py

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return ""
    return "{} {}".format(result[2], result[1])


#./rearrange_test.py            #(def test_empty)          OK  


#rearrenge.py

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


#./rearrange_test.py            #(def test_one_name)     Ok




###Practice Notebook - Unit Tests and Edge Cases



#letters.py

import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))   #['a', 'b']



#letter_test.py


from letters import LetterCompiler
import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main(argv = ['first-arg-is-ignored'], exit = False)

class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)


unittest.main(argv = ['first-arg-is-ignored'], exit = False)



# EDGE CASES HERE

def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(LetterCompiler(testcase), expected)
        
def test_word(self):
        testcase = "awesome"
        expected = ['a']
        self.assertEqual(LetterCompiler(testcase), expected)
        
def test_unmatch(self):
        testcase = "go"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

if __name__ == "__main__":
	unittest.main()



### The Try-Except Construct


def read_file(filename):
    if not os.path.exist(filename):
        return ""
    if not os.path.isfile(filename):
        return ""
    if not os.access(filename, os.R_OK):
        return ""
    if is_locked(filename):
        return ""
    if if_not_accessible(filename):
        return ""





# The Try-Except Construct Exzample

def character_frequency(filename):
    """Count a frequency of the each character in the given file"""
    #First try to open the file
    try: 
        f = open(filename)
    except OSError:
        return None
    
    #Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters




#Raising Errors

def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

#from validations import validate_user
#validate_user("", -1)
#
#ValueError: minlen must be at least 1

#validate_user("", 1)
#
#False

#validate_user("myuser", 1)
#
#True

#validate_user(88, 1)
#
#TyperError: object of type int has no len()

#validate_user([], 1)
#
#False

#validate_user(["name"], 1)
#
#AttributeError: list object has no attribute isalnum

def validate_user(username, minlen):
    asser type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

#from validations import validate_user

#validate_user([2], 1)
#
#AssertionErrorr: username must be a string





#Testing for Expected Errors

import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)
    
    def too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)

unittest.main()


#Practice Errors and Exceptions

my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    my_list.remove(myVal)
    return my_list

print(RemoveValue(27))  # [5, 9, 6, 8]

print(RemoveValue(27)) #ValueError: list.remove(x): x not in list

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27)) #ValueError: Value must be in the given list



my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list)) # ['after', 'east', 'inside', 'over', 'up']

my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list)) #TypeError: '<' not supported between instances of 'str' and 'int'

def OrganizeList(myList):
    for item in myList:
        assert type(myList)==str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list)) # AssertionError: Word list must be a list of strings



import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants)) #False

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
        try:
            f = open(participants)
            if my_participant_dict['Larry'] == 9:
                return True
            else:
                return False
        except TypeError:
                return None
    
participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants)) #None






#Implementing Unit Testing 


#emails_test.py

#!/usr/bin/env python3

import unittest
from emails import find_email

class TestFile(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)

  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)

  def test_two_name(self):
    testcase = [None, "Roy","Cooper"]
    expected = "No email address found"
    self.assertEqual(find_email(testcase), expected)

if __name__ == '__main__':
  unittest.main()



#emails.py.

#!/usr/bin/env python3

import csv
import sys


def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
     # If email exists, print it
    if email_dict.get(fullname.lower()):
      return email_dict.get(fullname.lower())
    else:
      return "No email address found"
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()
