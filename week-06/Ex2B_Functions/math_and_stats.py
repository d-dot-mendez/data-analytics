import random
import math
import statistics

vals_1_100   = range(1,100)
vals_sample  = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius       = random.randint(3,10)
pi           = math.pi

#_Experimenting with a subset of integers 1-100:
#Sum of 75 sample values from 1 to 100: ____
#Average of 75 sample values: ____
#Median of 75 sample values: ____
ex_1_sum = sum(vals_sample)
ex_1_avg = statistics.mean(vals_sample)
ex_1_med = statistics.median(vals_sample)

print(f"Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {ex_1_sum}")
print(f"Average of 75 sample values: {ex_1_avg}")
print(f"Median of 75 sample values: {ex_1_med}")

#_Experimenting with a superset of 200 values, integers 1-100:
#Average of 200 values: ____
#Median of 200 values: ____
#Mode of 200 values: ____
#Standard deviation of 200 values: ____
#Variance of 200 values: ____

vals_sample_2  = vals_choices  #Variable for 200 sample

ex_2_avg = statistics.mean(vals_sample_2)
ex_2_med = statistics.median(vals_sample_2)
ex_2_mode = statistics.mode(vals_sample_2)
ex_2_stdev = statistics.stdev(vals_sample_2)
ex_2_var = statistics.variance(vals_sample_2)
                               

print(f"Experimenting with a superset of 200 values, integers 1-100:\n"
      f"Average of 200 values: {ex_2_avg}\n"
      f"Median of 200 values: {ex_2_med}\n"
      f"Mode of 200 values: {ex_2_mode}\n"
      f"Standard deviation of 200 values: {ex_2_stdev}\n"
      f"Variance of 200 values: {ex_2_var}")

#Modeling a random circle:
#Radius = __, area = ____ (rounded up to the nearest integer)
#Radius = __, area = ____ (rounded down to the nearest integer)

r = radius
area = pi * (r**2)


print(f"The radius is {r}, so the area rounded down is {math.floor(area)}\n"
      f"The radius is {r} so the area rounded up is {math.ceil(area)}")