import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

#4A-Product of the day
print(random.choice(products))

#4B-Usability Survey
print(random.sample(products, 3))

#4C- Avoid Appearance of Ranking
random.shuffle(products)
print(products)

#4D- Random number 50-300
print(random.randint(50,300))