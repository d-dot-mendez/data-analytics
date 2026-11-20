#f = open("about_me.txt", "r")
#print(f.read())

f = open("about_me.txt", "r")
#print(f.read(50))
#print(f.read(50))

#With the first print statement, only the first fifty characters appeared. When I added the second
#print statement, it continued where it left off, showing the next set of fifty characters. 

#print(f.readline(10))
#print(f.readline())

#for i in range(1, 5):
#    print(f.readline())

#Where there is only one for loop statement, the computer displays lines 1-4. The index (i) in the
#readline method are the lines in the text rather than the characters or words. 
#When used with other statements, it continues from where the previous statements left off. 

#Questions:
# What do you get when you print using .readlines(1) with no argument specified?
#When no arguemnt is specified,the methord will return the entire text.
#When only one line is specified, only one line of code returns in brackets.

# Add another print statement using .readlines(1) – what do you get?
#Two lines of code appears in brackets

# Add a print statement using .readlines(10) – what do you get?
#Interestingly enough, three lines of code appeared.

# Add another print statement using .readlines(10), and comment out the first two
# print statements using .readlines(1) – now what do you get?
#The output is two lines of code.

# What do you get with .readlines(100)?
#The output returned the first three lines in the paragraph, but it listed it side by side
#despite there being indentations in the paragraph. 

#  How about .readlines(-1)?
#It returned the entire paragraph.

#print(f.readlines(1))
#print(f.readlines(1))
#print(f.readlines(10))
#print(f.readlines(10))
#print(f.readlines(100))
#print(f.readlines(-1))

print(f.read(50))
print(f.readline(4))
print(f.readlines(100))
f.close()