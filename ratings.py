"""Restaurant rating lister."""

read_file = open("scores.txt")
on = True

dictionary_restaurant = {}
for line in read_file:
    line = line.rstrip()
    line = line.split(":")
    restaurant_name = line[0]
    rate = line[1]
    dictionary_restaurant[restaurant_name] = rate
sorted_names = sorted(dictionary_restaurant.items())

while on: 
    choice = input("You can choose ratings(R), add(A) or quit(Q)").title()
    
    if choice == "R":
            
        for restaurant_name, rate in sorted_names:
            print(f'{restaurant_name} is rated at {rate}.')
        pass
    elif choice == "A":
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
    elif choice == "Q":
        on = False
        break
    else: 
        pass
