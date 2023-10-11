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