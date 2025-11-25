#Exercise 1: Favorite Numbers
my_fav_numbers = {1,2,3,80}
my_fav_numbers.add(15)
my_fav_numbers.remove(15)
print(my_fav_numbers)
my_fav_numbers_friend = {16,19,33}
print(my_fav_numbers_friend)
me_my_friend =my_fav_numbers.union(my_fav_numbers_friend)
print(me_my_friend)
#Exercise 2: Tuple
tuple1=(1,3,6)
print(tuple1)
tuple2=tuple1 + (7,)
print(tuple2)
#Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("kiwi")
basket.insert(0,"Apples")
count_apples = basket.count("Appeles")
basket.clear()
print(basket)
#Exercise 4: Floats
mixed_liste=[]
current_number = 1.5
while current_number <= 5:
    mixed_liste.append(current_number)
    current_number += 0.5
print(mixed_liste)
#Exercice 5: for loop
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for lists in list:
    print(lists)
#Exercise 6: While Loop
name = input("what's your name?")
while len(name) < 3 or name.isdigit():
    name = input("what's your name?")
print('thank you')
#Exercise 7: Favorite Fruits
fruit = input("enter your favorit fruit (separated by spaces) ")
fruits = fruit.split()
favorite_fruits= input("enter the name of  a fruit")
if fruit in fruits :
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
# Exercise 8: Pizza Toppings
toppings = []
base_price = 10
topping_price = 2.5

while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    if topping.lower() == "quit":
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + len(toppings) * topping_price

print("\n--- Your Pizza Order ---")
print("Toppings:", toppings)
print(f"Total cost: ${total_cost:.2f}")
#Exercise 9: Cinemax Tickets
total = 0

while True:
    age = input("Enter the age of a family member (or 'stop' to finish): ")

    if age.lower() == "stop":
        break

    if not age.isdigit():
        print("Please enter a valid number.")
        continue

    age = int(age)

    if age < 3:
        print("Ticket: free")
        price = 0
    elif age <= 12:
        print("Ticket: $10")
        price = 10
    else:
        print("Ticket: $15")
        price = 15

    total += price

print("Total ticket cost: $", total)
