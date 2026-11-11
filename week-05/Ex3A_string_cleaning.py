name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

#Using .lower()
print(name_1.lower())
print(name_2.lower()) 
print(name_3.lower())

#using.title()
print(name_1.title())
print(name_2.title())
print(name_3.title())

#using.replace()
#Even though I removed the dollar sign, both of the variables for salary is still a string data type.
#In order to perform math calculations on them, I would have to type cast the variables as an integer.
#I would also have to remove the commas before doing so.
print(salary_1.replace("$",""))
print(salary_2.replace("$",""))

new_salary_1 = salary_1.replace("$","")
new_salary_2 = salary_2.replace("$","")

print(type(new_salary_1)) #string
print(type(new_salary_2)) #string

#using the replace.() and type casting data into an integer
new_salary1 = new_salary_1.replace(",", "")
new_salary1 = int(new_salary1)
print(type(new_salary1))
