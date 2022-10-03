"""Restaurant rating lister."""


# put your code here

read_file = open("scores.txt")
dictionary_restaurant = {}

for line in read_file:
    line = line.rstrip()
    line = line.split(":")
    restaurant_name = line[0]
    rate = line[1]

    dictionary_restaurant[restaurant_name] = rate

sorted_names = sorted(dictionary_restaurant.items())
    
for restaurant_name, rate in sorted_names:
    print(f'{restaurant_name} is rated at {rate}.')

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
