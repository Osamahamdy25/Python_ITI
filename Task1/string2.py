# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


#  testString
# Given a string, If it consists from only digits,
# return the sum of these digits as a string .
# e.x "1548" => "18"
# Elif the string consists from only alphabets,
# return the number of occurrences of each character in the string as a string.
# e.x "ABCABCABC" => "333333333" , "Google" => "222211", treat all as lower case (G=g)
# Else return the given string back
# Hint: you may need to use for and while statements 
def testString(s):

  if s.isdigit() :
    res=0
    for i in range (0,len(s)):
      res+=(int(s[i]))
    return str(res)
  elif s.isalpha() :
    res=''   
    s=s.lower();
    for i in s :
      res+=str(s.count(i))
    return res 
  else :
    return s
  
#  minipulateString
# Given a command and a delimiter and a target string 's', 
# If the command is 'join_str', return s joined by the given delim.
# Elif the command is 'split_str', split s using the delim and return the output.
# If the delim was an empty string use space as a default delim in both cases.
def minipulateString(command,delim,s):
  # +++your code here+++
  if delim=='':
    delim=' ' 
  if command=='join_str':
    s=delim.join(s)
  elif command=='split_str':
    s=s.split(delim)
  return s 
#  isunicode
# Given a string 's', 
# If the string is a unicode string return "This is a unicode string".
# Else return "This is a string"
def isunicode(s):
  # +++your code here+++
  return  
  


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' %(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('testString')
  test(testString('00000'), '0')
  test(testString('9876'), '30')
  test(testString('boOkkEeper'), '1222233131')
  test(testString('ITI 41'), 'ITI 41')

  print ()
  print ('minipulateString')
  test(minipulateString('join_str','~',['AB','AB','AB']), 'AB~AB~AB')
  test(minipulateString('split_str','-','ITI-41-ES'), ['ITI','41','ES'])
  test(minipulateString('join_str','',['This','tea','is','hot']), 'This tea is hot')
  

  print ()
  print ('isunicode')
  test(isunicode('test'), 'This is a string')
  test(isunicode(u'test'), 'This is a unicode string')

if __name__ == '__main__':
  main()
  