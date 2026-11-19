class Restaurant():
    """This class is used to describe the foods being sold in restaurants"""
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        message = print(f"{self.rest_name} serves {self.food_type}.")
        

    def rest_open(self):
        output = print(f"{self.rest_name} is open.")

#Testing the class and methods 
my_rest = Restaurant ("Rubie's Smoothies", "boba tea")
my_rest.describe_rest()
my_rest.rest_open()

#Three restaurants using the class and methods
#Restaurant 1
my_rest = Restaurant ("MJ's Journey", "Soul Food")
my_rest.describe_rest()
my_rest.rest_open()

#Restaurant 2
my_rest = Restaurant ("Mickey's Wonderland", "Ice Cream")
my_rest.describe_rest()
my_rest.rest_open()

#Restaurant 3
my_rest = Restaurant ("Tiana's Diner", "Jamaican food")
my_rest.describe_rest()
my_rest.rest_open()