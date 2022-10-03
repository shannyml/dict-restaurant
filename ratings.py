"""Restaurant rating lister."""
from random import choice
read_file = open("scores.txt")
on = True

dictionary_restaurant = {}
restaurants = []
for line in read_file:
    line = line.rstrip()
    line = line.split(":")
    restaurant_name = line[0]
    rate = line[1]
    restaurants.append(restaurant_name)
    dictionary_restaurant[restaurant_name] = rate
sorted_names = sorted(dictionary_restaurant.items())

while on: 
    user_choice = input("You can choose ratings(R), add(A), random restaurant update(U), or quit(Q)").title()
    
    if user_choice == "R":
            
        for restaurant_name, rate in sorted_names:
            print(f'{restaurant_name} is rated at {rate}.')
        pass
    elif user_choice == "A":
        new_restaurant = input("Restaurant name:").title()
        new_rate = input("Rate:")

        if int(new_rate) < 0 or int(new_rate) > 6:
            print("Rate should be between 1 and 5")
            new_rate = input("Rate:")
        else: 
            dictionary_restaurant[new_restaurant] = new_rate

        sorted_names = sorted(dictionary_restaurant.items())

        for restaurant_name, rate in sorted_names:             
            print(f'{restaurant_name} is rated at {rate}.')
        pass
    elif user_choice == "U":
        random_restaurant = choice(restaurants)
        print(f"The restaurant is {random_restaurant}. The current rating is {dictionary_restaurant[random_restaurant]}")
        new_rate = input("Rate:")
        if int(new_rate) < 0 or int(new_rate) > 6:
            print("Rate should be between 1 and 5")
            new_rate = input("Rate:")
        else: 
            dictionary_restaurant[random_restaurant] = new_rate
        sorted_names = sorted(dictionary_restaurant.items())    
        pass
    elif user_choice == "Q":
        on = False
        break
    else: 
        pass
