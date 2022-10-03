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
print(dictionary_restaurant)
sorted_names = sorted(dictionary_restaurant.items())
    
for restaurant_name, rate in sorted_names:
    print(f'{restaurant_name} is ratesd at {rate}.')




