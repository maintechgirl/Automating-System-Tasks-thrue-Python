#Advanced Regular Expressions

import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
#re.Match object; span=(2, 7), match='ghost'>
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
#re.Match object; span=(2, 7), match='scary'>
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
#['scary', 'ghost', 'appea']
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
#['scary', 'ghost', 'appea']
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
#['scary', 'ghost']
print(re.findall(r"\w{5,10}", "I really like strawberries"))
#['really', 'strawberri']
print(re.findall(r"\w{5,}", "I really like strawberries"))
#['really', 'strawberries']
print(re.search(r"s\w{,20}", "I really like strawberries"))
#re.Match object; span=(14, 26), match='strawberries'>
 

#Problem: The long_words function returns all words that are at least 7 characters.
#  Fill in the regular expression to complete this function. 

def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []





#Extracting a PID Using regexes in Python

log = "July 31 04:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])  
#12345

result = re.search(regex, "A completly different string that also has numbers [34567]")
print(result)  #<re.Match object; span=(51, 58), match='[34567]'>   

#34567
result = re.search(regex, "99 elephans in a [cage]")
print(result[1])
#TypeError: 'NoneType' object is not subscriptable

#Solution for the past example:

log = "July 31 04:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

def extract_pid(log_line):
  regex = r"\[(\d+)\]"
  result = re.search(regex, log_line)
  if result is None:
      return ""
  return result[1]

print(extract_pid(log))
#12345

print(extract_pid("99 elephans in a [cage]"))
#Right. Its didnt match so it returned emphty string. That exactly what we wanted.



#Problem: Add to the regular expression used in the extract_pid function, 
# to return the uppercase message in parenthesis, after the process id.

def extract_pid(log_line):
    regex = r"\[(\d+)\]\: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)





#Splitting and Replacing

re.split(r"[.?!]", "One sentence. Another one? And the last one!")  #['One sentence', ' Another one', ' And the last one', '']
re.split(r"([.?!])", "One sentence. Another one? And the last one!") #['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com" )   #'Received an email for [REDACTED]'

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")





#Practice Quiz: Advanced Regular Expressions



#Problem: We're working with a CSV file, which contains employee information. 
# Each record has a name field, followed by a phone number field, and a role field. 
# The phone number field contains U.S. phone numbers, and needs to be modified to the international format, 
# with "+1-" in front of the phone number. Fill in the regular expression, using groups, to use the transform_record function to do that.

import re
def transform_record(record):
  new_record = re.sub(r",([\d\-]+),", r",+1-\1,", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer



#Problem: The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). 
# Fill in the regular expression to do that.

import re
def multi_vowel_words(text):
  pattern = r"\w*(?:a|e|i|o|u){3,}\w*"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []



#Problem:  The transform_comments function converts comments in a Python script into those usable by a C compiler. 
# This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), 
# which is the C single-line comment indicator. 
# For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, 
# and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., 
# as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the 
# substitution method to complete this function:  

import re
def transform_comments(line_of_code):
  result = re.sub(r"(#+)","//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"


#Problem: The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 
# 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. 
# Fill in the regular expression to complete this function.

import re
def convert_phone_number(phone):
  result = re.sub(r"(#+)","//", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300