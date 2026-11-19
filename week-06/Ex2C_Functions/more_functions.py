#The mailing address function
def display_mailing_label(name, address, city, state, zip):
    place = (f"{name}, {address}, {city}, {state}, {zip}")
    return place

print(display_mailing_label("Beyonce", "223 Mandela", "Bel-Air", "California", "19054"))
print(display_mailing_label("Rihanna", "556 Nelson", "Irish Spring", "Ireland", "19484"))

#The number function
def add_numbers(*args):
    # Add all the arguments together
    total = sum(args)

    # Build the left side: start with the first number, then add " + " and each remaining number
    text = str(args[0])
    for n in args[1:]:
        text = text + " + " + str(n)

    # Display the result in the format: number + number2 + ... = result
    print(f"{text} = {total}")

add_numbers(5, 4, 7, 8, 9)
add_numbers(3)
add_numbers(3,2)

#receipt
def display_receipt(total_due, amount_paid):
    receipt = (f"Total Due: ${total_due}\n"
               f"Amount Paid: ${amount_paid}\n"
               f"Change Due: ${amount_paid - total_due}")
    return receipt

print(display_receipt(5,20))
print(display_receipt(7,17))
print(display_receipt(65,73))