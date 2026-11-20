class Restaurant():
    """This class is used to describe the foods being sold in restaurants"""
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []


#add numbers served
    def add_num_served(self): 
        customers_served = int(input("How many customers served today? "))
        self.number_served =+ customers_served

#print num served
    def  print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

#add customer rating
    def customer_rating(self):
        rating = int(input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? "))
        self.customer_ratings.append(rating)

        if rating < 0 or rating > 5:
                    print("Enter a number 1-5") 

        else:
             print(f"Your rating was {rating}. The average rating for this restaurant is "
              f"{(sum(self.customer_ratings))/(len(self.customer_ratings))}.")
        
    



    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
        

    def rest_open(self):
        output = print(f"{self.rest_name} is open.")

#Restaurant 1
my_rest = Restaurant ("MJ's Journey", "Soul Food")
my_rest.describe_rest()
my_rest.rest_open()
my_rest.add_num_served()
my_rest.print_num_served()
my_rest.customer_rating()


#Restaurant 2
my_rest = Restaurant ("Mickey's Wonderland", "Ice Cream")
my_rest.describe_rest()
my_rest.rest_open()
my_rest.add_num_served()
my_rest.print_num_served()
my_rest.customer_rating()



#Restaurant 3
my_rest = Restaurant ("Tiana's Diner", "Jamaican food")
my_rest.describe_rest()
my_rest.rest_open()
my_rest.add_num_served()
my_rest.print_num_served()
my_rest.customer_rating()