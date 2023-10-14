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












