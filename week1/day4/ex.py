#Exercise 1: What Are You Learning?
def display_messagr():
      print("I am learning about functions in Python.")

display_messagr()
#Exercice 2:What’s Your Favorite Book?
def favorite_book(title):
  print("One of my favorite books is "+title)
favorite_book("alice in wonderland")     
#Exercise 3: Some Geography
def describe_city(city,country= "unknown"):
     print(city   + " is in " + country)
describe_city("casablanca, maroc")
describe_city("paris")
#Exercise 4: Random
import random

def compare_number(user_number):
    random_number = random.randint(1,100)

    if  user_number == random_number:
       print("succes!you gyessed the number.")
    else :
       print(f"fail!your number:{user_number} ,Random number : {random_number}")
compare_number(55)
compare_number(22)
#exercise 5: Let’s Create Some Personalized Shirts!
def make_shirt(size,text):
    print(f"the size of shirt is{size}  and the text is {text} ")
   
make_shirt("large","i love python")
def make_shirt(size = "meduim", texte = "i loove python"):
    print(f"the size of the shirt is {size}and the text is {texte}.")
make_shirt()
make_shirt("medium")
make_shirt("small", "custom message")
make_shirt(size="large", texte = "hello")
make_shirt(texte = "python", size ="meduim")
#Exercise 6: Magicians
magician_names = ['harry houdini','david blaine','criss angel']
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for i in range(len(magicians)):
       magicians[i]= "the great"+ magicians[i]
show_magicians(magician_names)
make_great(magician_names)
#Exercise 7: Temperature Advice
import random 
def get_random_temp():
    temp = random.randint(-10,40)
    return temp
def main():
    temperature = get_random_temp()
    print(f"the temperature right now is {temperature}degrees celsius.")
    if temperature < 0 :
       print("brrr,that's freezing ! waer some extra layers todays.")
    elif  0 <= temperature < 16 :
      print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 23 :
       print("nice weather")
    elif 24 <= temperature < 32 : 
      print("it's really hot! stay cool")
main()   
def main():
    month = int(input("enter a month (1-12):"))
    if month in [12 ,1, 2]:
       season= "winter"
    elif month in [3 ,4, 5]:
       season="spring"
    elif month in [6 ,7, 8]:
       season=   "summer"
    elif month in [9 ,10, 11]:
       season= "autumn"
    else: 
       print("invalid month!") 
main()