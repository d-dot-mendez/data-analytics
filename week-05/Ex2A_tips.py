# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
#print("The total due is " + str(total_due))

#Technically, the "total_due" would be a float and the computer would be confused as to what to do \
# Because it would think we are trying to add text with a number when we are really just tryinf to include \
#the number in the phrase. To get around this, we would have to convert the float into a string so that the \
# computer understands to include the float into the phrase. 

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))