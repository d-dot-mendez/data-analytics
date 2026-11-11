# Description: This script tests various numeric
#              conversion techniques
# Author: Denae M. New Programmer


a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

#Casting as an integer
#a- an error message showed up, probably because the decimal will make it a float. 
#b- This works just fine
#c- an error message popped up, most likely due to the text.
#d- an error message popped up, most likely for the same reason as c

#Casting as a float
#a- Now it is able to convert to a number because ot is using the correct numeric type.
#b- Deespite b originally being a string, the computer converted it into a float and added a decimal to it
#c- An error message popped up, again this is most likely due to the text
#d- An error message popped up, again this is most likely due to the same reason as c

#This is for the 'c' part of the labwork.
#Once we converted a into a float first, we were able to convert it into an integer
print(int(float(a)))

#This is for d 

print(len(c)) #11
print(len(d)) #9

c_num = int(c[:3])
d_1   = d.strip()
d_num = int(d_1[-1:])

print(c_num)
print(d_num)

#This for e

a_1 = a.strip()
print(a_1)
print(d_1)

