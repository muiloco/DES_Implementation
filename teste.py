# Python3 code to demonstrate working of 
# Converting String to binary 
# Using join() + ord() + format() 
  
# initializing string  
test_str = "a23456789fdc1abb"
  
# printing original string  
print("The original string is : " + str(test_str)) 
  
# using join() + ord() + format() 
# Converting String to binary 
res = "{0:b}".format(test_str).zfill(64)
  
# printing result  
print("The string after binary conversion : " + res) 