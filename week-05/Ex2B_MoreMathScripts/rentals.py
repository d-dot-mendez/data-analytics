import math

xpeople = 144
charter_vans = 15
vans = 250
total_vans = math.ceil(xpeople/charter_vans)
cost = vans*total_vans

#Now with 38 tourists

tourists = 38
charter_vans = 15
vans_price = 250
total_vans = math.ceil(tourists/charter_vans)
tourists_cost = vans_price*total_vans
per_tourist = tourists_cost/tourists

#A) My script says each person has to be charged $19.74
#B) I collected $750
#C) The vans were $750 in total
#D) I don't have leftover money and I think that is because I used the ceil function for total_vans because you cannot \
#   have a portion of a van.

print(round(per_tourist, 2))
print(tourists_cost)


