import math

box = 12
length = 100
width = 250 
dimension = length*width 
tiles_needed = dimension/box
tiles_bought = (tiles_needed *.1) + tiles_needed

print(dimension)
print(tiles_needed)
print(tiles_bought)
print(math.ceil(tiles_bought))
